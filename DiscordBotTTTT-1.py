import discord
import random
TOKEN = 'OTYyNDAzODQwOTc4NzMxMDE5.YlHCbA.IJW2swfXMkziRb8kQUxZsv4wtLo'

client = discord.Client()

@client.event

async def on_ready():
   print('We have logged in as {0.user}'.format(client))




client.run(TOKEN)

on_ready()
