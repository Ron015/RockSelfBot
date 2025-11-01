import discord
import requests
from discord.ext import commands

@commands.command(
    name="boobs_gif",
    help="Sends an NSFW boobs_gif image (⚠️ Use responsibly)"
)
async def boobs_gif(ctx):
    """Sends an NSFW boobs_gif image (⚠️ Use responsibly)"""
    try:
        response = requests.get("https://nekobot.xyz/api/image?type=boobs_gif")
        data = response.json()
        await ctx.send(data["message"])
    except Exception as e:
        await ctx.send(f"❌ Failed to fetch image.\n`{e}`", delete_after=10)

boobs_gif.category = "nsfw"

async def setup(bot):
    bot.add_command(boobs_gif)
