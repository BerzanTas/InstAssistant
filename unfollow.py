from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep



class Unfollow:
    def __init__(self, username, password):
        self.PATH = "chromedriver"
        self.username = username
        self.password = password
        #self.unfollow_amount = unfollow_amount
        #self.break_time = break_time

        self.driver = webdriver.Chrome(self.PATH)
        self.driver.get('https://www.instagram.com/')



    def prepareTo(self):
        cookies = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Zezwól tylko na niezbędne pliki cookie')]")))
        cookies.click()
        sleep(1)

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

        #INSTAGRAM POPUPS SKIPPING
        dont_remember_password = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Nie teraz')]"))).click()
        sleep(5)

        not_now = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Nie teraz')]"))).click()
        sleep(5)


        my_profile = self.driver.find_element(By.XPATH,'//div[@class = "_ab8w  _ab94 _ab99 _ab9f _ab9m _ab9p  _abcj _abcm"]//img')
        my_profile.click()
        sleep(5)

        

    def unfollow(self):
        self.unfollow_buttons = self.driver.find_elements(By.XPATH, '//button[@class = "_acan _acap _acat"]')
        return self.unfollow_buttons

    

    def mainaction(self):
        while(True):
            #CLICK ON FOLLOWS
            
            my_follows = self.driver.find_element(By.XPATH, '//div[contains(text(), "Obserwowani: ")]')
            my_follows.click()
            sleep(2)
            
            counter = 0

            while(True):
                try:

                    unfollow_butt = self.unfollow()
                    for button in unfollow_butt:

                        self.driver.execute_script("arguments[0].scrollIntoView(true);", button)
                            
                        if button.text == 'Obserwowanie' and counter<6:
                            button.click()
                            counter+=1
                            sleep(2)

                            stopfollowingbutton = self.driver.find_element(By.XPATH, "//button[@class = '_a9-- _a9-_']")
                            stopfollowingbutton.click()
                            sleep(2)

                    if counter == 6:
                        break
                    self.driver.execute_script("arguments[0].scrollIntoView(true);", unfollow_butt[-1])
                    sleep(2)
                except Exception as e:
                    print(e)

            self.waitAndRefresh()

    def waitAndRefresh(self):
        ActionChains.send_keys(Keys.ESCAPE)
        sleep(1)
        exit_button = self.driver.find_element(By.XPATH, "//div[@class='_abm0']//*[@aria-label='Zamknij']")
        exit_button.click()
        sleep(2)
        self.driver.refresh()
        sleep(300)


    def runAll(self):
        self.prepareTo()
        self.unfollow()
        self.mainaction()




if __name__ == "__main__":

    run = Unfollow("Karaluki1", "testowyinsta")
    run.runAll()