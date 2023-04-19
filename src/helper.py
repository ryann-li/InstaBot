from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 


def scroll():
    global count
    iter = 1
    while 1:
        scroll_top_num = str(iter * 1000)
        iter += 1
        # scroll down
        driver.execute_script("document.querySelector('div[role=dialog] ul').parentNode.scrollTop=" + scroll_top_num)
        try:
            WebDriverWait(driver, 1).until(check_difference_in_count)
        except:
            count = 0
            break


def get_followers():
    list_followers ="//div[@role='dialog']//li"
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, list_followers)))

    scroll(driver)

    list_elems = driver.find_elements_by_xpath(list_followers)
    time.sleep(100)
    
    followers = []

    while i < (len(list_elems)):
        row_text = list_elems[i].text
        username = row_text[:row_text.index("\n")]
        followers.append(username)
    
    return followers




def get_following():
    list_following ="//div[@role='dialog']//li"
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, list_following)))

    scroll(driver)

    list_elems = driver.find_elements_by_xpath(list_following)
    time.sleep(100)
    
    following = []

    while i < (len(list_elems)):
        row_text = list_elems[i].text
        username = row_text[:row_text.index("\n")]
        following.append(username)

    return following
