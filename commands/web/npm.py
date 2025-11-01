import discord
from discord.ext import commands
import requests

async def setup(bot):
    @bot.command()
    async def npm(ctx, *, query: str = None):
        if not query:
            await ctx.send("❗ Please provide a package name to search, e.g., `!npm express`", delete_after=5)
            return

        try:
            url = f"https://registry.npmjs.org/-/v1/search?text={query}&size=1"
            response = requests.get(url, timeout=5)
            
            if response.status_code != 200:
                await ctx.send("❌ Failed to reach NPM registry. Try again later.", delete_after=5)
                return

            npm_data = response.json()

            if not npm_data.get('objects'):
                await ctx.send(f"❌ No npm package found for '{query}'.", delete_after=5)
                return

            package = npm_data['objects'][0]['package']
            name = package.get("name", "N/A")
            description = package.get("description", "No description available")
            version = package.get("version", "N/A")
            link = package.get("links", {}).get("npm", "N/A")

            # Limit description length and clean it
            if len(description) > 500:
                description = description[:497] + "..."

            msg = f"""```js
📦 NPM Package Search: {query}

🔹 Name       : {name}
🔹 Version    : {version}
📝 Description: {description}
🔗 Link       : {link}
```"""
            await ctx.send(msg)

        except Exception as e:
            await ctx.send(f"❌ Error: {str(e)}", delete_after=5)