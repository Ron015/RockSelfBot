import discord
from discord.ext import commands
import requests

async def setup(bot):
    @bot.command()
    async def quotes(ctx, category: str = None):
        base_url = "https://hindi-quotes.vercel.app/random"
        valid_cats = {"motivational", "positive", "attitude", "love", "sad", "success"}

        if category and category.lower() in valid_cats:
            api_url = f"{base_url}/{category.lower()}"
        else:
            api_url = base_url
            category = None  # reset to None if invalid category given

        try:
            response = requests.get(api_url, timeout=10)
            response.raise_for_status()
            data = response.json()
        except (requests.RequestException, ValueError):
            await ctx.send("⚠️ Quote laane me dikkat aa gayi, zara phir try karo!", delete_after=5)
            return

        quote_type = data.get("type", "Unknown")
        quote_text = data.get("quote", "No quote available at the moment.")

        await ctx.send(f"```js\nTYPE: {quote_type.title()}\n{quote_text}\n```")
