from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
import pyautogui as py
import pyperclip
import time

navigator = webdriver.Chrome('chromedriver.exe')
navigator.get('https://www.google.com.br')
navigator.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('Kaggle')
navigator.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
navigator.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div/div/div/div/div/div[1]/a/h3').click()
navigator.find_element_by_xpath('//*[@id="site-container"]/div/div[1]/div[1]/div/div/div[1]/button').click()
navigator.find_element_by_xpath('//*[@id="site-container"]/div/div[2]/div[3]/div[1]/div/ul/li[3]/div/a').send_keys(Keys.ENTER)
"""time.sleep(2)
py.scroll(-32)
time.sleep(3)
print(py.position())"""




