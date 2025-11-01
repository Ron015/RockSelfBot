import discord
import requests
from discord.ext import commands

@commands.command(
    name="ngif",
    help="Sends an NSFW ngif image (⚠️ Use responsibly)"
)
async def ngif(ctx):
    """Sends an NSFW ngif image (⚠️ Use responsibly)"""
    try:
        response = requests.get("https://nekobot.xyz/api/image?type=ngif")
        data = response.json()
        await ctx.send(data["message"])
    except Exception as e:
        await ctx.send(f"❌ Failed to fetch image.\n`{e}`", delete_after=10)

ngif.category = "nsfw"

async def setup(bot):
    bot.add_command(ngif)
