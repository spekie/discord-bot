import requests
import inspect

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
        Hi **{interaction.user}**.
    """))

client.run('INSERT YOUR DISCORD BOT TOKEN HERE')
