import discord
from discord.ext import commands
import requests

async def setup(bot):
    @bot.command()
    async def fact(ctx):
        try:
            response = requests.get("https://uselessfacts.jsph.pl/api/v2/facts/random", timeout=5)
            if response.status_code != 200:
                await ctx.send("❌ Couldn't fetch a fact right now. Try again later.", delete_after=5)
                return

            data = response.json()
            fact_text = data.get("text", "No fact found.")
        except Exception as e:
            await ctx.send(f"❌ Error: {str(e)}", delete_after=5)
            return

        await ctx.send(f"💡 **Fact:** {fact_text}")
