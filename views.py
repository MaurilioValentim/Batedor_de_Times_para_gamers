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
                print(f"Erro: nome_real '{conta.nome_real}' já está cadastrado.")
                return f"Erro: nome_real '{conta.nome_real}' já está cadastrado."

        # Verifica se nick + hashtag já existem juntos
        nick_hashtag_existente = session.exec(
            select(Conta).where(
                Conta.nick == conta.nick,
                Conta.hashtag == conta.hashtag
            )
        ).first()
        if nick_hashtag_existente:
            print(f"Erro: a combinação nick '{conta.nick}' e hashtag '{conta.hashtag}' já existe.")
            return f"Erro: a combinação nick '{conta.nick}' e hashtag '{conta.hashtag}' já existe."

        # Se passou pelas verificações, salva a conta
        session.add(conta)
        session.commit()

        print(f"Conta criada com sucesso! ID: {conta.id}")
        return 


# # Funcao para atualizar o rank da pessoa
# def atualizar_rank(rank = Rank):   # Entradas rank_do_lol,   rank_local, pontuacao
#     with Session(engine) as session:    
