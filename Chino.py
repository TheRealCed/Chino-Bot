import discord
import os
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from commands import cmd_cuddle, cmd_help, cmd_kiss

Client = discord.Client()

commands = {

	"kiss": cmd_kiss,
	"cuddle": cmd_cuddle,
	"help": cmd_help,
	"headpat": cmd_headpat,
	"abc": cmd_def,
	"ask": cmd_ask,
	"chino": cmd_chino,

}


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
    if message.content.startswith(STATICS.PREFIX):
        invoke = message.content[len(STATICS.PREFIX):].split(" ")[0]
        args = message.content.split(" ")[1:]
        if commands.__contains__(invoke):
            await commands.get(invoke).ex(args, message, client, invoke)
        else:
	    await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.red(), description=("The command `%s` is not valid!" % invoke)))

@client.event
async def on_message(message):
	if message.content.startswith("a"):
		await client.send_message(message.channel, "ur all gay")
@client.event
async def on_message(message):
	if message.content.startswith("ck!headpat"):
		await client.send_message(message.channel, random.choice(["Oh...", "Aww..", "I l-love it...", "P-Please continue doing that.", "T-Thanks.. It feels great..."]))
	elif message.content.startswith("abc"):
		await client.send_message(message.channel, "def")
	elif message.content.startswith("ck!ask"):
		await client.send_message(message.channel, random.choice(["Uh.. I t-think that would be a yes.", "I-I agree with that..", "Oh.. M-My answer would be a maybe. I-I'm not too sure..", "I-I approve with it..", "Y-Yes..", "I d-don't approve of it..", "No.. T-That's a no.", "N-No..", "I-I don't think so..", "My answer is a no.."]))
	elif message.content.startswith("ck!chino"):
		await client.send_file(message.channel, random.choice(["pictures/chino1, pictures/chino2"]))
client.run(str(os.environ.get("BOT_TOKEN")))
