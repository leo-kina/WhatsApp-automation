import re

def parse_mensagem(texto: str):

    numeros = re.sub(r"\D", "", texto)

    if len(numeros) == 11:
        return {
            "TipoDocumento": "CPF",
            "Documento": numeros
        }

    if len(numeros) == 14:
        return {
            "TipoDocumento": "CNPJ",
            "Documento": numeros
        }
    

    return None
