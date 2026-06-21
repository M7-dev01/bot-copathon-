#cd .vscode
#C:/Users/Home/.local/bin/python3.14.exe bot.py
#"!loja",
 #   "classic",
 #   "peepoRiot",
#    "Sadge",
  #  "modCheck",
  #  "EZ",
  #  "duckPls",
  #  "emojiBubbly",
   # "emojiCheerful",
  #  "emojiAngel",
   # "jonvlogsEtVlogs",
   # "!points"
import pyautogui
import pyperclip
import time
import random

mensagens = [
    "KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK"
]

intervalo = 5

print("5 segundos pra clicar no chat...")
time.sleep(5)

i = 0
while True:
    mensagem = mensagens[i % len(mensagens)]
    pyperclip.copy(mensagem)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')
    espera = intervalo + random.randint(-5, 5)
    print(f"Mensagem enviada: {mensagem} | Próxima em {espera}s...")
    i += 1
    time.sleep(espera)
