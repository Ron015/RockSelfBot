import discord
import requests
from discord.ext import commands

@commands.command(
    name="feetg",
    help="Sends an NSFW feetg image (⚠️ Use responsibly)"
)
async def feetg(ctx):
    """Sends an NSFW feetg image (⚠️ Use responsibly)"""
    try:
        response = requests.get("https://nekobot.xyz/api/image?type=feetg")
        data = response.json()
        await ctx.send(data["message"])
    except Exception as e:
        await ctx.send(f"❌ Failed to fetch image.\n`{e}`", delete_after=10)

feetg.category = "nsfw"

async def setup(bot):
    bot.add_command(feetg)
