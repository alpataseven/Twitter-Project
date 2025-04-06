from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import userInformation
import time

browser = webdriver.Chrome()

browser.get("https://x.com/")

time.sleep(3)

sign_in = browser.find_element(By.XPATH, "//*[@id='react-root']/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[4]/a/div")

sign_in.click()

time.sleep(5)
user_name = browser.find_element(By.XPATH, "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input")
user_name.send_keys(userInformation.UserName())
time.sleep(5)


next_button = browser.find_element(By.XPATH, "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]/div/span") 
next_button.click()

time.sleep(5)

password = browser.find_element(By.XPATH, "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input")
password.send_keys(userInformation.Password())

time.sleep(5)

login_button = browser.find_element(By.XPATH, "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/button/div/span/span")
login_button.click()

time.sleep(5)

search_input = browser.find_element(By.XPATH, "//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div/div/div[2]/div/input")
search_input.send_keys("yönetim bilişim sistemleri")
search_input.send_keys(Keys.RETURN)

#browser.back() Önceki sayfaya gitmek için bu kod yazılır

time.sleep(5)

#Scroll sabit kalmaması için yazılan kod parçası
lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
match=False
while(match==False):
    lastCount = lenOfPage
    time.sleep(3)
    lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    if lastCount == lenOfPage:
        match=True

time.sleep(5)

tweets = []

elements = browser.find_elements(By.CSS_SELECTOR, ".css-146c3p1.r-8akbws.r-krxsd3.r-dnmrzs.r-1udh08x.r-1udbk01.r-bcqeeo.r-1ttztb7.r-qvutc0.r-37j5jr.r-a023e6.r-rjixqe.r-16dba41.r-bnwqim")
#elements = browser.find_elements(By.CSS_SELECTOR, ".css-175oi2r")
#elements = browser.find_elements(By.CSS_SELECTOR, ".css-146c3p1.r-8akbws.r-krxsd3.r-dnmrzs.r-1udh08x.r-1udbk01.r-bcqeeo.r-1ttztb7.r-qvutc0.r-37j5jr.r-a023e6.r-rjixqe.r-16dba41.r-bnwqim")
#elements = browser.find_elements(By.XPATH, "//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[1]/div/div[5]/section/div/div/div[1]/div[1]/div/article/div/div/div[2]/div[2]/div[2]")

for element in elements:
    tweets.append(element.text)

tweetCount = 1

with open("tweets.txt","w",encoding="UTF-8") as file:
    for tweet in tweets:
        file.write(str(tweetCount) + ".\n" + tweet + "\n") 
        file.write("*****************************************************\n") 
        tweetCount += 1
        
time.sleep(15)

browser.close()