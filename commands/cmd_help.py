import random
import discord

async def ex(args, message, client, invoke):
	if message.content.startswith("ck!help"):
		await client.send_message(message.channel, "Chino Kafuu bot\n\nPrefix: ck!\n\nCommands:\n\nck!cuddle - Cuddle Chino-Chan!\nck!kiss - Kiss Chino-Chan >-<\nck!headpat - Give Chino-Chan a headpat!\nck!ask - Ask Chino-Chan something!\nck!help - Shows this message.")	