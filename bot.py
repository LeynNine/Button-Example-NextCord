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


client.run("ODk5NjExMDA0MDkzMjI3MDM4.YW1SCQ.8x_XKN0OdFosn9ozhvh6xXoRP74")