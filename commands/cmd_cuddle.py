import discord
import random

async def ex(args, message, client, invoke):
	await client.send_message(message.channel, random.choice(["Stop..", "T-That.. feels good...", "Why do you.. do this?", "Umm.. Why don't y-you cuddle C-Cocoa-san?", "I-I'm sorry.. I don't want that right n-now....", "Oh.. T-That surprised me...", "W-Why me..? I'm not much...", "I liked that.. Can you p-please do more??", "*blushes* I love it when y-you c-cuddle me..", "J-Just... no... sorry."]))
