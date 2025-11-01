import discord
from discord.ext import commands
import time
import asyncio

async def setup(bot):
    @bot.command(aliases=["logout"])
    async def shutdown(ctx):
        msg = await ctx.send("Shutting down...")
        await asyncio.sleep(2)
        await msg.delete()
        await bot.close()
        