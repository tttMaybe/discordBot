import random
import aiohttp

async def get_reddit_image_url(sub_reddit: str):
    url = f"https://www.reddit.com/r/{sub_reddit}/hot.json?limit=100"
    headers = {'User-Agent': 'DiscordBotMemeFetcher/1.0'}
    
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            if not response.status == 200:
                return "Error with api"
            data = await response.json()
    
    posts = data['data']['children']
    images = []
    for p in posts:
        url = p['data']['url']
        
        if url.endswith(('.jpg', '.jpeg', '.png', '.gif', 'mp4', 'webm')):
            images.append(url)
    
    return random.choice(images) if images else "Try another time :("