import nextcord

class Confirm(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None

    @nextcord.ui.button(label="Agree", style=nextcord.ButtonStyle.danger) # Yep here
    async def confirm(self,button: nextcord.ui.Button, interaction: nextcord.Interaction):
        self.value = True
        self.stop()

    @nextcord.ui.button(label="Decline", style=nextcord.ButtonStyle.blurple) # And here
    async def cancel(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        self.value = False
        self.stop()


"""
ButtonStyle.blurple
ButtonStyle.danger
ButtonStyle.gray
ButtonStyle.green
ButtonStyle.grey
ButtonStyle.link
ButtonStyle.primary
ButtonStyle.red
ButtonStyle.secondary
ButtonStyle.success

You can use this colors in 24 line
"""
