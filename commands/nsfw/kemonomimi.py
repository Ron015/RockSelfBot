import discord
import requests
from discord.ext import commands

@commands.command(
    name="kemonomimi",
    help="Sends an NSFW kemonomimi image (⚠️ Use responsibly)"
)
async def kemonomimi(ctx):
    """Sends an NSFW kemonomimi image (⚠️ Use responsibly)"""
    try:
        response = requests.get("https://nekobot.xyz/api/image?type=kemonomimi")
        data = response.json()
        await ctx.send(data["message"])
    except Exception as e:
        await ctx.send(f"❌ Failed to fetch image.\n`{e}`", delete_after=10)

kemonomimi.category = "nsfw"

async def setup(bot):
    bot.add_command(kemonomimi)
