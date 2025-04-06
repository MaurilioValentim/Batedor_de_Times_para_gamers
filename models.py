# Local do banco de dados

from sqlmodel import SQLModel, Field, create_engine, Relationship
from enum import Enum
from datetime import date
from typing import Optional, List


class Conta(SQLModel, table=True):
    id: int = Field(primary_key=True)
    nome_real: Optional[str] = None
    nick: str
    hashtag: str

    # Relacionamentos
    rank: Optional["Rank"] = Relationship(back_populates="conta")
    historicos: List["Historico"] = Relationship(back_populates="conta")


class Rank(SQLModel, table=True):
    id: int = Field(primary_key=True)
    conta_id: int = Field(foreign_key="conta.id")
    rank_do_lol: str
    rank_local: str
    pontuacao: float

    conta: Optional[Conta] = Relationship(back_populates="rank")


class Partida(SQLModel, table=True):
    id: int = Field(primary_key=True)
    time_1: str
    time_2: str
    time_vencedor: str
    data: date
    bans_time_1: str
    bans_time_2: str

    historicos: List["Historico"] = Relationship(back_populates="partida")


class Historico(SQLModel, table=True):
    id: int = Field(primary_key=True)
    conta_id: int = Field(foreign_key="conta.id")
    partida_id: int = Field(foreign_key="partida.id")
    kda: str
    campeao: str

    conta: Optional[Conta] = Relationship(back_populates="historicos")
    partida: Optional[Partida] = Relationship(back_populates="historicos")


sqlite_file_name = 'database.db'
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo = False)

# if __name__ == "__main__":
#      SQLModel.metadata.create_all(engine)