import discord
import requests
from discord.ext import commands

@commands.command(
    name="lewd",
    help="Sends an NSFW lewd image (⚠️ Use responsibly)"
)
async def lewd(ctx):
    """Sends an NSFW lewd image (⚠️ Use responsibly)"""
    try:
        response = requests.get("https://nekobot.xyz/api/image?type=lewd")
        data = response.json()
        await ctx.send(data["message"])
    except Exception as e:
        await ctx.send(f"❌ Failed to fetch image.\n`{e}`", delete_after=10)

lewd.category = "nsfw"

async def setup(bot):
    bot.add_command(lewd)
