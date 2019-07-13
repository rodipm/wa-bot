import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome('D:\\chromedriver.exe')
driver.get('https://web.whatsapp.com/')

lastLength = 0

def waitForQR():
    print("Waiting for QR code...")
    while True:
        try:
            driver.find_element_by_class_name('_3RWII')
            print("QR Code Loaded. Waiting for chat...")
            break
        except:
            time.sleep(.5)

def waitForChat():
    while True:
        try:
            driver.find_element_by_class_name('_3u328.copyable-text.selectable-text')
            print("Chat Loaded.")
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
            print("Chat Selected.")
            break
        except:
            print("Nope")
            pass
        time.sleep(.5)

def SendMessage(message):
    messageBox = driver.find_element_by_class_name('_3u328.copyable-text.selectable-text')
    messageBox.send_keys(message)
    messageBox.send_keys(Keys.RETURN)

def checkOtherChatMessages():
    chats = driver.find_elements_by_class_name('X7YrQ')

    for chat in chats:
        try:
            chat.find_element_by_class_name('_1ZMSM')
            chooseChat(chat=chat)
            print("New Messages Detected on Another Chat...")
        except:
            pass

def checkCurrentChatMessages(cb):
    global lastLength
    if not lastLength:
        lastLength = len(driver.find_elements_by_class_name('selectable-text.invisible-space.copyable-text'))

    for _ in range(10):
        messages = driver.find_elements_by_class_name('selectable-text.invisible-space.copyable-text')
        currentLength = len(messages)

        if currentLength > lastLength:
            print("New Message Detected on current chat...")
            message = messages[lastLength-1].get_attribute('innerHTML')
            lastLength = currentLength + 1
            cb(message)
            print("Executed Callback...")
        time.sleep(.5)

if __name__ == "__main__":
    waitForQR()
    chooseChat()
    waitForChat()
    while True:
        checkCurrentChatMessages(cb=lambda message: print(message))
        checkOtherChatMessages()
        time.sleep(.5)