from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 



username = input("enter your username: ")
password = input("enter your password: ")

def Instabot():
    
#goes to instagram chrome

    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
    time.sleep(1)

#logs user in
    driver.find_element_by_name("username").send_keys(username)
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_name("password").send_keys(u'\ue007')

#deals with pop up options that automatically show up after logging in
    not_now = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()
    not_now2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()

#goes to user's profile
    profile1 = '[alt*="' + username + '"]'
    profile2 = "[href*=\"" + username + "\"]"

    button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, profile1)))
    button.click()

    button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, profile2)))
    button.click()
    time.sleep(1)

#goes to user's followers
    followers = "[href*=\"" + username + "/followers/\"]"

    button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, followers)))
    button.click()

    list_followers ="//div[@role='dialog']//li"
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, list_followers)))

    list_elems = driver.find_elements_by_xpath(list_followers)
    time.sleep(100)
    
#adds followers to a list
    followers = []

    while i < (len(list_elems)):
        row_text = list_elems[i].text
        username = row_text[:row_text.index("\n")]
        followers.append(username)

#closes followers page
    close_followers = '[aria-label="Close"]'

#goes to user's followings
    followers = "[href*=\"" + username + "/following/\"]"

    button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, followers)))
    button.click()

    list_following ="//div[@role='dialog']//li"
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, list_following)))

    list_elems = driver.find_elements_by_xpath(list_following)
    time.sleep(100)
    
#adds following to a list
    following = []

    while i < (len(list_elems)):
        row_text = list_elems[i].text
        username = row_text[:row_text.index("\n")]
        following.append(username)

    not_following_back = []

#checks if people you are following are following you back
    for i in len(following):
        if following[i] not in followers:
            not_following_back.append(following[i])
    
#prints users who do not follow back
    print(not_following_back)


Instabot()




