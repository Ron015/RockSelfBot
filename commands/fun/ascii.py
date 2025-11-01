import discord
import pyfiglet
from discord.ext import commands

async def setup(bot):
    @bot.command()
    async def ascii(ctx, *, message: str = None):
        """
        Convert text to ASCII art
        Usage: {prefix}ascii <text>
        Example: {prefix}ascii Hello
        """
        if not message:
            await ctx.send(f"`{ctx.prefix}ascii <message>`", delete_after=5)
            return
            
        art = pyfiglet.figlet_format(message)
        await ctx.send(f"```\n{art}\n```")