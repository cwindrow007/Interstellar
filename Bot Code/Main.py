import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# Loader for environment variables

load_dotenv()
BOT_TOKEN = os.getenv('TOKEN')

# Bot setup
intents = discord.Intents.default()
intents.messages = True #Message Tracking
intents.message_content = True #Reading Message content

bot = commands.Bot(command_prefix='/', intents=intents)

# Event: Bot is ready

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")

# Error handling

# Load Extensions

#loader
if __name__ == '__main__':
    bot.run(BOT_TOKEN)

