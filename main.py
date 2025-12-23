from services.whatsapp_service import iniciar_driver, aguardar_login, ler_mensagens
from services.excel_service import carregar_documentos_lidos, salvar_registros
from utils.parsers import parse_mensagem
from config.settings import ARQUIVO_EXCEL, DELAY_LEITURA
import time

def main():
    driver = iniciar_driver()
    aguardar_login(driver)

    documentos_lidos = carregar_documentos_lidos(ARQUIVO_EXCEL)
    novos_dados = []

    mensagens = ler_mensagens(driver)
    print(f"Mensagens encontradas: {len(mensagens)}")

    for msg in mensagens:
        texto = msg.text.strip()

        dados = parse_mensagem(texto)
        if not dados:
            continue

        if dados["Documento"] in documentos_lidos:
            continue

        novos_dados.append(dados)
        documentos_lidos.add(dados["Documento"])

        time.sleep(DELAY_LEITURA)

    total = salvar_registros(ARQUIVO_EXCEL, novos_dados)

    if total:
        print(f"{total} registros salvos com sucesso")
    else:
        print("Nenhum novo registro encontrado")

    driver.quit()

if __name__ == "__main__":
    main()
