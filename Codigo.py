import pyautogui
import time
import platform
import pandas

pyautogui.PAUSE = 0.5

tabela = pandas.read_csv("produtos.csv")

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

time.sleep(3)

if platform.node() == "DESKTOP-CMTBKDM":
    pyautogui.click(x=327, y=632)
#else : 

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

pyautogui.click(x=605, y=373)
time.sleep(2)
pyautogui.write("teste@teste.com.br")
time.sleep(2)
pyautogui.press("tab")
pyautogui.write("123")
pyautogui.press("enter")

for linha in tabela.index:
    pyautogui.click(x=501, y=256)

    pyautogui.write(tabela.loc[linha,"codigo"])
    pyautogui.press("tab")

    pyautogui.write(tabela.loc[linha,"marca"])
    pyautogui.press("tab")

    pyautogui.write(tabela.loc[linha,"tipo"])
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha,"categoria"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha,"preco_unitario"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha,"custo"]))
    pyautogui.press("tab")

    if str(tabela.loc[linha,"obs"]) != "nan":
        pyautogui.write(tabela.loc[linha,"obs"])
    pyautogui.press("tab")
    
    pyautogui.press("enter")

    pyautogui.scroll(100000)
