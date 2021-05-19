import os
import discord
import random

client = discord.Client()

@client.event # asynchronous library
async def on_ready(): # only starts when bot is ready and working for use
  print('We have logged in as {0.user}'.format(client))

@client.event
# async allows function to run, even if there's delays
async def on_message(message): # only triggers when certain message from others are received
  if message.author == client.user: # if self (bot)
    return
  
  if message.content.startswith('-hello'): # The greetings command
    greetings = ['Hello!', 'Tally-Ho!', 'HOWDY!']
    
    await message.channel.send(greetings[random.randint(0, len(greetings))]) # await allows to wait for message to be received

  if message.content.startswith('-joke'): # The "joke" command
    joke = ['You\'re mom\'s so fat, a wall containing her broke down!', 'You suck!', 'You smell like farts.']

    await message.channel.send(joke[random.randint(0, len(joke))]) # await allows to wait for message to be received

client.run(os.environ['TOKEN']) # Run bot using private token
