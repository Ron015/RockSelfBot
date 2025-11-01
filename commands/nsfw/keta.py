import discord
import requests
from discord.ext import commands

@commands.command(
    name="keta",
    help="Sends an NSFW keta image (⚠️ Use responsibly)"
)
async def keta(ctx):
    """Sends an NSFW keta image (⚠️ Use responsibly)"""
    try:
        response = requests.get("https://nekobot.xyz/api/image?type=keta")
        data = response.json()
        await ctx.send(data["message"])
    except Exception as e:
        await ctx.send(f"❌ Failed to fetch image.\n`{e}`", delete_after=10)

keta.category = "nsfw"

async def setup(bot):
    bot.add_command(keta)
