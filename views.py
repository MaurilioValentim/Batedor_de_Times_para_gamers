from models import Conta, Rank, Partida, Historico, engine
from sqlmodel import Session, select
from datetime import date

from models import Conta, Rank, Partida, Historico, engine
from sqlmodel import Session, select
from datetime import date

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



# # Funcao para atualizar o rank da pessoa
# def atualizar_rank(rank = Rank):   # Entradas rank_do_lol,   rank_local, pontuacao
#     with Session(engine) as session:    