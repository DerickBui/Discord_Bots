# Discord and Replit database libraries
import os
import discord
import time
from replit import db

# Selenium libraries
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Functions--------------------------------------------------------------
def search(driver, searchWord): # Searches up keyword
  exploreButton = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[2]/nav/a[2]/div')
  exploreButton.click()

  # time.sleep(10)
  searchBar = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[1]/div[1]/div/div/div/div/div[1]/div[2]/div/div/div/form/div[1]/div/label/div[2]/div/input')

  # enter your search string in the search box:
  searchBar.send_keys(searchWord)

  # submit the query (like hitting return):
  searchBar.submit()

# Selenium and Discord Processes-----------------------------------------
chrome_options = Options() # get Chrome settings for selenium
chrome_options.add_argument('--no-sandbox') # for replit use
chrome_options.add_argument('--disable-dev-shm-usage') # for replit use

driver = webdriver.Chrome(options=chrome_options) # variable that runs automated chrome
driver.wait = WebDriverWait(driver, 10) # create wait process

# Go to Twitter login page
driver.get('https://twitter.com/login') # go to login page
time.sleep(1) # wait for login page to fully load

# Twitter username input
username = driver.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')))
username = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')
username.send_keys(os.environ['USERNAME']) # input username

# Twitter password input and login
password = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input')
password.send_keys(os.environ['PASSWORD']) # input password
password.submit()

# Search keyword function test
search(driver, "")



