import discord
import random
from discord.ext import commands

async def setup(bot):
    @bot.command(help="❤️ Calculate love compatibility between two users")
    async def love(ctx, user1: discord.User = None, user2: discord.User = None):
        if user1 and user2:
            love_percentage = random.randint(0, 100)
            await ctx.send(f"❤️ **{user1.name}** and **{user2.name}** have a {love_percentage}% love compatibility!")
        elif user1:
            love_percentage = random.randint(0, 100)
            await ctx.send(f"❤️ **{ctx.author.name}** and **{user1.name}** have a {love_percentage}% love compatibility!")
        else:
            await ctx.send("❗ Please mention at least one user to calculate love percentage!", delete_after=5)
