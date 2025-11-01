import discord
from discord.ext import commands
import time

async def setup(bot):
    @bot.command(aliases=['hide'])
    async def hidemention(ctx, *, content: str = None):
        if not content:
            await ctx.send(f"`{bot.command_prefix}hidemention <message>`", delete_after=5)
            return
        await ctx.send(content + ('||\u200b||' * 200) + '@everyone')
