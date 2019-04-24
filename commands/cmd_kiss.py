import random
import discord

async def ex(args, message, client, invoke):
	if message.content.startswith("ck!kiss"):
		await client.send_message(message.channel, random.choice(["I d-don't think you're supposed t-to do that...", "What, umm...", "You c-can't.. do that...", "C-Can you not do that.. Thanks.", "I'm very uncomfortable... ", "W-Why.. Why did you p-pick me for that?! You could have asked Cocoa-san..", "What... umm. thanks? You're embarrasing me.. *blushes*", "Oh.. Y-You love me that much?", "I.. I enjoyed that.. *blushes*", "I-I love that...... <3", "Please stop...", "I don't want you to do that!!", "C-Can you please stop?!", "W-Why..?"]))