import discord
import requests
from discord.ext import commands

@commands.command(
    name="tits",
    help="Sends an NSFW tits image (⚠️ Use responsibly)"
)
async def tits(ctx):
    """Sends an NSFW tits image (⚠️ Use responsibly)"""
    try:
        response = requests.get("https://nekobot.xyz/api/image?type=tits")
        data = response.json()
        await ctx.send(data["message"])
    except Exception as e:
        await ctx.send(f"❌ Failed to fetch image.\n`{e}`", delete_after=10)

tits.category = "nsfw"

async def setup(bot):
    bot.add_command(tits)
