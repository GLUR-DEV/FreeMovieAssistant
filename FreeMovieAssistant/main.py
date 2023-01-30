import os
import pywinauto
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep

proxarr = []
proxarrresult = []

title = ""

def checkproxys():
    with open("proxies.txt") as file:
        line = file.read()
        line = line.splitlines()

        for ip in line:
            rawresponse = os.popen(f"ping {ip} ").read()
            response = rawresponse[-7]+rawresponse[-6]+rawresponse[-5]+rawresponse[-4]
            response = response.replace("= ", "")
            with open('proxiesresults.txt', 'a') as f:
                f.write(response + "\n")

    print("Proxy check has finished! Selecting fastest proxy...")
    compproxys()

def compproxys():

    file = open("proxiesresults.txt", "r")
    for x in file:
        proxarrresult.append(x)
    file.close()
    proxyspeed = min(proxarrresult)
    proxyspeedindex = proxarrresult.index(proxyspeed)

    file = open("proxies.txt", "r")
    for x in file:
        proxarr.append(x)
    file.close()
    fastestproxy = proxarr[proxyspeedindex]
    fastestproxy = fastestproxy.replace("\n", "")

    with open('config.txt', 'w') as f:
        f.write(fastestproxy + "\n")
        f.write(proxyspeed + "\n")

def getconfig():
    file = open("config.txt", "r")
    fastestproxy = file.readline().replace("\n", "")
    proxyspeed = file.readline().replace("\n", "")

    print("Fastest proxy found! Download speed optimized.\n")
    print("You are browsing on", fastestproxy + ".", "Ping:", proxyspeed)
    file.close()


print("Program made by GLUR. GLUR#4861 on discord")
print("If you downloaded this program from anywhere other than the my github(https://github.com/GLUR-DEV) then your computer may be at risk. If this is the case delete all traces of this program now!\n")

print("!!WARNING!!: DO NOT USE THIS PROGRAM WITHOUT A VPN. CONSEQUENCES MAY INCLUDE LARGE FINES.")
print("FREE VPN: protonvpn.com. IF YOU DO NOT HAVE A VPN TURNED ON DO NOT PROCEED")
print("Make sure free download manager(freedownloadmanager.org) is downloaded, opened and in full screen!\n")

input("!!BY PROCEEDING YOU AGREE THAT I DO NOT TAKE ANY LIABILITY FOR ANY FINES OR LEGAL PUNISHMENT THAT COMES FROM USING THIS PROGRAM!! (Press enter)")
print("")

bFileExists = os.path.exists("proxiesresults.txt")

if bFileExists == True:
    user = input("Proxies have already been checked! Do you want to recheck? (y/n): ")
    print("Please be patient this can take a minute...")
    if user == "y":
        os.remove("proxiesresults.txt")
        checkproxys()
else:
    print("Proxies haven't been checked! Checking proxies for optimized download speed.")
    print("Please be patient this can take a minute...")
    checkproxys()

getconfig()

title = input("Enter a movie you want to download: ")
print("")

options = Options()
options.add_argument("--window-size=800,800")
driver = webdriver.Chrome(options=options)

file = open("config.txt", "r")
fastestproxy = file.readline().replace("\n", "")
driver.get("https://" + fastestproxy +"/search/" + title + "/1/99/0/")
site = driver.current_window_handle
folder = driver.find_element(By.XPATH, "(//a)[21]")
folder.click()
folder = driver.find_element(By.XPATH, "//a[@title='Get this torrent']")
folder.click()
sleep(1)
pywinauto.mouse.click(button='left', coords=(187, 177))
pywinauto.mouse.click(button='left', coords=(486, 243))
sleep(3)
pywinauto.mouse.click(button='left', coords=(1171, 599))
driver.quit()
file.close()

print("Please wait for your movie to download!")
input("Press enter to close...")


