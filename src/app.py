import nextcord
import os
import asyncio
from nextcord.ext import commands
from dotenv import load_dotenv



load_dotenv() # Load environment variables

token = os.getenv('DISCORD_TOKEN')

# Load default Discord intents here + read message content
intents = nextcord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='.', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot has logged in as {bot.user}')

async def load():
    for filename in os.listdir('src/cogs'):
        if filename.endswith('.py'):
            bot.load_extension(f'cogs.{filename[:-3]}') # Register all available cogs as extensions

async def main():
    if token:
        await load()
        await bot.start(token=token)
    else:
        print("Discord token not found. Please create a .env file in the project folder with the DISCORD_TOKEN key.")
        quit()

asyncio.run(main())
