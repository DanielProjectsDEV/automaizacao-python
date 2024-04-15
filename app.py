import pyautogui
from time import sleep

#Clicar e Digitar meu Usuario
pyautogui.click(966,540,duration=0.5)
pyautogui.write('daniel')

#Clicar e Digitar minha Senha
pyautogui.click(976,562,duration=0.5)
pyautogui.write('3341')

#Clicar em Entrar
pyautogui.click(874,598,duration=0.5)
#Extrair cada produto
with open('produtos.txt','r') as file:
    for linha in file:
        produto = linha.split(',')[0]
        quantidade = linha.split(',')[1]
        preco = linha.split(',')[2]

        #clical e digitar produto
        pyautogui.click(687,529,duration=0.5)
        pyautogui.write(produto)

        #clicar e digitar quantidade
        pyautogui.click(686,556,duration=0.5)
        pyautogui.write(quantidade)

        #clicar e digitar preço
        pyautogui.click(687,580,duration=0.5)
        pyautogui.write(preco)

        #clicar em registrar
        pyautogui.click(592,736,duration=0.5)
        sleep(1)
