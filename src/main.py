# https://github.com/kym2006/random.bot
# https://discordpy.readthedocs.io/en/stable/index.html

import os
from dotenv import load_dotenv
load_dotenv()
import discord
from classes.bot import Bot

token = os.getenv("DISCORD_TOKEN")
clientID = os.getenv("APP_ID")


intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
bot = Bot(
    shard_count=6,
    command_prefix='?',
    heartbeat_timeout=300,
    intents=intents,
    case_insensitive=True,
    chunk_guilds_at_startup=False,
)

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')
    channel = client.get_channel(928238195626360917)
    await channel.send("Ready to roll!")

# @client.event
# async def on_member_join(member):
#     await member.create_dm()
#     await member.dm_channel.send(
#         f'Hi {member.name}, welcome to my Discord server!'
#     )

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    await message.channel.send("test")

client.run(token)