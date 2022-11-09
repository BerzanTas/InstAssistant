from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

PATH = "chromedriver"

driver = webdriver.Chrome(PATH)
driver.get('https://www.instagram.com/')
print(driver.title)
sleep(2)

cookies = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Zezwól tylko na niezbędne pliki cookie')]")))
cookies.click()
sleep(1)


#LOGIN TO INSTAGRAM

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

#INSTAGRAM POPUPS SKIPPING
dont_remember_password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Nie teraz')]"))).click()
sleep(1)
not_now = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Nie teraz')]"))).click()
sleep(3)

#SEARCHING FOR HASHTAG
search_button = driver.find_element(By.XPATH,"//*[@aria-label='Szukaj']")
search_button.click()
sleep(2)


search_input = driver.find_element(By.XPATH,"//*[@aria-label='Pole wejściowe wyszukiwania']")
search_input.clear()

hashtag = input("Enter the hashtag: ")
hashtag = hashtag.replace("#","")
hashtag = "#"+(hashtag)

search_input.send_keys(hashtag)
sleep(1)
search_input.send_keys(Keys.ENTER)
sleep(1)
search_input.send_keys(Keys.ENTER)
sleep(5)



while(True):
    driver.execute_script("window.scrollTo(0,600);")
    sleep(2)
    most_recent = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/article/div[2]/div/div[1]/div[1]/a/div/div[2]")
    most_recent.click()
    sleep(3)

    counter = 0
    while(counter < 3):
        like_button = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button")
        like_button.click()
        sleep(3)

        next_button = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div[2]/button")
        next_button.click()
        sleep(3)
        counter += 1

    ActionChains(driver).send_keys(Keys.ESCAPE).perform()
    sleep(120)
    driver.refresh()
    sleep(15)