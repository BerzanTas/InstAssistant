from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep




class FollowPeople():

    def __init__(self, username, password, targetUsername):
        self.PATH  =  "chromedriver"
        self.driver = webdriver.Chrome(self.PATH)
        self.driver.get('https://www.instagram.com/')
        self.username = username
        self.password = password
        self.targetUsername = targetUsername
        

    def cookies(self):
        cookies = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Zezwól tylko na niezbędne pliki cookie')]")))
        cookies.click()
        sleep(1)

    def instaLogin(self):
        #LOGIN TO INSTAGRAM
        usernameBox = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        passwordBox = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')

        usernameBox.clear()
        passwordBox.clear()

        usernameBox.send_keys(self.username)
        passwordBox.send_keys(self.password)
        sleep(1)

        passwordBox.submit()
        sleep(7)

    def skipPopupWindows(self):
        #INSTAGRAM POPUPS SKIPPING
        dont_remember_password = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Nie teraz')]"))).click()
        sleep(5)

        not_now = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Nie teraz')]"))).click()
        sleep(5)

    def searchUSer(self):
        #SEARCHING FOR A USER
        search_button = self.driver.find_element(By.XPATH,'//div[@class="x9f619 xxk0z11 xvy4d1p x11xpdln xii2z7h x19c4wfv"]//*[@aria-label="Szukaj"]')
        search_button.click()
        sleep(2)


        search_input = self.driver.find_element(By.XPATH,"//*[@aria-label='Pole wejściowe wyszukiwania']")
        search_input.clear()

        user = self.targetUsername

        search_input.send_keys(user)
        sleep(2)
        search_input.send_keys(Keys.ENTER)
        sleep(2)
        search_input.send_keys(Keys.ENTER)
        sleep(7)




    def findFollowButton(self):
        self.follow_buttons = self.driver.find_elements(By.XPATH, '//div[@class="_ab8w  _ab94 _ab97 _ab9h _ab9k _ab9p  _abb0 _abcm"]//*//*//*')
        return self.follow_buttons

    def mainAction(self):
        while(True):
            #CLICK ON FOLLOWERS
            
            followers = self.driver.find_element(By.XPATH, '//li[@class="xl565be x1m39q7l x1uw6ca5 x2pgyrj"]//a')
            followers.click()
            sleep(3)
            
            counter = 0

            while(True):
                try:

                    follow_butt = self.findFollowButton()
                    for buttons in follow_butt:

                        self.driver.execute_script("arguments[0].scrollIntoView(true);", buttons)
                            
                        if buttons.text == 'Obserwuj' and counter<6:
                            buttons.click()
                            counter+=1
                            sleep(2)

                    if counter == 6:
                        break
                    self.driver.execute_script("arguments[0].scrollIntoView(true);", follow_butt[-1])
                    sleep(2)
                except Exception as e:
                    print(e)

            self.waitAndRefresh()

    def waitAndRefresh(self):
        exit_button = self.driver.find_element(By.XPATH, "//div[@class='_abm0']//*[@aria-label='Zamknij']")
        exit_button.click()
        sleep(2)
        self.driver.refresh()
        sleep(300)
    
    def runAll(self):
        self.cookies()
        self.instaLogin()
        self.skipPopupWindows()
        self.searchUSer()
        self.mainAction()



if __name__ == "__main__":

    username = input("Enter your Instagram login/e-mail/phone number: ")
    sleep(1)
    password = input("Enter password: ")
    sleep(1)
    target = input("Enter target's username: ")
    sleep(1)

    run = FollowPeople(username, password, target)
    run.runAll()