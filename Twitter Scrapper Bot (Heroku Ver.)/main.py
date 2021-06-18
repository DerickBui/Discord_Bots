# Discord library
import os
import discord
import time

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
    # wait until the search box has loaded:

    # time.sleep(10)
    searchBar = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[1]/div[1]/div/div/div/div/div[1]/div[2]/div/div/div/form/div[1]/div/label/div[2]/div/input')

    # enter your search string in the search box:
    searchBar.send_keys(searchWord)

    # submit the query (like hitting return):
    searchBar.submit()

# Setup------------------------------------------------------------------
driver = webdriver.Chrome('C:\Program Files (x86)\chromedriver.exe')
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

# Discord Client-------------------------------------------------------
client = discord.Client()

@client.event # asynchronous library
async def on_ready(): # only starts when bot is ready and working for use, tells that the bot is online
  print('We have logged in as {0.user}'.format(client))

@client.event
# async allows function to run, even if there's delays
async def on_message(message): # only triggers when certain message from others are received
    if message.author == client.user:  # if self (bot)
        return

    if message.content.startswith('-search'): # Scrape twitter term
        term = message.content.split('-search ')[1]

        await message.channel.send('Searching ' + term)
        
        search(driver, term)

client.run(os.environ['TOKEN']) # Run bot using private token
