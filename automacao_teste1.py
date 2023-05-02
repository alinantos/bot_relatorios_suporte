import pyautogui as bot
import time
import datetime
import PySimpleGUI as sg
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# abrindo arquivos com usuario e senha pra login, e fazendo a leitura
file1 = open("user.txt", "r")
file2 = open("senha.txt", "r")
Usuario = file1.read()
Senha = file2.read()

# alerta ao começar a rodar o codigo
bot.alert('O relatório vai começar a ser gerado! Não mexa no computador até o bot lindo finalizar.')
# tempo de pausa pro pc executar tudo de boa
bot.PAUSE = 0.5

# definindo a data
data = datetime.datetime.now()
# corrigindo a data pra que fique sempre no formato 00/00/0000
if data.month < 10 and data.day < 10:
    dataHoje = ("0" + str(data.day) + "/0" +
                str(data.month) + "/" + str(data.year))
elif data.month >= 10 and data.day < 10:
    dataHoje = ("0" + str(data.day) + "/" +
                str(data.month) + "/" + str(data.year))
elif data.month < 10 and data.day >= 10:
    dataHoje = (str(data.day) + "/0" + str(data.month) + "/" + str(data.year))
else:
    dataHoje = (str(data.day) + str(data.month) + "/" + str(data.year))

# correção de erro ao executar selenium
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(service=Service(
    executable_path=r'./chromedriver.exe'), options=options)
# abrir chrome e acessar site app.tiflux
driver.get('https://app.tiflux.com.br/v/')

# procurando elementos de entrada para email e senha, e enviando dados
time.sleep(1)
user = driver.find_element(By.CSS_SELECTOR, "#sign_in_form_user_email")
user.send_keys(Usuario)
time.sleep(1)
passw = driver.find_element(By.CSS_SELECTOR, "#sign_in_form_user_password")
passw.send_keys(Senha)
entrar = driver.find_element(
    By.XPATH, "//*[@id='sign_in_form']/div[4]/div/div/div/button")
entrar.click()

# acessando o menu de relatórios


def relatorio(Data, driver):
    time.sleep(1)
    botaoRel = driver.find_element(By.XPATH, "/html/body/div[1]/section/aside/div[1]/div[3]/ul/li[6]")
    botaoRel.click()
    time.sleep(2)
    grafApont = driver.find_element(By.XPATH, "/html/body/div[1]/section/section/main/div/div/div[2]/div/div[1]/div/div[2]/div/div[6]/a")
    grafApont.click()

    # inserindo data selecionada pra gerar relatório
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "#date").clear()
    driver.find_element(By.CSS_SELECTOR, "#date").send_keys(Data)
    time.sleep(1)


# voltando pra tela inicial
def telaIni(driver):
    Tflux = driver.find_element(
        By.XPATH, '/html/body/div[1]/section/aside/div[1]/div[1]')
    Tflux.click()


# ----------------------- interface antiga ------------------------------------#
sg.theme('Topanga')

layout = [
    [sg.Text("Relatório Tiflux"), sg.Input(
        "dd/mm/aaaa", key="Data", size=(20, 1))],
    [sg.Button('Relatório hoje')],
    [sg.Text("")],
    [sg.Text(key="Erro")],
    [sg.Text(key="Pronto")],
    [sg.Button('Quit'), sg.Button("Começar")]
]

# Create the window
window = sg.Window('Relatório Netcontroll', layout)

# Display and interact with the Window using an Event Loop
while True:
    event, values = window.read()
    window['Erro'].update('')
    window['Pronto'].update('')
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        driver.quit()
        break

    elif event == 'Começar':
        if values['Data'] == "dd/mm/aaaa" or values['Data'] == '' or values['Data'] == ' ':
            window['Erro'].update(
                'Preencha a data primeiro', text_color="yellow")
            continue
        Data = str(values['Data'])
        relatorio(Data, driver)
        time.sleep(1)
        telaIni(driver)

    elif event == 'Relatório hoje':
        if values['Data'] != "dd/mm/aaaa":
            window['Erro'].update(
                'Feito o relatório da data especificada', text_color="yellow")
            Data = str(values['Data'])
            relatorio(Data, driver)
            time.sleep(1)
            telaIni(driver)
        else:
            relatorio(dataHoje, driver)
            time.sleep(1)
            telaIni(driver)

    window['Pronto'].update('Pronto', text_color="yellow")
# Finish up by removing from the screen
window.close()
