import discord
from discord.ext import commands
import requests

async def setup(bot):
    @bot.command(help="😂 Get a random joke from the internet")
    async def joke(ctx):
        try:
            response = requests.get("https://official-joke-api.appspot.com/random_joke")
            joke_data = response.json()

            setup = joke_data.get("setup", "No setup found.")
            punchline = joke_data.get("punchline", "No punchline found.")

            await ctx.send(f"**Setup:** {setup}\n**Punchline:** {punchline}")
        except Exception as e:
            await ctx.send(f"❌ Couldn't fetch a joke: {e}", delete_after=5)
