import discord
import requests
from discord.ext import commands

@commands.command(
    name="waifu",
    help="Sends an NSFW waifu image (⚠️ Use responsibly)"
)
async def waifu(ctx):
    """Sends an NSFW waifu image (⚠️ Use responsibly)"""
    try:
        response = requests.get("https://nekobot.xyz/api/image?type=waifu")
        data = response.json()
        await ctx.send(data["message"])
    except Exception as e:
        await ctx.send(f"❌ Failed to fetch image.\n`{e}`", delete_after=10)

waifu.category = "nsfw"

async def setup(bot):
    bot.add_command(waifu)
