import discord
from discord.ext import commands
import time

async def setup(bot):
    @bot.command(aliases=['uicon'])
    async def usericon(ctx, user: discord.User = None):
        if not user:
            await ctx.send(f"`{bot.command_prefix}usericon <@user>`", delete_after=5)
            return
        avatar_url = user.avatar.url if user.avatar else user.default_avatar.url
        await ctx.send(f"{user.mention}'s avatar:\n{avatar_url}")
