class GatewayPagamento:

    def processar(self, valor):

        return {
            "status": "pago",
            "valor": valor
        }
