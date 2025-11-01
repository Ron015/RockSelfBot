import discord
from discord.ext import commands

async def setup(bot):
    @bot.command(help="Set your Discord bot's playing status.")
    async def playing(ctx, *, status: str = None):
        if not status:
            await ctx.send(f"`playing <status>`", delete_after=5)
            return
        
        await bot.change_presence(activity=discord.Game(name=status))
        await ctx.send(f"🎮 Playing `{status}`", delete_after=5)