import discord
from discord.ext import commands

async def setup(bot):
    @bot.command(aliases=["stopstreaming", "stopstatus", "stoplistening", "stopplaying", "stopwatching"], help="Stop any current activity and set status to DND.")
    async def stopactivity(ctx):
        await bot.change_presence(activity=None, status=discord.Status.dnd)
        await ctx.send("🛑 Activity stopped, status set to Do Not Disturb.", delete_after=5)
