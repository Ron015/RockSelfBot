import discord
from discord.ext import commands
import aiohttp

async def setup(bot):
    @bot.command()
    async def github(ctx, username: str):
        """Get GitHub user info"""
        url = f"https://api.github.com/users/{username}"
        
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status != 200:
                    await ctx.send("❌ User not found", delete_after=5)
                    return

                data = await response.json()

        message = f"""```js
👤 GitHub User: {data.get('login', username)}

📝 Bio        : {data.get('bio', 'No bio available.')}
📍 Location   : {data.get('location', 'N/A')}
🔗 Blog       : {data.get('blog') or 'N/A'}
🌐 Profile    : {data.get('html_url', 'N/A')}

📊 Followers  : {data.get('followers', 'N/A')}
📈 Following  : {data.get('following', 'N/A')}
📦 Public Repos: {data.get('public_repos', 'N/A')}
```"""

        await ctx.send(message)