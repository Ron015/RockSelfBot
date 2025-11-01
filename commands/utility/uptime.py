import discord
from discord.ext import commands
import datetime
start_time = datetime.datetime.now()
# Make sure `start_time` is defined globally somewhere in your bot script like:
# start_time = datetime.datetime.now()

async def setup(bot):
    @bot.command(help="Show how long the bot has been running.")
    async def uptime(ctx):
        delta = datetime.datetime.now() - start_time
        hours, remainder = divmod(int(delta.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)
        days, hours = divmod(hours, 24)
        uptime_str = f"{days}d {hours}h {minutes}m {seconds}s"
        await ctx.send(f"Uptime: `{uptime_str}`")
