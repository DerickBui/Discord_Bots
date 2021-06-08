import os
import discord
import random
from replit import db

# function that converts list of strings into float
def numberListConversion(message, stringedNums):
  numberList = []
  errorMessage = ""
  for i in stringedNums: # go through list of number strings
    try:
      numberList.append(float(i)) # convert string to float
    except ValueError: # if input causing errors, error message will be sent
      errorMessage = "Some value input error, values causing errors removed from equation"

  return [numberList, errorMessage] # return list of floats

client = discord.Client()

@client.event # asynchronous library
async def on_ready(): # only starts when bot is ready and working for use, tells that the bot is online
  print('We have logged in as {0.user}'.format(client))

@client.event
# async allows function to run, even if there's delays
async def on_message(message): # only triggers when certain message from others are received
  print(message.content)
  if message.author == client.user: # if self (bot)
    return

# add command ------------------------------------------------------------------------
  if message.content.startswith('-add'): # The add command
    # await allows to wait for message to be received
    numbers = message.content.split(' ')[1:] # only get string of numbers and spaces
    print(numbers)
    # need to convert list of strings to values
    data = numberListConversion(message, numbers)
    if (data[1] != ''):
      await message.channel.send(data[1])
    
    total = 0
    for i in range(len(data[0])):
      total = total + data[0][i]

    await message.channel.send("The answer is: " + str(total))

# subtract command -------------------------------------------------------------------

# multiplication command -------------------------------------------------------------

# division command -------------------------------------------------------------------

# power command ----------------------------------------------------------------------

client.run(os.environ['TOKEN']) # Run bot using private token
