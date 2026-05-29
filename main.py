from flask import Flask

from app.database import Base
from app.database import engine
from app.database import SessionLocal

from app.models import Produto

from app.routes import bp

app = Flask(__name__)

app.register_blueprint(bp)

Base.metadata.create_all(bind=engine)

def popular_banco():

    db = SessionLocal()

    if not db.query(Produto).first():

        produtos = [

            Produto(
                nome="Notebook Gamer",
                preco=5000,
                estoque=20
            ),

            Produto(
                nome="Mouse Gamer",
                preco=250,
                estoque=12
            ),

            Produto(
                nome="Teclado Mecânico",
                preco=450,
                estoque=9
            )

        ]

        db.add_all(produtos)

        db.commit()

    db.close()

popular_banco()

if __name__ == "__main__":
    app.run(debug=True)