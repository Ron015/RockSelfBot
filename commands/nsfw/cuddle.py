import discord
import requests
from discord.ext import commands

@commands.command(
    name="cuddle",
    help="Sends an NSFW cuddle image (⚠️ Use responsibly)"
)
async def cuddle(ctx):
    """Sends an NSFW cuddle image (⚠️ Use responsibly)"""
    try:
        response = requests.get("https://nekobot.xyz/api/image?type=cuddle")
        data = response.json()
        await ctx.send(data["message"])
    except Exception as e:
        await ctx.send(f"❌ Failed to fetch image.\n`{e}`", delete_after=10)

cuddle.category = "nsfw"

async def setup(bot):
    bot.add_command(cuddle)
