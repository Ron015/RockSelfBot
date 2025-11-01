import discord
from discord.ext import commands
import time

async def setup(bot):
    @bot.command()
    async def edit(ctx, *, content: str = None):
        if not content:
            await ctx.send(f"`{ctx.prefix}edit <message>`", delete_after=5)
            return
        text = await ctx.send(content)
        await text.edit(content=f"\u202b{content}")
