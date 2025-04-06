from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import userInformation
import time

browser = webdriver.Chrome()
browser.get("https://x.com/")
browser.maximize_window()

try:
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/login']"))).click()
    
    username = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@name='text']"))
    )
    username.send_keys(userInformation.UserName())
    browser.find_element(By.XPATH, "//span[contains(text(),'İleri')]").click()
    
    password = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@name='password']"))
    )
    password.send_keys(userInformation.Password())
    browser.find_element(By.XPATH, "//span[contains(text(),'Giriş yap')]").click()

    
    search = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@data-testid='SearchBox_Search_Input']"))
    )
    search.send_keys("yönetim bilişim sistemleri")
    search.send_keys(Keys.RETURN)

    
    last_height = browser.execute_script("return document.body.scrollHeight")
    while True:
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        new_height = browser.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    
    like_buttons = WebDriverWait(browser, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, '[data-testid="like"]'))
    )
    
    for button in like_buttons:
        try:
            browser.execute_script("arguments[0].scrollIntoView();", button)
            WebDriverWait(browser, 2).until(EC.element_to_be_clickable(button))
            browser.execute_script("arguments[0].click();", button)
            time.sleep(1) 
        except Exception as e:
            print(f"Beğenme hatası: {str(e)}")
            continue
    
    
    save_buttons = WebDriverWait(browser, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, '[data-testid="bookmark"]'))
    )
    
    for button in save_buttons:
        try:
            browser.execute_script("arguments[0].scrollIntoView();", button)
            WebDriverWait(browser, 2).until(EC.element_to_be_clickable(button))
            browser.execute_script("arguments[0].click();", button)
            time.sleep(1)
        except Exception as e:
            print(f"Beğenme hatası: {str(e)}")
            continue
    
finally:
    browser.quit()