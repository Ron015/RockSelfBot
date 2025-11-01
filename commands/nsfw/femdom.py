import discord
import requests
from discord.ext import commands

@commands.command(
    name="femdom",
    help="Sends an NSFW femdom image (⚠️ Use responsibly)"
)
async def femdom(ctx):
    """Sends an NSFW femdom image (⚠️ Use responsibly)"""
    try:
        response = requests.get("https://nekobot.xyz/api/image?type=femdom")
        data = response.json()
        await ctx.send(data["message"])
    except Exception as e:
        await ctx.send(f"❌ Failed to fetch image.\n`{e}`", delete_after=10)

femdom.category = "nsfw"

async def setup(bot):
    bot.add_command(femdom)
