Feature: Compra de produto

Scenario: Compra realizada com sucesso

    Given que existe um produto com estoque
    When o cliente realiza a compra
    Then a compra deve ser concluída com sucesso
