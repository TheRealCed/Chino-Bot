import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random

async def ex(args, message, client, invoke):
	await client.send_message(message.channel, "test")
