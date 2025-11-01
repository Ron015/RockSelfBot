import discord
import requests
from discord.ext import commands

@commands.command(
    name="ahegao",
    help="Sends an NSFW ahegao image (⚠️ Use responsibly)"
)
async def ahegao(ctx):
    """Sends an NSFW ahegao image (⚠️ Use responsibly)"""
    try:
        response = requests.get("https://nekobot.xyz/api/image?type=ahegao")
        data = response.json()
        await ctx.send(data["message"])
    except Exception as e:
        await ctx.send(f"❌ Failed to fetch image.\n`{e}`", delete_after=10)

ahegao.category = "nsfw"

async def setup(bot):
    bot.add_command(ahegao)
