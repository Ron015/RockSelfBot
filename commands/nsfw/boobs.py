import discord
import requests
from discord.ext import commands

@commands.command(
    name="boobs",
    help="Sends an NSFW boobs image (⚠️ Use responsibly)"
)
async def boobs(ctx):
    """Sends an NSFW boobs image (⚠️ Use responsibly)"""
    try:
        response = requests.get("https://nekobot.xyz/api/image?type=boobs")
        data = response.json()
        await ctx.send(data["message"])
    except Exception as e:
        await ctx.send(f"❌ Failed to fetch image.\n`{e}`", delete_after=10)

boobs.category = "nsfw"

async def setup(bot):
    bot.add_command(boobs)
