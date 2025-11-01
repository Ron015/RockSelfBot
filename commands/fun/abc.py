import discord
import asyncio
from discord.ext import commands

async def setup(bot):
    @bot.command(help="Send the alphabet in a message")
    async def abc(ctx):
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        msg = await ctx.send("A")
        for letter in alphabet[1:]:
            msg = await msg.edit(content=msg.content + letter)
            await asyncio.sleep(1)
