import pyautogui as bot

# alerta ao começar a rodar o codigo
bot.alert('O relatório vai começar a ser gerado! Não mexa no computador até o bot lindo finalizar.')
# tempo de pausa pro pc executar tudo de boa 
bot.PAUSE = 0.5
# abrir chrome 
bot.press('winleft')
bot.write('chrome')
bot.press('enter')
# acessar site app.tiflux 
# fazer login com email e senha 
