import discord
import random
Token = ''
client = discord.Client()

@client.event

async def on_ready():
   print('We have logged in as {0.user}'.format(client))




client.run(TOKEN)

on_ready()
