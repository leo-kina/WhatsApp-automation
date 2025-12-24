from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from threading import Thread
import time

from config.settings import URL_WHATSAPP, TEMPO_QR, TEMPO_ABRIR_GRUPO

# controla a parada manual do scroll
parar_scroll = False


def iniciar_driver():
    # inicia o navegador e abre o whatsapp web
    driver = webdriver.Chrome()
    driver.get(URL_WHATSAPP)
    driver.maximize_window()
    return driver


def aguardar_login(driver):
    # aguarda o tempo para escanear o qr code
    print("escaneie o qr code do whatsapp web")
    time.sleep(TEMPO_QR)

    # aguarda abertura manual do grupo
    print("abra manualmente o grupo desejado")
    time.sleep(TEMPO_ABRIR_GRUPO)


def input_parar():
    # escuta o enter do usuario para parar o scroll
    global parar_scroll
    input("pressione enter a qualquer momento para parar o scroll...\n")
    parar_scroll = True


def scroll_conversa(driver, max_tentativas=100, delay=0.5):
    # realiza o scroll para cima na conversa
    global parar_scroll
    parar_scroll = False

    # thread para capturar input sem travar o programa
    Thread(target=input_parar, daemon=True).start()

    chat_box = driver.find_element(
        By.XPATH,
        '//div[contains(@class, "copyable-area")]'
    )

    actions = ActionChains(driver)

    for _ in range(max_tentativas):
        # interrompe o scroll se o usuario solicitar
        if parar_scroll:
            print("scroll interrompido pelo usuario")
            break

        # foca no chat e envia a tecla page up
        actions.move_to_element(chat_box).click().perform()
        actions.send_keys(u'\ue013').perform()
        time.sleep(delay)


def ler_mensagens(driver):
    # garante que todas as mensagens sejam carregadas
    scroll_conversa(driver)

    # captura os elementos de mensagem do chat
    elementos = driver.find_elements(
        By.XPATH,
        '//div[@data-pre-plain-text]'
    )

    return elementos
