import nextcord
from nextcord import Intents
from nextcord.ext import commands
import asyncio

client = commands.Bot(command_prefix='!', intents=Intents.all())
client.remove_command('help')


@client.event
async def on_ready():
    print("Бот запущен!")
    client.load_extension("cogs.test")


client.run(DISCORD_TOKEN)
