import tkinter
from tkinter import *
import http.client
import json
import os
import ctypes


def connect():
    print("e")

    uName = T.get()
    uPass = T1.get()

    print(uName)
    print(uPass)

    os.remove("C:/Users/Public/uName.txt")
    os.remove("C:/Users/Public/uPass.txt")

    with open('C:/Users/Public/uName.txt', 'w') as f:
        f.write(T.get())
    with open('C:/Users/Public/uPass.txt', 'w') as f:
        f.write(T1.get())

    with open('C:/Users/Public/uName.txt', encoding="utf-8") as f:
        username = f.read()
    with open('C:/Users/Public/uPass.txt', encoding="utf-8") as f:
        password = f.read()


    conn = http.client.HTTPSConnection("api.ecoledirecte.com")
    payload = 'data={"identifiant":' + f'"{username}"' + ',"motdepasse":' + f'"{password}"' + '}'

    headers = {
        'authority': 'api.ecoledirecte.com',
        'accept': 'application/json, text/plain, */*',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
        'content-type': 'application/x-www-form-urlencoded',
        'sec-gpc': '1',
        'origin': 'https://www.ecoledirecte.com',
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://www.ecoledirecte.com/',
        'accept-language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7'
    }

    conn.request("POST", "/v3/login.awp", payload, headers)
    res = conn.getresponse()
    data = res.read()
    error = json.loads(data.decode("utf-8"))['code']
    if error == 505:
        InvalidPassOrUn = ctypes.windll.user32.MessageBoxW
        InvalidPassOrUn(None, 'Votre nom d utilisateur ou votre not de passe est invalide.', 'Erreur', 0)


window = Tk()

window.title("EcoleDirecte - Client")
window.iconbitmap('assets/logo.ico')
window.geometry("900x600")
window.resizable(False, False)
bg = PhotoImage(file="assets/bg.png")
label1 = Label(window, image=bg)
label1.place(x=0, y=0)

T = tkinter.Entry(window)
T.place(rely=0.35, relx=0.59, anchor='center', height=65)
T.configure(font=("Calibri", 12, "bold"))

T1 = tkinter.Entry(window)
T1.place(rely=0.50, relx=0.59, anchor='center', height=65)
T1.configure(font=("Calibri", 12, "bold"))

exit_button = Button(window, width=10, text='- - - - - - - -Se Connecter- - - - - - - -', command=lambda: connect())
exit_button.place(relx=0.43, rely=0.6, height=40, width=300)

window.mainloop()
