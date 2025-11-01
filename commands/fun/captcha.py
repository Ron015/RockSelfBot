import discord
import requests
from discord.ext import commands

async def setup(bot):

    @bot.command(help="Fake CAPTCHA of user")
    async def captcha(ctx, user: discord.Member = None):
        if not user:
            await ctx.send("❌ Please mention a user.")
            return

        response = requests.get(f"https://nekobot.xyz/api/imagegen?type=captcha&url={user.display_avatar.url}&username={user.name}")
        data = response.json()
        await ctx.send(data["message"])
