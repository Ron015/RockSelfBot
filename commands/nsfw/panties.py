import discord
import requests
from discord.ext import commands

@commands.command(
    name="panties",
    help="Sends an NSFW panties image (⚠️ Use responsibly)"
)
async def panties(ctx):
    """Sends an NSFW panties image (⚠️ Use responsibly)"""
    try:
        response = requests.get("https://nekobot.xyz/api/image?type=panties")
        data = response.json()
        await ctx.send(data["message"])
    except Exception as e:
        await ctx.send(f"❌ Failed to fetch image.\n`{e}`", delete_after=10)

panties.category = "nsfw"

async def setup(bot):
    bot.add_command(panties)
