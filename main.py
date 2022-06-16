# BY Z10ASH

from selenium import webdriver
from time import sleep

driver1 = webdriver.Chrome(executable_path="chromedriver.exe")
driver2 = webdriver.Chrome(executable_path="chromedriver.exe")
driver3 = webdriver.Chrome(executable_path="chromedriver.exe")
driver4 = webdriver.Chrome(executable_path="chromedriver.exe")
driver5 = webdriver.Chrome(executable_path="chromedriver.exe")
driver6 = webdriver.Chrome(executable_path="chromedriver.exe")
driver7 = webdriver.Chrome(executable_path="chromedriver.exe")
driver8 = webdriver.Chrome(executable_path="chromedriver.exe")
driver9 = webdriver.Chrome(executable_path="chromedriver.exe")

driver1.get("LINK YT")
driver2.get("LINK YT")
driver3.get("LINK YT")
driver4.get("LINK YT")
driver5.get("LINK YT")
driver6.get("LINK YT")
driver7.get("LINK YT")
driver8.get("LINK YT")
driver9.get("LINK YT")

while True:
    sleep(15)
    driver1()
    driver2()
    driver3()
    driver4()
    driver5()
    driver6()
    driver7()
    driver8()
    driver9()