import os


import time
import datetime
import discord
TOKEN = "NjkyMzQwMzY4ODI5NzEwNDA2.Xn2S0A.qCcya3tUCRWYhaDzZfUXh3YecH0"
GUILD = "Same"

client = discord.Client()

	
global startTime1, endTime1
@client.event
async def on_message(message):
	if message.content.startswith('!tc'):
		channel=message.channel
		
		today = datetime.date.today()
		someday = datetime.date(2020, 4, 14)
		diff = someday - today
		res=diff.days
		await channel.send(f'{res} days left. {21-res} have passed. Hold tight. Gonna get over soon.')

@client.event
async def on_voice_state_update(SheNoob,before,after):
	
	global startTime1,endTime1
	channel=client.get_channel(690665206136700963)

		
		
	if before.channel is None and after.channel is not None:

		startTime1=time.time()
		
	if before.channel is not None and after.channel is None:
			
		endTime1=time.time()
		se=endTime1-startTime1
		
		if se<60 :
			se=(int)(se)
			if before.channel.name=="stuff":
				await channel.send(f'Duration: {se} seconds. That was quite short eh...')

			
		else:
			min=se/60
			sec=se%60	
			if min<60:
				min=(int)(min)
				sec=(int)(sec)
				if before.channel.name=="stuff":
					await channel.send(f'Duration: {min} minutes {sec} seconds.Still not an hour.')
				# print(f'{min} minutes {sec} seconds')
			else :

				hr=min/60
				min=min%60
				hr=(int)(hr)
				min=(int)(min)
				sec=(int)(sec)
				if before.channel.name=="stuff":
					await channel.send(f'Duration: {hr} hour {min} minutes {sec} seconds. Dude its been more than an hr.')
				# print(f'{hr} hour {min} minutes {sec} seconds')
			
						
client.run(TOKEN)
