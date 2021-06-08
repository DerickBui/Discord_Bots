import os
import discord
import random
from replit import db

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
  
  msg = message.content # make it easier to shorthand

  if msg.startswith('-add'): # The greetings command
    # await allows to wait for message to be received
    numbers = msg.split('-add', 1)[1] # only get list of numbers (needs fixing)
    # need to convert list of strings to values
    await message.channel.send("Hello!")

client.run(os.environ['TOKEN']) # Run bot using private token
