from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options


#Constants to be added to settings
TIME_BETWEEN_CHECKS = 5
AMOUNT_TO_BUY = 1


#Unused
WEB_PAGES = ['https://www.amazon.co.uk/BIC-Cello-Comfort-Ballpoint-Medium/dp/B07RY6ZC83/ref=sr_1_2_sspa?dchild=1&keywords=pen&qid=1613387800&sr=8-2-spons&psc=1&smid=A2RCZCHI7CGC8P&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFTS0tQSkFYRkRNMEYmZW5jcnlwdGVkSWQ9QTAwNzI2MDMzOVdOSVhDV1lKMDc1JmVuY3J5cHRlZEFkSWQ9QTA4NjIxMjczVFBRQkVHSVhKM0EzJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ==']

CHROME_DRIVER_LOCATION = 'chromedriver.exe'



class AmazonBot():
    def __init__(self, WEB_PAGES):
        try:
            self.driver = webdriver.Chrome(CHROME_DRIVER_LOCATION)
        except:
            try:
                self.driver = webdriver.Chrome()
            except:
                print('Cant find valid Chrome driver')
        self.WEB_PAGES = WEB_PAGES

    def login(self, username, password):
        self.driver.get('https://www.amazon.co.uk/')
        #Accepts Cookies
        try:
            self.driver.find_element_by_id("sp-cc-accept").click()
        except:
            pass
        
        #Enters User details
        self.driver.find_element_by_id("nav-link-accountList").click()
        self.driver.find_element_by_id("ap_email").send_keys(username)    
        self.driver.find_element_by_id("continue").click()
        sleep(0.5)
        self.driver.find_element_by_name('rememberMe').click()
        self.driver.find_element_by_id("ap_password").clear()
        self.driver.find_element_by_id("ap_password").send_keys(password)
        self.driver.find_element_by_id("signInSubmit").click()
        sleep(1)

        #If they need to use 2fa gives longer
        url = self.driver.current_url
        if url.startswith('https://www.amazon.co.uk/ap/signin'):
            sleep(120)
        else:
            sleep(10)
        #Enable Oneclick purchase
        self.driver.get('https://www.amazon.co.uk/cpe/yourpayments/settings/manageoneclick')
        self.driver.find_element_by_css_selector('.a-switch-control').click()
        sleep(2)

    #Unused/Needs improving
    def checkStock(self):
        for webpage in self.WEB_PAGES:
            self.driver.get(webpage)
            try:
                self.driver.find_element_by_id("sp-cc-accept").click()
            except:
                pass
            
            try:
                buyNow = self.driver.find_element_by_id('buy-now-button')         
                print('In stock')
            except:
                print('Not in stock')

    #Checks What the Xbox Button is 
    def findXboxButton(self):
        self.driver.get('https://www.amazon.co.uk/Xbox-RRT-00007-Series-X/dp/B08H93GKNJ/')

        #Accepts Cookies
        try:
            self.driver.find_element_by_id("sp-cc-accept").click()
        except:
            pass
        sleep(1)

        #Trys all product options till error which indicates all have been tried or Xbox Series X has been found
        try:
            i = 0
            while True:
                selectbtn = self.driver.find_element_by_id(f'edition_{i}')
                #Sees if button value is eqal to Xbox Series X
                if selectbtn.text == 'Xbox Series X':
                    self.xboxNumber = i
                    break
                i=i+1
        except:
            #Needs proper error handling adding
            print('Error')



    #Checks Stock
    def xboxCheckStock(self):
        #Gets Xbox Page
        self.driver.get('https://www.amazon.co.uk/Xbox-RRT-00007-Series-X/dp/B08H93GKNJ/')

        #Accepts Cookies
        try:
            self.driver.find_element_by_id("sp-cc-accept").click()
        except:
            pass
        sleep(1)

        #Selects the Xbox
        selectbtn = self.driver.find_element_by_id(f'edition_{self.xboxNumber}')
        if selectbtn.text == 'Xbox Series X':
            selectbtn.click()
            #self.driver.find_element_by_partial_link_text('Xbox Series X')
            sleep(2)

            #Looks for buy now
            try:
                buyNow = self.driver.find_element_by_id('buy-now-button')         
                print('In stock')
                return True
            #If error its not availible
            except:
                print('Not in stock')
                return False
            sleep(1)
        #This runs when the btutton is wrong
        else:
            #Needs proper error handling adding
            print('Error')

    #Need creating
    def Buy(self):
        buyNow = self.driver.find_element_by_id('buy-now-button')
        buyNow.click()
        
#Needs creating
def AlertUser():
    pass




bot = AmazonBot(WEB_PAGES)

username = input('username')
password = input('password')
bot.login(username, password)

bot.findXboxButton()

#Runs while not in stock/availible
stock = False
while not stock:
    stock = bot.xboxCheckStock()
    sleep(TIME_BETWEEN_CHECKS)

AlertUser()
bot.login(username, password)
bot.Buy()

