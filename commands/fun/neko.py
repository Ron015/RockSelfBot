import discord
import requests
from discord.ext import commands

@commands.command(
    name="neko",
    help="Sends a fun neko response"
)
async def neko(ctx):
    """Sends a fun neko response"""
    try:
        response = requests.get("https://nekobot.xyz/api/image?type=neko")
        data = response.json()
        await ctx.send(data["message"])
    except Exception as e:
        await ctx.send(f"❌ Failed to fetch content.\n`{e}`", delete_after=10)

neko.category = "fun"

async def setup(bot):
    bot.add_command(neko)
