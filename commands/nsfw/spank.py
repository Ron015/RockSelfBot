import discord
import requests
from discord.ext import commands

@commands.command(
    name="spank",
    help="Sends an NSFW spank image (⚠️ Use responsibly)"
)
async def spank(ctx):
    """Sends an NSFW spank image (⚠️ Use responsibly)"""
    try:
        response = requests.get("https://nekobot.xyz/api/image?type=spank")
        data = response.json()
        await ctx.send(data["message"])
    except Exception as e:
        await ctx.send(f"❌ Failed to fetch image.\n`{e}`", delete_after=10)

spank.category = "nsfw"

async def setup(bot):
    bot.add_command(spank)
