import pytest

from unittest.mock import Mock

from app.services import processar_pedido
from app.services import EstoqueInsuficiente

from app.models import Produto

def test_compra_com_sucesso(db_session):

    gateway = Mock()

    resultado = processar_pedido(
        1,
        db_session,
        gateway
    )

    assert resultado["mensagem"] == \
        "Compra realizada com sucesso"

    gateway.processar.assert_called_once()

def test_produto_inexistente(db_session):

    gateway = Mock()

    with pytest.raises(ValueError):

        processar_pedido(
            999,
            db_session,
            gateway
        )

def test_sem_estoque(db_session):

    produto = db_session.get(Produto, 1)

    produto.estoque = 0

    db_session.commit()

    gateway = Mock()

    with pytest.raises(EstoqueInsuficiente):

        processar_pedido(
            1,
            db_session,
            gateway
        )