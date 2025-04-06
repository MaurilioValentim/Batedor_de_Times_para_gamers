from models import Conta, Rank, Partida, Historico, engine
from sqlmodel import Session, select
from datetime import date

from models import Conta, Rank, Partida, Historico, engine
from sqlmodel import Session, select
from datetime import date


#====================================================================================================================================
#
#       Parte das Funcoes da Conta
#
#====================================================================================================================================

#Funcao para criar a conta. Possui as Entradas nome_real, nick e hashtag. Alem disso o Nome_real pode ser None
def criar_conta(conta: Conta):  # Entradas Nome_real , Nick ,  hashtag
    with Session(engine) as session:
        if conta.nome_real is not None:
            nome_existente = session.exec(
                select(Conta).where(Conta.nome_real == conta.nome_real)
            ).first()
            if nome_existente:
                print(f"Erro: nome_real {conta.nome_real} já está cadastrado.")
                return 

        # Verifica se nick + hashtag já existem juntos
        nick_hashtag_existente = session.exec(
            select(Conta).where(
                Conta.nick == conta.nick,
                Conta.hashtag == conta.hashtag
            )
        ).first()
        if nick_hashtag_existente:
            print(f"Erro: a combinação nick {conta.nick} e hashtag {conta.hashtag} já existe.")
            return 
        
        # Se passou pelas verificações, salva a conta
        session.add(conta)
        session.commit()

        print(f"Conta criada com sucesso! ID: {conta.id}")
        return 

# Funcao para excluir jogadores do banco de dados
def excluir_conta(conta = Conta):
    with Session(engine) as session:
         # Procura a conta com base em nome_real, nick e hashtag
        query = select(Conta).where(
            Conta.nome_real == conta.nome_real,
            Conta.nick == conta.nick,
            Conta.hashtag == conta.hashtag
        )
        conta_existente = session.exec(query).first()

        if conta_existente:
            session.delete(conta_existente)
            session.commit()
            print(f"Conta {conta.nick}#{conta.hashtag} excluída com sucesso.")
            return 
        else:
            print("Erro: Conta não encontrada.")
            return 

# Funcao para atualizar informacoes do jogador
# Vc deve passar o Nick e a Hashtag
# Vc pode mudar o Nome e o Nick
# Para mudar o Nick coloque None na parte do Novo Nome
def atualizar_informacoes_do_jogador(nick_atual: str, hashtag: str, novo_nome_real: str = None, novo_nick: str = None) -> str:
    with Session(engine) as session:
        # Verifica se a conta existe com o nick atual e hashtag
        conta = session.exec(
            select(Conta).where(Conta.nick == nick_atual, Conta.hashtag == hashtag)
        ).first()

        if not conta:
            print("Erro: Conta não encontrada com esse nick e hashtag.")
            return 

        # Atualiza os campos permitidos
        if novo_nome_real is not None:
            # Verifica se nome_real já está em uso por outra conta
            nome_ja_usado = session.exec(
                select(Conta).where(Conta.nome_real == novo_nome_real, Conta.id != conta.id)
            ).first()
            if nome_ja_usado:
                print(f"Erro: nome_real '{novo_nome_real}' já está em uso.")
                return 
            conta.nome_real = novo_nome_real

        if novo_nick is not None:
            # Verifica se nova combinação nick + hashtag já está sendo usada
            nick_ja_usado = session.exec(
                select(Conta).where(Conta.nick == novo_nick, Conta.hashtag == hashtag, Conta.id != conta.id)
            ).first()
            if nick_ja_usado:
                print(f"Erro: a combinação nick '{novo_nick}' e hashtag '{hashtag}' já existe.")
                return 
            conta.nick = novo_nick

        # Nenhum campo para atualizar
        if novo_nome_real is None and novo_nick is None:
            print("Nada foi atualizado. Forneça novo nome_real ou novo nick.")
            return 

        session.add(conta)
        session.commit()
        session.refresh(conta)
        print(f"Conta atualizada com sucesso: {conta.nome_real}, {conta.nick}#{conta.hashtag}")
        return 

