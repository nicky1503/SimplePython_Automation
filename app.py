import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-notifications")


driver = webdriver.Chrome(executable_path='D://chromedriver_win32//chromedriver', options=chrome_options)
driver.get("https://www.facebook.com")

driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div/div/div/div[3]/button[2]').click()

input_email = driver.find_element_by_xpath('//*[@id="email"]')
input_email.send_keys('user-email')

input_password = driver.find_element_by_xpath('//*[@id="pass"]')
input_password.send_keys("user-password")
click_log_in = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div'
                                            '/div/div[2]/div/div[1]/form/div[2]/button').click()
click_on_messenger = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div[4]'
                                                  '/div[1]/div[2]/span/div/div[1]').click()
time.sleep(8)
search_for_user = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div[4]'
                                               '/div[2]/div/div/div[1]/div[1]/div/div/div/div/div'
                                               '/div/div[1]/div/div[1]/div[1]/div[2]/div/div[1]/div/div/div/label/input')
search_for_user.send_keys('Name of_user')
time.sleep(1)
click_on_chat_with_user = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div[4]/div[2]/div/div/div[1]/div[2]/div/div/div[1]/div[1]/div/div/div[1]/ul/li[1]/ul/li/div/a/div').click()
time.sleep(1)
messages = ['message 1']
for message in messages:
    click_on_chat_box = driver.find_element_by_xpath(
        '/html/body/div[1]/div/div[1]/div/div[5]/div/div[1]/div[1]/div[1]/div/div/div/div/div/div/div[2]/div/div[2]'
        '/form/div/div[3]/div[2]/div[1]/div/div/div/div/div[2]/div/div/div/div/span')
    click_on_chat_box.send_keys(message, Keys.ENTER)
    time.sleep(1)
