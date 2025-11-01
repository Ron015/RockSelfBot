import discord
import requests
from discord.ext import commands

@commands.command(
    name="bj",
    help="Sends an NSFW bj image (⚠️ Use responsibly)"
)
async def bj(ctx):
    """Sends an NSFW bj image (⚠️ Use responsibly)"""
    try:
        response = requests.get("https://nekobot.xyz/api/image?type=bj")
        data = response.json()
        await ctx.send(data["message"])
    except Exception as e:
        await ctx.send(f"❌ Failed to fetch image.\n`{e}`", delete_after=10)

bj.category = "nsfw"

async def setup(bot):
    bot.add_command(bj)
