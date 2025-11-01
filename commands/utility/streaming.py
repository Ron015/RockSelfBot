import discord
from discord.ext import commands

async def setup(bot):
    @bot.command(help="Set your Discord bot's streaming status.")
    async def streaming(ctx, *, status: str = None):
        if not status:
            await ctx.send(f"`{ctx.prefix}streaming <status>`", delete_after=5)
            return

        await bot.change_presence(activity=discord.Streaming(name=status, url=f"https://www.twitch.tv/{status}"))
        await ctx.send(f"📽️ Streaming `{status}`", delete_after=5)
