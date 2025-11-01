import discord
import requests
from discord.ext import commands

@commands.command(
    name="nsfw_neko_gif",
    help="Sends an NSFW nsfw_neko_gif image (⚠️ Use responsibly)"
)
async def nsfw_neko_gif(ctx):
    """Sends an NSFW nsfw_neko_gif image (⚠️ Use responsibly)"""
    try:
        response = requests.get("https://nekobot.xyz/api/image?type=nsfw_neko_gif")
        data = response.json()
        await ctx.send(data["message"])
    except Exception as e:
        await ctx.send(f"❌ Failed to fetch image.\n`{e}`", delete_after=10)

nsfw_neko_gif.category = "nsfw"

async def setup(bot):
    bot.add_command(nsfw_neko_gif)
