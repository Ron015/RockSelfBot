import discord
import requests
from discord.ext import commands

@commands.command(
    name="feet",
    help="Sends an NSFW feet image (⚠️ Use responsibly)"
)
async def feet(ctx):
    """Sends an NSFW feet image (⚠️ Use responsibly)"""
    try:
        response = requests.get("https://nekobot.xyz/api/image?type=feet")
        data = response.json()
        await ctx.send(data["message"])
    except Exception as e:
        await ctx.send(f"❌ Failed to fetch image.\n`{e}`", delete_after=10)

feet.category = "nsfw"

async def setup(bot):
    bot.add_command(feet)
