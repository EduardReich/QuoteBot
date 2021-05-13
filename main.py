import discord
import os
import random
from arrays import nimeniCelebru

my_secret = os.environ['token']


client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))
  
@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('citat'):
    await message.channel.send(random.choice(nimeniCelebru))



client.run(my_secret)