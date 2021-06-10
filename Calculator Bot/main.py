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
    data = numberListConversion(message, numbers) # need to convert list of strings to values
    if (data[1] != ''):
      await message.channel.send(data[1])
    
    total = 0 # start number at zero
    for i in range(len(data[0])):
      total = total + data[0][i]

    if (total.is_integer()): # Convert float to int if float decimal is 0
      total = int(total)

    await message.channel.send("The sum is: " + str(total))

# subtract command -------------------------------------------------------------------
  if message.content.startswith('-subtract'): # The subtract command
    # await allows to wait for message to be received
    numbers = message.content.split(' ')[1:] # only get string of numbers and spaces
    data = numberListConversion(message, numbers) # need to convert list of strings to values
    if (data[1] != ''):
      await message.channel.send(data[1])
    
    total = data[0][0] # grab first numbered input
    for i in range(1, len(data[0])):
      total = total - data[0][i]

    if (total.is_integer()): # Convert float to int if float decimal is 0
      total = int(total)

    await message.channel.send("The difference is: " + str(total))

# multiplication command -------------------------------------------------------------
  if message.content.startswith('-mult'): # The multiplication command
    # await allows to wait for message to be received
    numbers = message.content.split(' ')[1:] # only get string of numbers and spaces
    data = numberListConversion(message, numbers) # need to convert list of strings to values
    if (data[1] != ''):
      await message.channel.send(data[1])
    
    total = 0 # start number at zero
    if (len(data[0]) == 0):
      total = 0
    else:
      total = 1
    for i in range(len(data[0])):
      total = total * data[0][i]

    if (total.is_integer()): # Convert float to int if float decimal is 0
      total = int(total)

    await message.channel.send("The product is: " + str(total))

# division command -------------------------------------------------------------------
  if message.content.startswith('-div'): # The division command
    # await allows to wait for message to be received
    numbers = message.content.split(' ')[1:] # only get string of numbers and spaces
    data = numberListConversion(message, numbers) # need to convert list of strings to values
    if (data[1] != ''):
      await message.channel.send(data[1])
    
    zeroFlag = False # Tells if there is a flag
    total = data[0][0] # grab first numbered input
    for i in range(1, len(data[0])):
      if (data[0][i] != 0):
        total = total / data[0][i]
      else: # failsafe for zeroes
        zeroFlag = True
        await message.channel.send("A zero is not used as first input for division, abort calcluation")
        break

    if (total.is_integer()): # Convert float to int if float decimal is 0
      total = int(total)

    if (zeroFlag == False):
      await message.channel.send("The quotient is: " + str(total))

# power command ----------------------------------------------------------------------
  if message.content.startswith('-power'): # The multiplication command
      # await allows to wait for message to be received
      numbers = message.content.split(' ')[1:] # only get string of numbers and spaces
      data = numberListConversion(message, numbers) # need to convert list of strings to values
      if (data[1] != ''):
        await message.channel.send(data[1])
      
      total = data[0][0] # grab first number
      for i in range(1, len(data[0])):
        total = total ** data[0][i]

      if (total.is_integer()): # Convert float to int if float decimal is 0
        total = int(total)

      await message.channel.send("The power product is: " + str(total))

# modulus command---------------------------------------------------------------------
  if message.content.startswith('-power'): # The multiplication command
    # await allows to wait for message to be received
    numbers = message.content.split(' ')[1:] # only get string of numbers and spaces
    data = numberListConversion(message, numbers) # need to convert list of strings to values
    if (data[1] != ''):
      await message.channel.send(data[1])
    
    if (len(data[0]) == 2):
      total = data[0][0] % data[0][1] # calculate modulus
      if (total.is_integer()): # Convert float to int if float decimal is 0
        total = int(total)

      await message.channel.send("The modulus is: " + str(total))
    else:
      await message.channel.send("Not an appropriate amount of numbers for modulus function")

# deep division command---------------------------------------------------------------

    
client.run(os.environ['TOKEN']) # Run bot using private token
