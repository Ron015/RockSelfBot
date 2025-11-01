import discord
import requests
from discord.ext import commands

@commands.command(
    name="pussy",
    help="Sends an NSFW pussy image (⚠️ Use responsibly)"
)
async def pussy(ctx):
    """Sends an NSFW pussy image (⚠️ Use responsibly)"""
    try:
        response = requests.get("https://nekobot.xyz/api/image?type=pussy")
        data = response.json()
        await ctx.send(data["message"])
    except Exception as e:
        await ctx.send(f"❌ Failed to fetch image.\n`{e}`", delete_after=10)

pussy.category = "nsfw"

async def setup(bot):
    bot.add_command(pussy)
