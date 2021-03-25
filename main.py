from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys
import time

email = "iamprakash1609@gmail.com"
password = "pcchater@1609"
webdriver_path = "C:\Chrome driver\chromedriver.exe"
url = "https://tinder.com/"
driver = webdriver.Chrome(executable_path=webdriver_path)
driver.get(url)

time.sleep(5)
log_in = driver.find_element_by_xpath('//*[@id="t--771258051"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/button')
log_in.click()
time.sleep(3)
try:
    fb_login = driver.find_element_by_xpath('//*[@id="t-1483503441"]/div/div/div[1]/div/div[3]/span/div[2]/button')
except NoSuchElementException:
    more_option = driver.find_element_by_xpath('//*[@id="t-1483503441"]/div/div/div[1]/div/div[3]/span/button')
    more_option.click()
    time.sleep(3)
    fb_login = driver.find_element_by_xpath('//*[@id="t-1483503441"]/div/div/div[1]/div/div[3]/span/div[2]/button')
    fb_login.click()
else:
    time.sleep(3)
    fb_login.click()


time.sleep(3)
#Switch to Facebook login window
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

#LOGIN AND ENTER
email_login = driver.find_element_by_xpath('//*[@id="email"]')
email_login.send_keys(email)
password_login = driver.find_element_by_xpath('//*[@id="pass"]')
password_login.send_keys(password)
login = driver.find_element_by_xpath('//*[@id="loginbutton"]')
login.send_keys(Keys.ENTER)

#Switch back to Tinder window
driver.switch_to.window(base_window)
print(driver.title)

time.sleep(7)
location = driver.find_element_by_xpath('//*[@id="t-1483503441"]/div/div/div/div/div[3]/button[1]')
location.click()
time.sleep(2)
notification_not_interested = driver.find_element_by_xpath('//*[@id="t-1483503441"]/div/div/div/div/div[3]/button[2]')
notification_not_interested.click()
time.sleep(2)
cookies = driver.find_element_by_xpath('//*[@id="t--771258051"]/div/div[2]/div/div/div[1]/button')
cookies.click()

time.sleep(3)
# like_button = driver.find_element_by_xpath('//*[@id="t--771258051"]/div/div[1]/div/div/main/div/div[1]/div/div[2]/div[4]/button')
# like_button.click()
for i in range(10):
    time.sleep(1)

    try:
        print("swiping")
        like_button = driver.find_element_by_xpath('//*[@id="t--771258051"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]')
        like_button.click()

    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element_by_css_selector(".itsAMatch a")
            match_popup.click()

        except NoSuchElementException:
            time.sleep(3)








