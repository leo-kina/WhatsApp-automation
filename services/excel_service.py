import pandas as pd
import os

def carregar_documentos_lidos(caminho):
    if not os.path.exists(caminho):
        return set()

    df = pd.read_excel(caminho)

    if "Documento" not in df.columns:
        return set()

    return set(df["Documento"].astype(str))


def salvar_registros(caminho, novos_dados):

    if not novos_dados:
        return 0

    df_novo = pd.DataFrame(novos_dados)

    if os.path.exists(caminho):
        df_existente = pd.read_excel(caminho)

        df_final = pd.concat([df_existente, df_novo], ignore_index=True)
        df_final = df_final.drop_duplicates(subset=["Documento"])
    else:
        df_final = df_novo

    df_final.to_excel(caminho, index=False)
    return len(df_novo)
