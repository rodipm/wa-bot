import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.firefox.options import Options
import random
from PIL import Image
import requests

# options = webdriver.ChromeOptions()
# options.add_argument("headless")
# options.add_argument("--user-data-dir=C:\\Users\\Rodrigo\\AppData\\Local\\Google\\Chrome\\Selenium Data\\")
# driver = webdriver.Chrome('D:\\chromedriver.exe', chrome_options=options)

options = Options()
options.add_argument("--headless")
driver = webdriver.Firefox(options=options, executable_path="D:\\geckodriver.exe")

# driver.minimize_window()
driver.get('https://web.whatsapp.com/')

lastLength = 0

# perolas = ["CANNON REAVES - Guri, IKIDA. 2019", "- Yuri, o que significa O.V.N.I? - Extraterrestre. Guri, IKIDA. 2019", "Lógico que existe cobra herbívora, tem cobra que come inseto... - Guguri, Ikida. 2019", "Cow Marx - Ikida, GURI. 2019", "- Yuri, o nazismo era de Direita ou de Esquerda? - Nem um nem outro. Posso estar equivocado, mas nazismo é fascismo. - IKIDA, Guri. 2019", "Alemões - IKIDA, Guri", "Urangotango - IKIDA, Guri. 2018", "borro de café - IKIDA, Guri. 2018", "Nossa, eu vou morrer de fatiga... IKIDA, Guri. 2018", "Terezinha é um lugar muito quente né? Terezinha que fala? - IKIDA, Guri", "Dava pra salvar a cidade com a quantidade de couro de jacaré que sai desse bicho - IKIDA, Guri. 2018", "É o crânio de um crocodilo que é mais resistente que diamante? - IKIDA, Guguri. 2018", "Os cara do ISIS nao sao nem louco de fazer um atestado na Rússia - IKIDA, Guri. 2018"]


def waitForAuth():
    print("[wa-bot] Waiting for Auth...")
    while True:
        try:
            driver.find_element_by_class_name('_3RWII')
            print("[wa-bot] Auth Completed. Waiting for chat...")
            # driver.minimize_window()
            break
        except:
            time.sleep(.5)

def waitForChat():
    while True:
        try:
            driver.find_element_by_class_name('_3u328.copyable-text.selectable-text')
            print("[wa-bot] Chat Loaded.")
            break
        except:
            time.sleep(.5)

def waitForQR():
    print("[wa-bot] Waiting For QR Code...")
    while True:
        try:
            driver.find_element_by_class_name('_1pw2F')
            time.sleep(.3)
            driver.find_element_by_class_name('_1pw2F').screenshot('qr.png')
            img = Image.open('qr.png')
            img.show()
            print("[wa-bot] QR Code Received, Scan the Image Displaying on Screen...")
            waitForAuth()
            img.close()
            break
        except:
            time.sleep(.7)

def chooseChat(number=0, chat=None):
    global lastLength
    while True:
        try:
            if chat == None:
                chat = driver.find_elements_by_class_name('X7YrQ')[number]
            actions = ActionChains(driver)
            actions.click(chat).perform()
            lastLength = 0
            print("[wa-bot] Chat Selected.")
            break
        except:
            pass
        time.sleep(.5)

def SendMessage(message):
    messageBox = driver.find_element_by_class_name('_3u328.copyable-text.selectable-text')
    messageBox.send_keys(message)
    messageBox.send_keys(Keys.RETURN)
    print("[wa-bot] Message Sent.")

def checkOtherChatMessages():
    print("[wa-bot] Checking for Messages on Other Chats.")
    chats = driver.find_elements_by_class_name('X7YrQ')

    for chat in chats:
        try:
            chat.find_element_by_class_name('_1ZMSM')
            name = chat.find_element_by_class_name('_19RFN').get_attribute('title')
            print("[wa-bot] New Messages Detected on {}'s Chat...".format(name))
            chooseChat(chat=chat)
        except:
            pass

def processMessage(message):
    if message == "!ikida":
        r = requests.get('https://ikida-api.mybluemix.net/perolas')
        perolas = r.json()
        pMessage = random.choice(perolas)
        SendMessage(pMessage)
    
    elif message == "!borbanews":
        r = requests.get('https://ikida-api.mybluemix.net/borba_news')
        news = r.json()
        pMessage = random.choice(news)
        SendMessage(pMessage)

def checkCurrentChatMessages(cb, echo=False):
    print("[wa-bot] Checking for Messages on Current Chat...")

    global lastLength

    if lastLength == 0:
        lastLength = len(driver.find_elements_by_class_name('selectable-text.invisible-space.copyable-text'))
    for _ in range(10):
        messages = driver.find_elements_by_class_name('selectable-text.invisible-space.copyable-text')
        currentLength = len(messages)
        if currentLength < lastLength:
            lastLength = currentLength

        if currentLength > lastLength:
            message = messages[currentLength-1].get_attribute('innerHTML')
            print("[wa-bot] New Message Detected on current chat: {}".format(message))
            lastLength = currentLength
            if echo:
                lastLength += 1
            cb(message)
            print("[wa-bot] Executed Callback...")
        time.sleep(.5)

if __name__ == "__main__":
    waitForQR()
    chooseChat()
    waitForChat()
    driver.save_screenshot('chat.png')
    while True:
        # checkCurrentChatMessages(cb=lambda message : print(message))
        checkCurrentChatMessages(cb=processMessage, echo=True)
        # checkOtherChatMessages()
        time.sleep(.5)
