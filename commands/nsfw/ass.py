import discord
import requests
from discord.ext import commands

@commands.command(
    name="ass",
    help="Sends an NSFW ass image (⚠️ Use responsibly)"
)
async def ass(ctx):
    """Sends an NSFW ass image (⚠️ Use responsibly)"""
    try:
        response = requests.get("https://nekobot.xyz/api/image?type=ass")
        data = response.json()
        await ctx.send(data["message"])
    except Exception as e:
        await ctx.send(f"❌ Failed to fetch image.\n`{e}`", delete_after=10)

ass.category = "nsfw"

async def setup(bot):
    bot.add_command(ass)
