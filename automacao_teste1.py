import pyautogui as bot
import time 
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

# abrir chrome e acessar site app.tiflux
driver = webdriver.Chrome() 
driver.get('https://app.tiflux.com.br/users/sign_in')
# procurando elemento de entrada para email e senha, e enviando dados 
# id="sign_in_form_user_email"
time.sleep(1)
user = driver.find_element(By.ID, "login_email")
user.send_keys(Usuario)
time.sleep(1)
passw = driver.find_element(By.ID, "user_password")
passw.send_keys(Senha)
entrar = driver.find_element(By.NAME, "commit")
entrar.click()
