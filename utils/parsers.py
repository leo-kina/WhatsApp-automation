import re

def parse_mensagem(texto: str):
    if not texto.lower().startswith("/enviar"):
        return None

    texto = texto.replace("/enviar", "").strip()

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
