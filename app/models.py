from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from app.database import Base

class Produto(Base):

    __tablename__ = "produtos"

    id = Column(Integer, primary_key=True)

    nome = Column(String, nullable=False)

    preco = Column(Integer, nullable=False)

    estoque = Column(Integer, nullable=False)