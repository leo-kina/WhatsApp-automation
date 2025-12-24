import re

def parse_mensagem(texto: str):
    # valida se a mensagem comeca com o comando esperado ('/enviar')
    if not texto.lower().startswith("/enviar"):
        return None

    # remove o comando da mensagem
    texto = texto.replace("/enviar", "").strip()

    # extrai apenas numeros do texto
    numeros = re.sub(r"\D", "", texto)

    # identifica cpf pelo tamanho
    if len(numeros) == 11:
        return {
            "TipoDocumento": "CPF",
            "Documento": numeros
        }

    # identifica cnpj pelo tamanho
    if len(numeros) == 14:
        return {
            "TipoDocumento": "CNPJ",
            "Documento": numeros
        }

    # retorna none se nao for cpf nem cnpj
    return None
