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
  
  if message.content.startswith('$hello'):
    greetings = ['Hello!', 'Tally-Ho!', 'HOWDY!']

    # await allows to wait for message to be received
    await message.channel.send(greetings[random.randint(0, len(greetings))])

client.run(os.environ['TOKEN']) # Run bot using private token
