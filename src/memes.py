import random
import aiohttp

async def get_reddit_cat_url():
    url = "https://www.reddit.com/r/cats/hot.json?limit=100"
    headers = {'User-Agent': 'DiscordBotMemeFetcher/1.0'}
    
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            data = await response.json()
    
    posts = data['data']['children']
    images = []
    for p in posts:
        url = p['data']['url']
        
        if url.endswith(('.jpg', '.jpeg', '.png', '.gif')):
            images.append(url)
    
    return random.choice(images) if images else "Try another time :("