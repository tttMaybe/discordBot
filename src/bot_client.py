import discord
from memes import get_reddit_image_url
from time_commands import city_time
from weather import get_weather_embed_current, get_weather_embed_forecast

class BotClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        if message.author == self.user or len(message.content) > 100:
            return
        
        command_parts = message.content[1:].split(' ')
        command_name = command_parts[0].lower()
        

        match command_name:
            case "cat":
                if len(command_parts) > 1:
                    return
                response = await get_reddit_image_url("cats")
                await message.channel.send(response)
            case "fun":
                if len(command_parts) > 1:
                    return
                response = await get_reddit_image_url("FunnyAnimals")
                await message.channel.send(response)
            case "еж":
                if len(command_parts) > 1:
                    return
                response = await get_reddit_image_url("Hedgehogs")
                while "65c1eqlnyp3f1" in response:
                    response = await get_reddit_image_url("Hedgehogs")
                await message.channel.send(response)
            case "time":
                if len(command_parts) > 1:
                    return
                response = await city_time()
                await message.channel.send(response)
            case "pfp":
                if len(command_parts) > 2:
                    return
                if message.mentions:
                    target_user = message.mentions[0]
                else:
                    target_user = message.author
                await message.channel.send(target_user.display_avatar.url)
            case "temp":
                if len(command_parts) != 2:
                    return
                weather_response = get_weather_embed_current(command_parts[1])
                embed = discord.Embed.from_dict(weather_response)
                await message.channel.send(embed=embed)
            case "fore":
                if len(command_parts) != 2:
                    return
                weather_response = get_weather_embed_forecast(command_parts[1], 3)
                embed = discord.Embed.from_dict(weather_response)
                await message.channel.send(embed=embed)
            case _:
                pass