# Funcao para retornar todos os jogadores cadastrados
def listar_jogadores():
    with Session(engine) as session:
        contas = session.exec(select(Conta)).all()
        jogadores = [[conta.nome_real, conta.nick, conta.hashtag] for conta in contas]
        return jogadores

#====================================================================================================================================
#
#       Parte das Funcoes do Ranked
#
#====================================================================================================================================


# Funcao para adicionar o rank da pessoa, precisa enviar todos os dados
def adicionar_rank(nick: str, hashtag: str, rank_do_lol: str, rank_local: str, pontuacao: float) -> str:
    with Session(engine) as session:
        # Busca a conta pelo nick e hashtag
        conta = session.exec(
            select(Conta).where(Conta.nick == nick, Conta.hashtag == hashtag)
        ).first()

        if not conta:
            return "Erro: Conta não encontrada."

        # Cria e adiciona o novo Rank
        novo_rank = Rank(
            conta_id=conta.id,
            rank_do_lol=rank_do_lol,
            rank_local=rank_local,
            pontuacao=pontuacao
        )

        session.add(novo_rank)
        session.commit()
        session.refresh(novo_rank)

        print(f"Rank adicionado com sucesso para {conta.nick}#{conta.hashtag}!")
        return 

# Funcao para obter informacoes do rank da pessoa, precisa do Nome Real ou do Nick
def informacoes_rank(nome_real: str = None, nick: str = None):
    with Session(engine) as session:
        # Consulta a conta com base no nome_real ou nick
        query = select(Conta).where(
            (Conta.nome_real == nome_real) if nome_real else (Conta.nick == nick)
        )
        conta = session.exec(query).first()

        if not conta:
            return "Conta não encontrada."

        # Acessa o relacionamento com Rank
        if conta.rank:
            return {
                "nick": conta.nick,
                "hashtag": conta.hashtag,
                "rank_do_lol": conta.rank.rank_do_lol,
                "rank_local": conta.rank.rank_local,
                "pontuacao": conta.rank.pontuacao
            }
        else:
            return "Esta conta não possui informações de rank."

# Funcao para excluir o rank da pessoa
def excluir_rank(nick: str, hashtag: str) -> str:
    with Session(engine) as session:
        conta = session.exec(
            select(Conta).where(Conta.nick == nick, Conta.hashtag == hashtag)
        ).first()

        if not conta:
            return "Erro: Conta não encontrada."

        rank = session.exec(
            select(Rank).where(Rank.conta_id == conta.id)
        ).first()

        if not rank:
            return "Erro: Essa conta não possui rank para excluir."

        session.delete(rank)
        session.commit()
        return f"Rank excluído com sucesso para {nick}#{hashtag}!"


# Funcao para atualizar o rank de uma pessoa
def atualizar_rank(nick: str, hashtag: str, rank_do_lol: str = None, rank_local: str = None, pontuacao: float = None) -> str:
    with Session(engine) as session:
        conta = session.exec(
            select(Conta).where(Conta.nick == nick, Conta.hashtag == hashtag)
        ).first()

        if not conta:
            return "Erro: Conta não encontrada."

        rank = session.exec(
            select(Rank).where(Rank.conta_id == conta.id)
        ).first()

        if not rank:
            return "Erro: Essa conta não possui rank para atualizar."

        # Atualiza apenas os valores que foram passados
        if rank_do_lol is not None:
            rank.rank_do_lol = rank_do_lol
        if rank_local is not None:
            rank.rank_local = rank_local
        if pontuacao is not None:
            rank.pontuacao = pontuacao

        session.add(rank)
        session.commit()
        session.refresh(rank)

        return f"Rank atualizado com sucesso para {nick}#{hashtag}!"


#====================================================================================================================================
#
#       Parte das Funcoes da Partida
#
#====================================================================================================================================


