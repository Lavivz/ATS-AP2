import os
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database import Base
from app.models import Produto

TEST_DB = "sqlite:///test.db"

@pytest.fixture(scope="function")
def db_session():

    os.environ["DATABASE_URL"] = TEST_DB

    engine = create_engine(
        TEST_DB,
        connect_args={"check_same_thread": False}
    )

    TestingSessionLocal = sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=engine
    )

    Base.metadata.create_all(bind=engine)

    session = TestingSessionLocal()

    produto = Produto(
        nome="Notebook Gamer",
        preco=5000,
        estoque=10
    )

    session.add(produto)

    session.commit()

    yield session

    session.close()

    Base.metadata.drop_all(bind=engine)

    if os.path.exists("test.db"):
        os.remove("test.db")