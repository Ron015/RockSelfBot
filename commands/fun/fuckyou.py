import discord
import asyncio
from discord.ext import commands


async def setup(bot):

    @bot.command(help="Send animated 'fuck you' message")
    async def fuckyou(ctx):
        msg = await ctx.send("F")
        for word in ["FU", "FUC", "FUCK", "FUCK Y", "FUCK YO", "FUCK YOU"]:
            await asyncio.sleep(0.5)
            await msg.edit(content=word)
