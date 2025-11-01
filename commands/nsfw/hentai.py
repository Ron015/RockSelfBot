import discord
import requests
from discord.ext import commands

@commands.command(
    name="hentai",
    help="Sends an NSFW hentai image (⚠️ Use responsibly)"
)
async def hentai(ctx):
    """Sends an NSFW hentai image (⚠️ Use responsibly)"""
    try:
        response = requests.get("https://nekobot.xyz/api/image?type=hentai")
        data = response.json()
        await ctx.send(data["message"])
    except Exception as e:
        await ctx.send(f"❌ Failed to fetch image.\n`{e}`", delete_after=10)

hentai.category = "nsfw"

async def setup(bot):
    bot.add_command(hentai)
