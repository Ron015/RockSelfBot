import discord
import requests
from discord.ext import commands

@commands.command(
    name="classic",
    help="Sends an NSFW classic image (⚠️ Use responsibly)"
)
async def classic(ctx):
    """Sends an NSFW classic image (⚠️ Use responsibly)"""
    try:
        response = requests.get("https://nekobot.xyz/api/image?type=classic")
        data = response.json()
        await ctx.send(data["message"])
    except Exception as e:
        await ctx.send(f"❌ Failed to fetch image.\n`{e}`", delete_after=10)

classic.category = "nsfw"

async def setup(bot):
    bot.add_command(classic)
