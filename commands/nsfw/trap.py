import discord
import requests
from discord.ext import commands

@commands.command(
    name="trap",
    help="Sends an NSFW trap image (⚠️ Use responsibly)"
)
async def trap(ctx):
    """Sends an NSFW trap image (⚠️ Use responsibly)"""
    try:
        response = requests.get("https://nekobot.xyz/api/image?type=trap")
        data = response.json()
        await ctx.send(data["message"])
    except Exception as e:
        await ctx.send(f"❌ Failed to fetch image.\n`{e}`", delete_after=10)

trap.category = "nsfw"

async def setup(bot):
    bot.add_command(trap)
