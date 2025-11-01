import discord
from discord.ext import commands
import random

async def setup(bot):
    @bot.command(help="🍆 Shows a humorous randomly sized 'dick' for a user")
    async def dick(ctx, user: str = None):
        user = user or ctx.author.display_name
        size = random.randint(1, 15)
        await ctx.send(f"**{user}**'s Dick size\n8{'=' * size}D")
