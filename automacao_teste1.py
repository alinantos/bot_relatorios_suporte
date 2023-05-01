import pyautogui as bot
import time 
from selenium import webdriver as driver 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

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
nav = driver.Chrome() 
nav.get('https://app.tiflux.com.br/v/users/sign_in')
# fazer login com email e senha 
driver.find_element(By.NAME, "user[email]").send_keys(Usuario)
driver.find_element(By.NAME, "user[password]").send_keys(Senha)
entrar = driver.find_element(By.NAME, "commit")
entrar.click()
