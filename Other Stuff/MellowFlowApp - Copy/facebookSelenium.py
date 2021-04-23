import openpyxl

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import autoit
import time
import sys, os
from sys import platform
from datetime import datetime, timedelta

class fblogin():
    def __init__(self, username, password, message, photo_filepath = "", master=None):
        # TODO : LOAD EXCEL FILE
        print("INIT")
        self.username = username
        self.password = password

        self.link = "https://www.facebook.com/"
        self.options = Options()
        self.options.add_argument("--disable-infobars")
        self.options.add_argument("start-maximized")
        self.options.add_argument("--disable-extensions")
        self.options.add_argument("--disable-notifications")
        self.options.add_argument("--disable-application-cache")

        #TODO OPTION TO SEE CHROME

        self.options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.path = os.path.abspath(os.path.dirname(sys.argv[0]))

        # For launching selenium on each platform
        if platform == "win32":
            self.cd = '/chromedriver.exe'
        elif platform == "linux":
            self.cd = '/chromedriver_linux'
        elif platform == "darwin":
           self. cd = '/chromedriver'

        self.driver = webdriver.Chrome(self.path + self.cd, options=self.options)

        #TODO DEFINE SELECTION BTW POSTING TO GROUP OR TO PAGE
        self.driver.get(self.link)  # Read link
        time.sleep(3)

        # driver.find_element_by_xpath ("//*[@id="u_0_j_Zi"]").click ()
        self.driver.find_element_by_css_selector("[name*='email']").click()
        print(f"Press on <Accept All> button...")

        time.sleep(3)

        self.login(id= self.username, password= self.password)
        print(f"Login To Facebook...")
        time.sleep(3)

        # TODO SET UP PAGE LINK
        self.link_code = "/2299601160183761"
        self.textCell = message

        try:
            link2 = "https://www.facebook.com/groups" + self.link_code
            self.driver.get(link2)
            print(f"Working on link {link2}...")
            time.sleep(3)
            self.driver.find_element_by_xpath("//span[.='Create a public post…']").click()
            print(f"Click in Message field...")
            time.sleep(3)
            # Important for Creating message
            actions = ActionChains(self.driver)
            actions.send_keys(self.textCell)
            actions.perform()
            # driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div[1]/div[2]/div[1]/div[1]/div[1]/div/div/div/div/div/div/div/div/div/span/span').send_keys(text)
            print(f"Write text to message box...")
            time.sleep(3)

            # self.driver.find_element_by_xpath("//aria-label[.='Photo/Video']").click()

            #uploadElement.sendKeys(photo_filepath)
            import math
            try:
                if math.isnan(photo_filepath):
                    print("No photos")
                    # uploadElement = self.driver.find_element_by_css_selector("[aria-label*='Photo/Video']").click()
                    # autoit.win_wait_active("Open", 15)
                    # autoit.send(str(photo_filepath).replace('/', r'\ '[0]))
                    # autoit.send("{ENTER}")
            except:
                uploadElement = self.driver.find_element_by_css_selector("[aria-label*='Photo/Video']").click()
                autoit.win_wait_active("Open", 15)
                autoit.send(str(photo_filepath).replace('/', r'\ '[0]))
                autoit.send("{ENTER}")
            time.sleep(3)
            self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div[1]/div[3]/div[2]/div[1]/div').click()
            print(f"Send message...")
            time.sleep(3)
            print(f"Message send on Facebook for site {self.link_code} for cell {self.textCell}")
        except Exception as e:
            print(f"Error while working on for site {self.link_code} - wrote error to column...")
            print(f"ErrorCode: {e}")


        self.driver.quit()


    def login(self,id,password):
        email = self.driver.find_element_by_id("email")
        email.send_keys(id)
        Password = self.driver.find_element_by_id("pass")
        Password.send_keys(password)
        button = self.driver.find_element_by_name("login").click()
        pass


def startFBLogin(username,password, message="",filePath=""):
    fblogin(username,password, message,filePath)

