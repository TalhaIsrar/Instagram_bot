from selenium import webdriver 
from time import sleep 
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.chrome.options import Options
import pyperclip as pc
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

print('===>Script started!')

print('===>Opening Browser')
driver = webdriver.Chrome(r'C:\Users\x\Desktop\Python\chromedriver.exe')
driver.implicitly_wait(15)
sleep(1)

print('===>Opening new account')
driver.get('https://temp-mail.org/en/')
driver.implicitly_wait(15)
sleep(2)

copy_email = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div[1]/form/div[2]/button")
copy_email.click()

print('===>Opening Instagram')
driver2 = webdriver.Chrome(r'C:\Users\x\Desktop\Python\chromedriver.exe')
driver2.implicitly_wait(15)
sleep(2)

print('===>Opening instagram signup')
driver2.get('https://www.instagram.com/accounts/emailsignup/')
driver2.implicitly_wait(15)
sleep(2)

email = pc.paste()
user = email.split("@")

username = driver2.find_element_by_name('emailOrPhone')
username.send_keys(email) 
sleep(2)

password = driver2.find_element_by_name('fullName')
password.send_keys(user[0]) 
sleep(2)

username = driver2.find_element_by_name('username')
username.send_keys(user[0]) 
sleep(2)

password = driver2.find_element_by_name('password')
password.send_keys('Talha123') 
sleep(2)

button_signup = driver2.find_element(By.XPATH, "/html/body/div[1]/section/main/div/div/div[1]/div/form/div[7]/div/button")
button_signup.click()
sleep(2)

print('===>Selecting DOB')
select_month = Select(driver2.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[1]/div/div[4]/div/div/span/span[1]/select"))
select_month.select_by_index(1)
sleep(2)

select_day = Select(driver2.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[1]/div/div[4]/div/div/span/span[2]/select"))
select_day.select_by_index(1)
sleep(2)

select_year = Select(driver2.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[1]/div/div[4]/div/div/span/span[3]/select"))
select_year.select_by_index(20)
sleep(2)

button_dob = driver2.find_element(By.XPATH, "/html/body/div[1]/section/main/div/div/div[1]/div/div[6]/button")
button_dob.click()
sleep(25)

print('===>Verifying Email')
confirm = driver.find_element(By.XPATH,"/html/body/main/div[1]/div/div[2]/div[2]/div/div[1]/div/div[4]/ul/li[2]/div[2]/span/a").text
code = confirm.split(" ")
confirm_code = code[0]

print('===>Confirming Email')
conf = driver2.find_element(By.XPATH,"/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[1]/input")
conf.send_keys(confirm_code) 
sleep(2)

print('===>Email Confirmed')
button_confirmed = driver2.find_element(By.XPATH, "/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[2]/button")
button_confirmed.click()
sleep(2)

