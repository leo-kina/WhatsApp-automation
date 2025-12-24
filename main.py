from services.whatsapp_service import iniciar_driver, aguardar_login, ler_mensagens
from services.excel_service import carregar_documentos_lidos, salvar_registros
from utils.parsers import parse_mensagem
from config.settings import ARQUIVO_EXCEL, DELAY_LEITURA
import time

def main():
    #inicia o navegador e abre o zap web
    driver = iniciar_driver()

    try:
    #aguarda login e abertura do grupo
        aguardar_login(driver)

    #carrega documentos salvos no Excel (evita duplicacao)
        documentos_lidos = carregar_documentos_lidos(ARQUIVO_EXCEL)

    #lista para armazenar novos registros
        novos_dados = []

    #le todas as mensagens visiveis do chat
        mensagens = ler_mensagens(driver)
        print(f"Mensagens encontradas: {len(mensagens)}")

        # processa mensagem por mensagem
        for msg in mensagens:
            texto = msg.text.strip()

            # ignora mensagens vazias
            if not texto:
                continue

            # tenta extrair dados da mensagem
            dados = parse_mensagem(texto)

            #ignora mensagens fora do padrao
            if not dados:
                continue

            documento = dados["Documento"]

            #ignora documentos ja processados
            if documento in documentos_lidos:
                continue

            #salva novo registro
            novos_dados.append(dados)
            documentos_lidos.add(documento)

            #pausa para evitar leitura rapida demais
            time.sleep(DELAY_LEITURA)

        #salva os novos registros no Excel
        total = salvar_registros(ARQUIVO_EXCEL, novos_dados)

        if total:
            print(f"{total} registros salvos com sucesso")
        else:
            print("Nenhum novo registro encontrado")

    finally:
        # garante que o navegador sera fechado
        driver.quit()
