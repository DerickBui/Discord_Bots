import os
import discord
import random
from replit import db
from keep_alive import keep_alive

client = discord.Client()

greetings = ['Hello!', 'Tally-Ho!', 'HOWDY!']
starter_jokes = ['You\'re mom\'s so fat, a wall containing her broke down!', 'You suck!', 'You smell like farts.']

def update_joke(joke_message): # add joke to db function
  if "jokes" in db.keys():
    jokes = db["jokes"]
    jokes.append(joke_message)
    db["jokes"] = jokes
  else:
    db["jokes"] = [joke_message]

def delete_joke(index): # delete joke in db function
  jokes = db["jokes"]
  if len(jokes) > index:
    del jokes[index]
    db["jokes"] = jokes

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
  
  if msg.startswith('-hello'): # The greetings command
    # await allows to wait for message to be received
    await message.channel.send(random.choice(greetings))

  # Have starter jokes and jokes in db together
  options = starter_jokes
  if "jokes" in db.keys():
    options = options + list(db["jokes"])
  print(db["jokes"])

  if msg.startswith('-help'): # Gives documentations
    await message.channel.send('Commands for Not Funny Bot: \n -joke : Robot gives joke \n -new_joke : Add new joke to bot\'s database \n -del_joke : Delete joke stored in bot\'s database')

  if msg.startswith('-joke'): # The "joke" command
    # await allows to wait for message to be received
    await message.channel.send(random.choice(options))
  
  if msg.startswith("-new_joke"): # adding new joke from discord server
    joke_message = msg.split("-new_joke", 1)[1] # take off "-new_joke" from message
    update_joke(joke_message) # add joke to db using function
    await message.channel.send("New joke added")

  if msg.startswith("-del_joke"): # delete joke command from discord server
    jokes = []
    if "jokes" in db.keys():
      index = int(msg.split("-del_joke", 1)[1]) # Get index and convert it to int
      delete_joke(index) # delete joke in db using function
      jokes = db["jokes"]

      listOfJokesString = ""
      for i in range(len(db["jokes"])):
        if (len(listOfJokesString) + len(str(i + 1) + ". " + db["jokes"][i]) <= 2000):
          listOfJokesString = listOfJokesString + str(i + 1) + ". " + db["jokes"][i] + "\n"
        else: # Clean comment after character limit is reached
          await message.channel.send(listOfJokesString)
          listOfJokesString = ""
          listOfJokesString = listOfJokesString + str(i + 1) + ". " + db["jokes"][i] + "\n"

      await message.channel.send(listOfJokesString) # Send list of jokes as message

keep_alive()
client.run(os.environ['TOKEN']) # Run bot using private token
