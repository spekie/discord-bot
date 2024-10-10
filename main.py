import requests
import inspect
import sys

from discord import app_commands, Intents, Client, Interaction

class client(Client):
    def __init__(self, *, intents: Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self) -> None:
        await self.tree.sync()

client = client(intents=Intents.none())

@client.event
async def on_ready():
    print(inspect.cleandoc(f"""
        Bot name: {client.user}
		Bot ID: {client.user.id}

		Invite link below
        https://discord.com/api/oauth2/authorize?client_id={client.user.id}&scope=applications.commands%20bot
    """), end="\n\n")


@client.tree.command()
async def hello(interaction: Interaction):
    """ Wow you read this? """

    print(f"> {interaction.user} used the /hello command.")

    await interaction.response.send_message(inspect.cleandoc(f"""
        Hi **{interaction.user}**, this bot is still under development by the big brain, slightly lazy, extremely unpythonic developer by the name of spekies.
	Oh yeah he also has a website at https://spekie.org so that's cool.
    """))

client.run('INSERT YOUR DISCORD BOT TOKEN HERE')
