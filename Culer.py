import os
from os import system
from time import sleep
import sys
import datetime
import requests
from colorama import Fore
system("clear")
os.system("")
class color:
    green = "\033[32m"
    red = "\033[31m"
    blue = "\033[36m"
    pink = "\033[35m"
    yellow = "\033[93m"
    darkblue = "\033[34m"
    white = "\033[00m"
    mark = '\x1b[38;5;4m'
    mark1 = '\x1b[48;5;15m'
    mark2 = '\x1b[0m'
n = 1
r = "="



sleep(3)
system("clear")
print("")
print("")
print("")
print("salam")
print("start")
bnr = (Fore.LIGHTGREEN_EX+f"""
      
            ⠀⢀⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠻⣥⠙⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡿⠀⡿⠻⣆⠙⠦⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⡄⠁⠀⠘⣆⡔⢶⣆⠉⢷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡄⠀⠀⡿⢿⡀⠉⠀⠞⠹⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡿⡄⠀⡇⠘⣧⣀⣀⣀⠀⠻⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⠃⠁⢀⣠⠞⣹⢿⠻⡟⢿⣿⣯⢳⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⠃⠶⠒⠉⠁⣴⠇⢸⡇⡟⡷⢬⡙⠎⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⠇⢀⣠⣄⡀⠚⠁⠀⠈⠀⠀⣷⠀⠉⠛⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼⣽⣿⣶⠋⢉⡿⠇⠀⠀⠀⠀⠀⣰⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢱⣿⣿⠇⠀⣠⣥⣤⡀⠀⠀⠀⢀⡟⣿⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⢿⣿⢀⣾⡟⠉⢹⡇⠀⠀⠀⢸⠁⡿⠙⣿⣷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⢸⣇⣾⡟⠀⠸⡏⣄⡀⠀⠀⢹⢀⡇⢀⢘⢿⣮⡙⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣇⠀⡀⣧⠰⣿⣶⣄⠀⠀⠀⠘⣎⠳⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡿⣿⣆⠹⣿⡐⣾⣷⣹⣆⠀⠀⠀⠘⢷⣄⣻⣿⣿⣷⡄⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⢿⣿⣦⠽⣇⣹⣟⢿⠙⠁⠀⠀⠀⣤⠉⠻⣿⣿⣿⣿⣦⡀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠙⡟⠂⣿⢹⡿⣼⠇⠀⠀⣀⠀⣷⡀⠀⠈⠻⣿⣿⣿⣷⡀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡆⢻⠀⠉⢸⡇⠈⣀⣠⣾⠇⠀⠻⣿⣦⣤⣴⣿⠿⣿⡿⣷⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡇⢸⡀⠀⢸⠁⣰⠛⣽⡧⠖⠻⢿⡆⠈⠉⠉⠀⠀⢻⣷⠹⠇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠘⡇⠀⢸⢰⡏⢰⡟⠀⣀⣀⡼⠃⠀⢀⡆⠀⠀⠘⣿⡆⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣴⣿⣶⣷⣶⣾⣿⣧⣾⣤⣄⣀⣀⣤⣤⣶⡿⠀⠀⠀⢠⣿⡇⠀
⠀⠀⠀⠀⠀⠀⠀⣠⣴⣾⣿⣟⡛⠛⠛⠉⠉⠉⠉⢉⣭⣽⡿⠿⠿⠿⠛⠛⠛⠓⠲⠦⠄⣼⢻⡇⠀
⠀⠀⠀⠀⠀⠀⠘⢉⣼⣿⣿⠿⠛⠛⠁⠀⠀⣠⠖⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⠁⣸⡇⠀
⠀⠀⠀⠀⠀⢀⣴⠿⠛⠁⢀⣀⣀⣀⣀⣀⣄⡀⠀⠀⠀⢦⣀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠇⣰⣿⠁⠀
⠀⠀⠀⢀⣴⣟⣥⣶⣾⣿⣿⣿⣿⣿⣿⣭⣤⣤⣤⣀⣀⡀⠈⠛⠶⢶⣶⣶⣶⣾⣿⣿⣿⠟⠁⠀⠀   ⠀⠀⠀⠀⠀
 ⠐⠋⠁⠀
 
 

""")
for i in bnr:
  sys.stdout.write(i)
  sys.stdout.flush()
  sleep(0.010)
