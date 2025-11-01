import discord
import asyncio
from discord.ext import commands

async def setup(bot):
    @bot.command(help="Count to 100 in a message")
    async def count(ctx):
        msg = await ctx.send("0")
        for i in range(1, 101):
            await msg.edit(content=str(i))
            await asyncio.sleep(1)
