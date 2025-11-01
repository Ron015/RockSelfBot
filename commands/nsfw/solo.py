import discord
import requests
from discord.ext import commands

@commands.command(
    name="solo",
    help="Sends an NSFW solo image (⚠️ Use responsibly)"
)
async def solo(ctx):
    """Sends an NSFW solo image (⚠️ Use responsibly)"""
    try:
        response = requests.get("https://nekobot.xyz/api/image?type=solo")
        data = response.json()
        await ctx.send(data["message"])
    except Exception as e:
        await ctx.send(f"❌ Failed to fetch image.\n`{e}`", delete_after=10)

solo.category = "nsfw"

async def setup(bot):
    bot.add_command(solo)
