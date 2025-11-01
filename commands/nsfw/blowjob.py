import discord
import requests
from discord.ext import commands

@commands.command(
    name="blowjob",
    help="Sends an NSFW blowjob image (⚠️ Use responsibly)"
)
async def blowjob(ctx):
    """Sends an NSFW blowjob image (⚠️ Use responsibly)"""
    try:
        response = requests.get("https://nekobot.xyz/api/image?type=bj")
        data = response.json()
        await ctx.send(data["message"])
    except Exception as e:
        await ctx.send(f"❌ Failed to fetch image.\n`{e}`", delete_after=10)

blowjob.category = "nsfw"

async def setup(bot):
    bot.add_command(blowjob)
