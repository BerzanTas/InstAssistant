from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep




class LikeLoop:
    def __init__(self, username, password, hashtag, like_amount, break_time):
        self.PATH = "chromedriver"
        self.username = username
        self.password = password
        self.hashtag = hashtag
        self.like_amount = like_amount
        self.break_time = break_time

        self.driver = webdriver.Chrome(self.PATH)
        self.driver.get('https://www.instagram.com/')



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

    def searchHashtag(self):
        #SEARCHING FOR A USER
        search_button = self.driver.find_element(By.XPATH,'//div[@class="x9f619 xxk0z11 xvy4d1p x11xpdln xii2z7h x19c4wfv"]//*[@aria-label="Szukaj"]')
        search_button.click()
        sleep(2)


        search_input = self.driver.find_element(By.XPATH,"//*[@aria-label='Pole wejściowe wyszukiwania']")
        search_input.clear()

        search_input.send_keys(self.hashtag)
        sleep(3)
        search_input.send_keys(Keys.ENTER)
        sleep(3)
        search_input.send_keys(Keys.ENTER)
        sleep(7)


    def mainAction(self):
        #CREATING LOOP
        #I am creating a loop so the user doesn't have to execute the program every single time.
        #Instead, the loop will fall asleep for a certain period of time.
        while(True):

            #SCROLLING TO THE MOST RECENT POSTS SECTION
            self.driver.execute_script("window.scrollTo(0,600);")
            sleep(2)

            most_recent = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/article/div[2]/div/div[1]/div[1]/a/div/div[2]")
            most_recent.click()
            sleep(3)

            counter = 0
            while(counter < self.like_amount):
                like_button = self.driver.find_element(By.XPATH, '//div[@class = "_abm0 _abl_"]//*[@aria-label]')
                like_button_text = like_button.get_attribute("aria-label")
                if like_button_text == "Lubię to!":
                    like_button.click()
                sleep(3)

                next_button = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div[2]/button")
                next_button.click()
                sleep(3)
                counter += 1
            self.breakAndRefresh()



    def breakAndRefresh(self):
            ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
            sleep(self.break_time)
            self.driver.refresh()
            sleep(10)


    def runAll(self):
        self.cookies()
        self.instaLogin()
        self.skipPopupWindows()
        self.searchHashtag()
        self.mainAction()


















'''
#ACCEPT COOKIES
cookies = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Zezwól tylko na niezbędne pliki cookie')]")))
cookies.click()
sleep(1)


#SIGNING-IN TO INSTAGRAM
user_input = input("Enter your Instagram login/e-mail/phone number: ")
user_input2 = input("Enter password: ")

username = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
password = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')

username.clear()
password.clear()

username.send_keys(user_input)
password.send_keys(user_input2)
sleep(1)

password.submit()

#INSTAGRAM POPUP NOTIFICATIONS SKIPPING
dont_remember_password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Nie teraz')]"))).click()
sleep(1)

not_now = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Nie teraz')]"))).click()
sleep(3)

#SEARCHING FOR GIVEN HASHTAG
search_button = driver.find_element(By.XPATH,"//*[@aria-label='Szukaj']")
search_button.click()
sleep(2)


search_input = driver.find_element(By.XPATH,"//*[@aria-label='Pole wejściowe wyszukiwania']")
search_input.clear()

hashtag = input("Enter the hashtag: ")
#here I am checking if the user gave me the hashtag name with a hashtag, if so, I am replacing it with nothing.
hashtag = hashtag.replace("#","") 
hashtag = "#"+(hashtag)

search_input.send_keys(hashtag)
sleep(1)

search_input.send_keys(Keys.ENTER)
sleep(2)

search_input.send_keys(Keys.ENTER)
sleep(5)
'''


if __name__ == "__main__":
    print("WARNING!")
    sleep(1)
    print("You may be get blocked if you'll set a large like amount and small break time!")
    sleep(1)
    print("The suggested amounts for likes and break are:\n10 likes every 300 seconds")
    sleep(1)

    username = input("Enter your Instagram login/e-mail/phone number: ")
    password = input("Enter password: ")
    hashtag = input("Enter the hashtag: ")
    #here I am checking if the user gave me the hashtag name with a hashtag, if so, I am replacing it with nothing.
    hashtag = hashtag.replace("#","") 
    hashtag = "#"+(hashtag)
    like_amount = int(input("How many post to like in a single loop?: "))
    break_time = int(input("How long should the break be? (seconds): "))
    sleep(1)

    print("Sit back and let me grow your account!")
    sleep(2)


    run = LikeLoop(username, password, hashtag, like_amount, break_time)
    run.runAll()