import re

def parse_mesnagem(texto : str) -> dict | None:
    if not texto.startswith("/enviar"):
        return None

    doc = re.search(r"CPF\/CNPJ:\s*(.*)", texto, re.I)
    if not (doc):
        return None
    
    return {
        "Documento" : doc.group(1).strip(),
    }