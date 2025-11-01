import discord
from discord.ext import commands

async def setup(bot):
    @bot.command(
        help="Pushes chat up with blank lines to simulate clearing chat."
    )
    async def blank(ctx):
        try:
            await ctx.send("​\n" * 190)
        except discord.HTTPException:
            await ctx.send("❌ Could not send message. Possibly too long.")
