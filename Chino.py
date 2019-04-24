import discord
import os
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random

Client = discord.Client()
client = commands.Bot(command_prefix = "ck!")

@client.event
async def on_ready():
	print("Bot is ready!")
	print("Logged in as")
	print(client.user.name)
	print("with a UserID of")
	print(client.user.id)
	await client.change_presence(game=discord.Game(name="Making Coffee! x3 (ck!)"))

@client.event
async def on_message(message):
	if message.content.startswith("a"):
		await client.send_message(message.channel, "ur all gay")
@client.event
async def on_message(message):
	if message.content.startswith("ck!cuddle"):
		await client.send_message(message.channel, random.choice(["Stop..", "T-That.. feels good...", "Why do you.. do this?", "Umm.. Why don't y-you cuddle C-Cocoa-san?", "I-I'm sorry.. I don't want that right n-now....", "Oh.. T-That surprised me...", "W-Why me..? I'm not much...", "I liked that.. Can you p-please do more??", "*blushes* I love it when y-you c-cuddle me..", "J-Just... no... sorry."]))
	elif message.content.startswith("ck!kiss"):
		await client.send_message(message.channel, random.choice(["I d-don't think you're supposed t-to do that...", "What, umm...", "You c-can't.. do that...", "C-Can you not do that.. Thanks.", "I'm very uncomfortable... ", "W-Why.. Why did you p-pick me for that?! You could have asked Cocoa-san..", "What... umm. thanks? You're embarrasing me.. *blushes*", "Oh.. Y-You love me that much?", "I.. I enjoyed that.. *blushes*", "I-I love that...... <3", "Please stop...", "I don't want you to do that!!", "C-Can you please stop?!", "W-Why..?"]))
	elif message.content.startswith("ck!help"):
		await client.send_message(message.channel, "Chino Kafuu bot\n\nPrefix: ck!\n\nCommands:\n\nck!cuddle - Cuddle Chino-Chan!\nck!kiss - Kiss Chino-Chan >-<\nck!headpat - Give Chino-Chan a headpat!\nck!ask - Ask Chino-Chan something!\nck!help - Shows this message.")		
	elif message.content.startswith("ck!headpat"):
		await client.send_message(message.channel, random.choice(["Oh...", "Aww..", "I l-love it...", "P-Please continue doing that.", "T-Thanks.. It feels great..."]))
	elif message.content.startswith("abc"):
		await client.send_message(message.channel, "def")
	elif message.content.startswith("ck!ask"):
		await client.send_message(message.channel, random.choice(["Uh.. I t-think that would be a yes.", "I-I agree with that..", "Oh.. M-My answer would be a maybe. I-I'm not too sure..", "I-I approve with it..", "Y-Yes..", "I d-don't approve of it..", "No.. T-That's a no.", "N-No..", "I-I don't think so..", "My answer is a no.."]))
	elif message.content.startswith("ck!chino"):
		await client.send_file(message.channel, random.choice(["pictures/chino1, pictures/chino2"]))
client.run(str(os.environ.get("BOT_TOKEN")))
