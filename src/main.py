import discord
import os
from dotenv import load_dotenv

from bot_client import BotClient

load_dotenv(dotenv_path="build/.env")
DISCORD_TOKEN = os.getenv("bot_token")

intents = discord.Intents.default()
intents.message_content = True

client = BotClient(intents = intents)
client.run(DISCORD_TOKEN)