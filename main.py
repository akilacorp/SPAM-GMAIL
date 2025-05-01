import random
import string
from colorama import *
import smtplib
import os
import time
import sys

init(autoreset=True)

def typewriter(texto, delay=0.0001):
    for char in texto:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def input_typewriter(prompt, delay=0.001):
    for char in prompt:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    return input(Fore.GREEN)

tag = """ [==================================================-byBROOONKS======================================================] 
"""

logo = Fore.GREEN + """ 


░██████╗██████╗░░█████╗░███╗░░░███╗  ░█████╗░███████╗░██████╗░█████╗░░█████╗░██████╗░██████╗░
██╔════╝██╔══██╗██╔══██╗████╗░████║  ██╔══██╗██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗
╚█████╗░██████╔╝███████║██╔████╔██║  ███████║█████╗░░╚█████╗░██║░░╚═╝██║░░██║██████╔╝██████╔╝
░╚═══██╗██╔═══╝░██╔══██║██║╚██╔╝██║  ██╔══██║██╔══╝░░░╚═══██╗██║░░██╗██║░░██║██╔══██╗██╔═══╝░
██████╔╝██║░░░░░██║░░██║██║░╚═╝░██║  ██║░░██║███████╗██████╔╝╚█████╔╝╚█████╔╝██║░░██║██║░░░░░
╚═════╝░╚═╝░░░░░╚═╝░░╚═╝╚═╝░░░░░╚═╝  ╚═╝░░╚═╝╚══════╝╚═════╝░░╚════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░░░░
[==================================================-byAESCORP======================================================]
"""

email = input_typewriter(logo + "Digite seu email :\n[==> ")
os.system("cls")

vers = input_typewriter(tag + "Digite o email da vítima :\n[==> ")
os.system("cls")

subject = input_typewriter(tag + "Digite o assunto do email :\n[==> ")
os.system("cls")

message = input_typewriter(tag +"Digite sua mensagem :\n[==> ")
os.system("cls")

nombre = int(input_typewriter(tag +"Digite o número de emails que deseja enviar :\n[==> "))
os.system("cls")

text = f"Subject: {subject}\n\n{message}"

token = input_typewriter(tag + "Digite sua senha de aplicativo :\nPara ajuda :  https://support.google.com/mail/answer/185833?hl \n[==> ")

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

for i in range(nombre):
    server.login(email, token)
    server.sendmail(email, vers, text)

typewriter(tag + f"Email foi enviado para {vers}")
os.system("cls")
