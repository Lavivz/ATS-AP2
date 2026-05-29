from unittest.mock import Mock

from app.services import processar_pedido

def test_gateway_chamado(db_session):

    gateway = Mock()

    processar_pedido(
        1,
        db_session,
        gateway
    )

    gateway.processar.assert_called_once_with(5000)