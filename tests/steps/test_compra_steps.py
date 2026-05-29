from pytest_bdd import scenarios
from pytest_bdd import given
from pytest_bdd import when
from pytest_bdd import then

from unittest.mock import Mock

from app.services import processar_pedido

scenarios("../features/compra_sucesso.feature")

@given(
    "que existe um produto com estoque",
    target_fixture="produto"
)
def produto():
    return 1

@when(
    "o cliente realiza a compra",
    target_fixture="realizar_compra"
)
def realizar_compra(produto, db_session):

    gateway = Mock()

    return processar_pedido(
        produto,
        db_session,
        gateway
    )

@then("a compra deve ser concluída com sucesso")
def validar(realizar_compra):

    assert realizar_compra["mensagem"] == \
        "Compra realizada com sucesso"