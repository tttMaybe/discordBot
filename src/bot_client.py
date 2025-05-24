import discord
from memes import get_reddit_cat_url

class BotClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith("!cat"):
            response = await get_reddit_cat_url()
            await message.channel.send(response)