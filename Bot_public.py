import discord
import time
import Pathfinder
import re
from datetime import date as d
import Captions


client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    global list
    if message.author == client.user:
        return




    if re.match(r'[s|S][e|E][n|N][d|D] [m|M].+',message.content) or re.match(r'sawaw puas',message.content) is not None:



        date = re.findall(r'[a-zA-Z]+ (\d+)', message.content)
        if re.search('[T|t]oday',message.content) != None:
            date = d.today().strftime('%Y%m%d')
        if type(date) is not str:
            list = Pathfinder.getpath(date[0])
        else:
            list = Pathfinder.getpath(date)
        i = 0
        while i < len(list):
            with open('iisc.ugmemes\\'+list[i],'rb') as file:
                meme = discord.File(file)
                await message.channel.send(file=meme)
                date_time = list[i].replace('.jpg','')

                await message.channel.send(Captions.caption(date_time))
                time.sleep(1)
            i= i + 1


client.run('Token')