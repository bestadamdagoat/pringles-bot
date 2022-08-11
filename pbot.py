from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random

service = Service(executable_path="chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_extension('./anticaptcha-blank.zip')
driver = webdriver.Chrome('./chromedriver.exe', options=options)


def bot():
    catchall = "YOURCATCHALLHERE"
    genned_email = str(random.randrange(1000, 999999)) + "@" + catchall
    ##
    driver.get("https://pringlessweepstakes.com/")
    ##
    driver.implicitly_wait(100)
    ##
    email = driver.find_element(by=By.NAME, value="email")
    email_confirm = driver.find_element(by=By.NAME, value="email_confirm")
    email.send_keys(genned_email)
    email_confirm.send_keys(genned_email)
    ##
    dob_m = driver.find_element(by=By.NAME, value="month")
    dob_d = driver.find_element(by=By.NAME, value="day")
    dob_y = driver.find_element(by=By.NAME, value="year")
    dob_m.send_keys(str(random.randrange(1, 12)))
    dob_d.send_keys(str(random.randrange(1, 29)))
    dob_y.send_keys(str(random.randrange(1970, 2000)))
    ##
    rules = driver.find_element(by=By.NAME, value="agreement")
    rules.click()
    ##
    WebDriverWait(driver, 120000).until(lambda x: x.find_element(By.CSS_SELECTOR, '.antigate_solver.solved'))
    ##
    play = driver.find_element(by=By.ID, value="formButton")
    play.click()
    ##
    WebDriverWait(driver, 15).until(EC.url_changes('https://pringlessweepstakes.com/'))
    ##
    driver.get("https://pringlessweepstakes.com/final.php")
    print("Finished Attempt")


while True:
    bot()
