from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
from threading import Thread

from config.settings import URL_WHATSAPP, TEMPO_QR, TEMPO_ABRIR_GRUPO

parar_scroll = False

def iniciar_driver():
    driver = webdriver.Chrome()
    driver.get(URL_WHATSAPP)
    driver.maximize_window()
    return driver

def aguardar_login(driver):
    print("Escaneie o QR Code do WhatsApp Web")
    time.sleep(TEMPO_QR)

    print("Abra manualmente o grupo desejado")
    time.sleep(TEMPO_ABRIR_GRUPO)

def input_parar():
    global parar_scroll
    input("Pressione ENTER a qualquer momento para parar o scroll...\n")
    parar_scroll = True

def scroll_conversa(driver, max_tentativas=100, delay=0.5):

    global parar_scroll

    Thread(target=input_parar, daemon=True).start()

    chat_box = driver.find_element(By.XPATH, '//div[contains(@class, "copyable-area")]')
    actions = ActionChains(driver)

    for i in range(max_tentativas):
        if parar_scroll:
            print("Scroll interrompido pelo usuário.")
            break

        actions.move_to_element(chat_box).click().perform()
        actions.send_keys(u'\ue013').perform()  
        time.sleep(delay)

def ler_mensagens(driver):

    scroll_conversa(driver)  
    elementos = driver.find_elements(By.XPATH, '//div[@data-pre-plain-text]')
    return elementos
