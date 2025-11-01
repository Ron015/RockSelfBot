import discord
import requests
from discord.ext import commands

@commands.command(
    name="anal",
    help="Sends an NSFW anal image (⚠️ Use responsibly)"
)
async def anal(ctx):
    """Sends an NSFW anal image (⚠️ Use responsibly)"""
    try:
        response = requests.get("https://nekobot.xyz/api/image?type=anal")
        data = response.json()
        await ctx.send(data["message"])
    except Exception as e:
        await ctx.send(f"❌ Failed to fetch image.\n`{e}`", delete_after=10)

anal.category = "nsfw"

async def setup(bot):
    bot.add_command(anal)
