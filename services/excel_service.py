import pandas as pd
import os


def carregar_documentos_lidos(caminho):
    # verifica se o arquivo existe
    if not os.path.exists(caminho):
        return set()

    # le o arquivo excel
    df = pd.read_excel(caminho)

    # valida se a coluna documento existe
    if "Documento" not in df.columns:
        return set()

    # retorna os documentos como set de strings
    return set(df["Documento"].astype(str))


def salvar_registros(caminho, novos_dados):
    # nao faz nada se nao houver novos dados
    if not novos_dados:
        return 0

    # cria dataframe com os novos registros
    df_novo = pd.DataFrame(novos_dados)

    # verifica se o arquivo ja existe
    if os.path.exists(caminho):
        # le dados existentes
        df_existente = pd.read_excel(caminho)

        # junta dados antigos com os novos
        df_final = pd.concat(
            [df_existente, df_novo],
            ignore_index=True
        )

        # remove documentos duplicados
        df_final = df_final.drop_duplicates(
            subset=["Documento"]
        )
    else:
        # cria novo arquivo se nao existir
        df_final = df_novo

    # salva o resultado final no excel
    df_final.to_excel(caminho, index=False)

    # retorna quantidade de novos registros
    return len(df_novo)
