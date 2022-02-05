import nextcord
from nextcord.ext import commands
from buttons.button import Confirm # import class button 
import asyncio

class Test(commands.Cog):
	
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def test(self, ctx):
		view = Confirm() # sample rename
		message = "Hello, i am testing command"
		await ctx.send(message, view=view) # add button under message

		await view.wait() # waiting answer
		if view.value is True:
			print("Agree")
			# You can add anymore action with member
		elif view.value is True:
			print("Decline")


def setup(bot): # функция
	bot.add_cog(Test(bot))
