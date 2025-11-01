import requests
import discord
from discord.ext import commands

async def setup(bot):
    @bot.command(help="🤣 Fetch a random meme from Reddit")
    async def meme(ctx):
        try:
            response = requests.get("https://meme-api.com/gimme")
            response.raise_for_status()
            meme_data = response.json()

            meme_url = meme_data.get("preview")[-1]
            title = meme_data.get("title")
            subreddit = meme_data.get("subreddit")
            author = meme_data.get("author")
            ups = meme_data.get("ups")

            await ctx.send(
                f"**Meme Title:** {title}\n"
                f"**Subreddit:** r/{subreddit}\n"
                f"**Author:** u/{author}\n"
                f"**Upvotes:** {ups}\n\n{meme_url}"
            )
        except Exception as e:
            await ctx.send(f"❌ Failed to fetch meme: {str(e)}", delete_after=5)
