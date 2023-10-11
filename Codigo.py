# Entrar no link
    #https://dlp.hashtagtreinamentos.com/python/intensivao/login
    #  Chrome 



import pyautogui
import time
import pandas



# pyautogui.click clicar com mause
# pyautogui.write escrever
# pyautogui.press apertar
# pyautogui.hotkey Combinação de teclas 

pyautogui.PAUSE = 0.5


pyautogui.press ("win")
pyautogui.write ( " Chrome " )
pyautogui.press ("enter")

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press ("enter")

time.sleep (3) 

pyautogui.click(x=607, y=563)
pyautogui.write ("joao.otaviobarros@hotmail.com")
pyautogui.press ("tab")
pyautogui.write ("Celta")   
pyautogui.press("tab")
pyautogui.press ("enter")

time.sleep (4)

tabela = pandas.read_csv( "produtos.csv.csv" )
print(tabela)


for linha in tabela.index:

    pyautogui.click(x=689, y=384)
 
    codigo = tabela.loc [linha, "codigo"]

    pyautogui.write (str (codigo))
    pyautogui.press ("tab")
    pyautogui.write (str (tabela.loc [linha,"marca"]))
    pyautogui.press ("tab")
    pyautogui.write (str (tabela.loc [linha,"tipo"]))
    pyautogui.press ("tab")
    pyautogui.write (str (tabela.loc [linha,"categoria"]) )
    pyautogui.press ("tab")
    pyautogui.write (str (tabela.loc [linha,"preco_unitario"]))
    pyautogui.press ("tab")
    pyautogui.write (str (tabela.loc [linha,"custo"]))
    pyautogui.press ("tab")
    
    obs= tabela.loc [linha, "obs"]
    if not pandas.isna(obs):
        
        pyautogui.write (str (tabela.loc [linha, "obs"]))
    pyautogui.press ("tab")
    pyautogui.press ("enter")


    pyautogui.scroll (10000)

 