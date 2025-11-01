import discord
import requests
from discord.ext import commands

@commands.command(
    name="les",
    help="Sends an NSFW les image (⚠️ Use responsibly)"
)
async def les(ctx):
    """Sends an NSFW les image (⚠️ Use responsibly)"""
    try:
        response = requests.get("https://nekobot.xyz/api/image?type=les")
        data = response.json()
        await ctx.send(data["message"])
    except Exception as e:
        await ctx.send(f"❌ Failed to fetch image.\n`{e}`", delete_after=10)

les.category = "nsfw"

async def setup(bot):
    bot.add_command(les)