print("")
bnr = (Fore.LIGHTGREEN_EX+f"""
im culer
Id rubika @Auth1_culer
This script is updated every 24 hours and new codes are added
""")
for i in bnr:
  sys.stdout.write(i)
  sys.stdout.flush()
  sleep(0.020)
code=input(f"""\033[36m
(1)mokharab
(2)dx
(3)hasas
(4)algoritm
(5)video porn hub
(6)logo
(7)server
(8)bag
(9)sex
(10)cod fil acc
Enter The Number>>>>>>""")
List1['http://3.5.7.9//shad.ir/.9.9.5.3.2.5.//f//h//y//n/3.5.7.4.8.4.6.8.9.0.0.9.7.4.2.2.5.6(yfttk15k)7.8.4.6.7.8.9.5.4.2.6.9','http://5.8.6.3/filter_account/b/9.8.4.2.1.5.4.6.2.9.5.7.4.8.1.2.2.1.6.7.1.8.9.2.6.1.7.3.6.7.9.3.8.8.3.4.5.5.6.2.9.1.6.1.6.7.4.2.9.1.6.4.2.6.8.9.5','http://Bug.spam.rubika/1000.900.800.700.600.500.400.300.200.100.90.80.70.60.50.40.30.20.10.9.8.7.6.5.4.3.2.1/https://malware.expert/malware/db-php/Z.Y.X.W.U.T.R.S.Q.P.O.N.L.K.J.I.H.G.F.E.D.C.B.A/xXx_http://spam.rubika.ir/yftt15k-0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0_@SupportBot']

if code=="1":print("\033[31m(https://cigarettes-chemical-rid-numeric.trycloudflare.com  ~  https://bit.li/3ild93L/php-hack  ~  https://bit.li/3ild93L  ~  https://raw.githubusercontent.com/Spam404/lists/master/main-blacklist.txt  ~  https://bit.ly/3fX8ljZ/fil.rubika  ~  http://ffmodmenu.page.link/Anti-V  ~  http://vxvault.net/URL_List.php  ~  https://v.3.0.9.yftt18k.in.xxx.com  ~  http://fil.sex.com/Distribution.immoral.content.com  ~  http://naturerleben-xhain.berlin/kieznaturkarte  ~  https://book.hacktricks.xyz  ~  http://zqktlwi4fecvo6ri.onion/wiki/index.php  ~  https://crash-bandicoot.info/enfejar/gambling-site  ~  https://dl.uploadgram.me/60bdffd3a2be4h  ~  https://cigarettes-chemical-rid-numeric.trycloudflare.com)")
if code=="2":print("\033[31mhttps://github.com/farnamryson/filtering-robika/issues/28--------------------http://dxprit-mehrab-sigari-28-hacker.phpnet.us---------------https://m.me11r.com/albums/338266/danni-rivers-gets-her-tight-pussy-drilled-in-various-positions/----------------https://github.com/aware18/mr-dxpirt-filtering.rubika.sex/blob/main/index.html")
if code=="3":print("\033[31mhttps://theintercept.com/2022/12/09/iran-regime-khamenei-death---------‐--https://xgore.net/category/bestgore/dead-female/--------------------https://l.zxvax.com/2132.html")
if code=="4":print(r.choice(Lest1))
if code=="5":print("\033[31mhttps://www.pornhub.com/view_video.php?viewkey=ph62541e492c3a7------------------https://www.pornhub.com/interstitial?viewkey=ph6203e4bf1b1d9")
if code=="6":print("\033[31mhttp://xa.fltvuq.cn/?account.Code=10749999999172-Shervi.Gazme.zan-hackers65.78766.infect.in.29*offs.ec/2Mcezwr")
if code=="7":print("\033[31mv.3.1.1.yftt15k.in")
if code=="8":print("\033[31mbug_AI = bug-9.9.9-support {<https://rubika.ir/SupportBot>} ip : 80.249.115.8 tcp {<https://rubika.ir/Netreport>} log account {<report-user.AI>} AI-report : Spam%100")
if code=="9":print("\033[31mhttps://imgurl.ir/uploads/s345712_--Rubika-photo-.jpg,,,,https://uploadkon.ir/uploads/55cd03_24InShot-۲۰۲۴۰۳۰۳-۲۱۴۶۳۳۶۰۷.jpg")
if code=="10":os.system("python Report.py")
    
