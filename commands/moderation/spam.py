import discord
from discord.ext import commands
import asyncio

async def setup(bot):
    @bot.command(
        help="Spam a message a number of times (1-9).\nUsage: spam <amount> <message>"
    )
    async def spam(ctx, amount: int = 1, *, message: str = "Hello"):
        if not 1 <= amount <= 9:
            await ctx.send("❌ Amount must be between 1 and 9.", delete_after=5)
            return

        for _ in range(amount):
            await ctx.send(message)
            await asyncio.sleep(0.1)

    # 🔥 Add error handler for the spam command
    @spam.error
    async def spam_error(ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send("❌ Invalid number! Usage: `spam <amount 1-9> <message>`", delete_after=7)
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("⚠️ Missing message or amount! Try: `spam 3 hello`", delete_after=7)
        else:
            await ctx.send(f"⚠️ Unexpected error: `{error}`", delete_after=7)