import discord
import requests
from discord.ext import commands

@commands.command(
    name="cum",
    help="Sends an NSFW cum image (⚠️ Use responsibly)"
)
async def cum(ctx):
    """Sends an NSFW cum image (⚠️ Use responsibly)"""
    try:
        response = requests.get("https://nekobot.xyz/api/image?type=cum")
        data = response.json()
        await ctx.send(data["message"])
    except Exception as e:
        await ctx.send(f"❌ Failed to fetch image.\n`{e}`", delete_after=10)

cum.category = "nsfw"

async def setup(bot):
    bot.add_command(cum)
