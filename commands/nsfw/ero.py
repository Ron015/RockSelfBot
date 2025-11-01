import discord
import requests
from discord.ext import commands

@commands.command(
    name="ero",
    help="Sends an NSFW ero image (⚠️ Use responsibly)"
)
async def ero(ctx):
    """Sends an NSFW ero image (⚠️ Use responsibly)"""
    try:
        response = requests.get("https://nekobot.xyz/api/image?type=ero")
        data = response.json()
        await ctx.send(data["message"])
    except Exception as e:
        await ctx.send(f"❌ Failed to fetch image.\n`{e}`", delete_after=10)

ero.category = "nsfw"

async def setup(bot):
    bot.add_command(ero)
