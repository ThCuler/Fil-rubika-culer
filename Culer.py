import os
from os import system
from time import sleep
import sys
import datetime
import requests
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
print(f"""\033[34m
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
code=input(f"""
(1)mokharab
(2)dx
(3)hasas
(4)algoritm
(5)video porn hub
(6)logo
(7)server
(8)bag
(9)sex


Enter The Number>>>>>>""")
if code=="1":print("(https://cigarettes-chemical-rid-numeric.trycloudflare.com  ~  https://bit.li/3ild93L/php-hack  ~  https://bit.li/3ild93L  ~  https://raw.githubusercontent.com/Spam404/lists/master/main-blacklist.txt  ~  https://bit.ly/3fX8ljZ/fil.rubika  ~  http://ffmodmenu.page.link/Anti-V  ~  http://vxvault.net/URL_List.php  ~  https://v.3.0.9.yftt18k.in.xxx.com  ~  http://fil.sex.com/Distribution.immoral.content.com  ~  http://naturerleben-xhain.berlin/kieznaturkarte  ~  https://book.hacktricks.xyz  ~  http://zqktlwi4fecvo6ri.onion/wiki/index.php  ~  https://crash-bandicoot.info/enfejar/gambling-site  ~  https://dl.uploadgram.me/60bdffd3a2be4h  ~  https://cigarettes-chemical-rid-numeric.trycloudflare.com)")
if code=="2":print("https://github.com/farnamryson/filtering-robika/issues/28--------------------http://dxprit-mehrab-sigari-28-hacker.phpnet.us---------------https://m.me11r.com/albums/338266/danni-rivers-gets-her-tight-pussy-drilled-in-various-positions/----------------https://github.com/aware18/mr-dxpirt-filtering.rubika.sex/blob/main/index.html")
if code=="3":print("https://theintercept.com/2022/12/09/iran-regime-khamenei-death---------‐--https://xgore.net/category/bestgore/dead-female/--------------------https://l.zxvax.com/2132.html")
if code=="4":print("https://photo.sex.com/5.3.8.4/g/y///v//w/s//5.2.4.7.2.8.6.2.7.9.3.7.1.5.7.3.7.8.1.6.3.6.2.8.2com")
if code=="5":print("https://www.pornhub.com/view_video.php?viewkey=ph62541e492c3a7------------------https://www.pornhub.com/interstitial?viewkey=ph6203e4bf1b1d9")
if code=="6":print("http://xa.fltvuq.cn/?account.Code=10749999999172-Shervi.Gazme.zan-hackers65.78766.infect.in.29*offs.ec/2Mcezwr")
if code=="7":print("v.3.1.1.yftt15k.in")
if code=="8":print("bug_AI = bug-9.9.9-support {<https://rubika.ir/SupportBot>} ip : 80.249.115.8 tcp {<https://rubika.ir/Netreport>} log account {<report-user.AI>} AI-report : Spam%100")
if code=="9":print("https://imgurl.ir/uploads/s345712_--Rubika-photo-.jpg,,,,https://uploadkon.ir/uploads/55cd03_24InShot-۲۰۲۴۰۳۰۳-۲۱۴۶۳۳۶۰۷.jpg")
