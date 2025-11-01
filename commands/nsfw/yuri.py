import discord
import requests
from discord.ext import commands

@commands.command(
    name="yuri",
    help="Sends an NSFW yuri image (⚠️ Use responsibly)"
)
async def yuri(ctx):
    """Sends an NSFW yuri image (⚠️ Use responsibly)"""
    try:
        response = requests.get("https://nekobot.xyz/api/image?type=yuri")
        data = response.json()
        await ctx.send(data["message"])
    except Exception as e:
        await ctx.send(f"❌ Failed to fetch image.\n`{e}`", delete_after=10)

yuri.category = "nsfw"

async def setup(bot):
    bot.add_command(yuri)
