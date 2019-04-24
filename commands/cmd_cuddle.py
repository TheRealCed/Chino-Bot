import discord
import random

async def ex(args, message, client, invoke):
	if message.content.startswith("ck!cuddle"):
		await client.send_message(message.channel, random.choice(["Stop..", "T-That.. feels good...", "Why do you.. do this?", "Umm.. Why don't y-you cuddle C-Cocoa-san?", "I-I'm sorry.. I