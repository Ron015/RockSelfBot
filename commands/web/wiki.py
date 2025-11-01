import discord
from discord.ext import commands
import requests

async def setup(bot):
    @bot.command()
    async def wiki(ctx, *, query: str = None):
        """
        Search Wikipedia and get a summary.
        Usage: !wiki <search_term>
        Example: !wiki Python
        """
        if not query:
            await ctx.send("❗ Please provide a topic to search, e.g., `!wiki Python`", delete_after=5)
            return

        url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{query}"
        response = requests.get(url)

        if response.status_code != 200:
            await ctx.send(f"❌ No information found for '{query}'.", delete_after=5)
            return

        wiki_data = response.json()
        title = wiki_data.get("title", "N/A")
        description = wiki_data.get("extract", "No description available.")
        page_url = wiki_data.get("content_urls", {}).get("desktop", {}).get("page", "N/A")

        await ctx.send(
            f"**Wikipedia Summary for '{title}':**\n"
            f"**Description:** {description}\n"
            f"**Link:** {page_url}"
        )
