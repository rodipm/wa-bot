import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

options = webdriver.ChromeOptions()
options.add_argument("--user-data-dir=C:\\Users\\Rodrigo\\AppData\\Local\\Google\\Chrome\\Selenium Data\\")
driver = webdriver.Chrome('D:\\chromedriver.exe', chrome_options=options)
driver.get('https://web.whatsapp.com/')

lastLength = 0

def waitForQR():
    print("[wa-bot] Waiting for QR code...")
    while True:
        try:
            driver.find_element_by_class_name('_3RWII')
            print("[wa-bot] QR Code Loaded. Waiting for chat...")
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

def checkCurrentChatMessages(cb):
    print("[wa-bot] Checking for Messages on Current Chat...")

    global lastLength

    if lastLength == 0:
        lastLength = len(driver.find_elements_by_class_name('selectable-text.invisible-space.copyable-text')) - 1

    for _ in range(10):
        messages = driver.find_elements_by_class_name('selectable-text.invisible-space.copyable-text')
        currentLength = len(messages)

        if currentLength > lastLength:
            message = messages[lastLength-1].get_attribute('innerHTML')
            print("[wa-bot] New Message Detected on current chat: {}".format(message))
            lastLength = currentLength + 1
            cb(message)
            print("[wa-bot] Executed Callback...")
        time.sleep(.5)

if __name__ == "__main__":
    waitForQR()
    chooseChat()
    waitForChat()
    while True:
        checkCurrentChatMessages(cb=lambda message: print(message))
        checkOtherChatMessages()
        time.sleep(.5)
