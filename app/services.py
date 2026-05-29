from app.models import Produto

class EstoqueInsuficiente(Exception):
    pass

def processar_pedido(produto_id, db, gateway):

    produto = db.get(Produto, produto_id)

    if not produto:
        raise ValueError("Produto não encontrado")

    if produto.estoque <= 0:
        raise EstoqueInsuficiente("Produto sem estoque")

    gateway.processar(produto.preco)

    produto.estoque -= 1

    db.commit()

    return {
        "mensagem": "Compra realizada com sucesso"
    }