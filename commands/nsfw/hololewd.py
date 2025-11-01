import discord
import requests
from discord.ext import commands

@commands.command(
    name="hololewd",
    help="Sends an NSFW hololewd image (⚠️ Use responsibly)"
)
async def hololewd(ctx):
    """Sends an NSFW hololewd image (⚠️ Use responsibly)"""
    try:
        response = requests.get("https://nekobot.xyz/api/image?type=hololewd")
        data = response.json()
        await ctx.send(data["message"])
    except Exception as e:
        await ctx.send(f"❌ Failed to fetch image.\n`{e}`", delete_after=10)

hololewd.category = "nsfw"

async def setup(bot):
    bot.add_command(hololewd)
