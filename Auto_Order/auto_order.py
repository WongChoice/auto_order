import os
import array as arr
from pandas import array
from selenium.webdriver.common.keys import Keys
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://www.flipkart.com/")

time.sleep(2.5)
t=[]
t=driver.find_element("xpath","/html/body/div[2]/div/div/div/div/div[2]/div/form/div[1]/input")
t.click()
t.send_keys("userid")

t=driver.find_element("xpath","/html/body/div[2]/div/div/div/div/div[2]/div/form/div[2]/input")
t.click()
t.send_keys("pass")

t=driver.find_element("xpath","/html/body/div[2]/div/div/div/div/div[2]/div/form/div[4]/button")
t.click()

time.sleep(5.5)
t= driver.find_element("xpath","//*[@id='container']/div/div[2]/div/div/div[2]/a/div[1]/div/img")
t.click()
time.sleep(2.5)
arr = ["mustard oil 1L", "masoor dal 1kg","toor dal 1kg"]

for i in range (len(arr)):  
 t= driver.find_element("xpath","//*[@id='container']/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input")
 t.click() 
 t.clear()
 t.send_keys(arr[i])
 time.sleep(6)

 t= driver.find_element("xpath","//*[@id='container']/div/div[1]/div[1]/div[2]/div[2]/form/div/button")
 t.click()
 time.sleep(2.5)
 t = driver.find_element("xpath","//*[@id='container']/div/div[3]/div[2]/div[2]/div/div[1]/div[1]/div/div[2]/div[3]")
 t .click()
 time.sleep(2.5)
 t = driver.find_element("xpath","//*[@id='container']/div/div[3]/div[2]/div[2]/div/div[2]/div/div[1]/div/div/div[3]/button[2]")
 
 t.click()
driver.close()