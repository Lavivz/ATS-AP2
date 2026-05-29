from flask import Blueprint
from flask import jsonify
from flask import render_template

from app.database import SessionLocal
from app.models import Produto
from app.services import processar_pedido
from app.services import EstoqueInsuficiente

from app.payment_gateway import GatewayPagamento

bp = Blueprint("routes", __name__)

@bp.route("/")
def home():

    return render_template("index.html")

@bp.route("/produtos")
def produtos():

    db = SessionLocal()

    produtos = db.query(Produto).all()

    resultado = []

    for p in produtos:

        resultado.append({
            "id": p.id,
            "nome": p.nome,
            "preco": p.preco,
            "estoque": p.estoque
        })

    db.close()

    return jsonify(resultado)

@bp.route("/comprar/<int:produto_id>", methods=["POST"])
def comprar(produto_id):

    db = SessionLocal()

    gateway = GatewayPagamento()

    try:

        resultado = processar_pedido(
            produto_id,
            db,
            gateway
        )

        return jsonify(resultado), 200

    except EstoqueInsuficiente as e:

        return jsonify({
            "erro": str(e)
        }), 400

    except ValueError as e:

        return jsonify({
            "erro": str(e)
        }), 404

    finally:

        db.close()