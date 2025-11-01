import discord
import requests
from discord.ext import commands

@commands.command(
    name="thigh",
    help="Sends an NSFW thigh image (⚠️ Use responsibly)"
)
async def thigh(ctx):
    """Sends an NSFW thigh image (⚠️ Use responsibly)"""
    try:
        response = requests.get("https://nekobot.xyz/api/image?type=thigh")
        data = response.json()
        await ctx.send(data["message"])
    except Exception as e:
        await ctx.send(f"❌ Failed to fetch image.\n`{e}`", delete_after=10)

thigh.category = "nsfw"

async def setup(bot):
    bot.add_command(thigh)
