import discord
from discord.ext import commands

async def setup(bot):
    @bot.command(
        help="Delete bot messages from DMs.\nUsage: cleardm <1-100>"
    )
    async def cleardm(ctx, amount: str = "1"):
        if not amount.isdigit() or not (1 <= int(amount) <= 100):
            await ctx.send("❌ Usage: {ctx.prefix}cleardm <1-100>", delete_after=5)
            return

        if not isinstance(ctx.channel, discord.DMChannel):
            await ctx.send("❌ This command can only be used in DMs.", delete_after=5)
            return

        amount = int(amount)
        deleted = 0

        async for msg in ctx.channel.history(limit=amount):
            if msg.author == bot.user:
                try:
                    await msg.delete()
                    deleted += 1
                except discord.Forbidden:
                    pass

        await ctx.send(f"✅ Cleared {deleted} bot message(s).", delete_after=5)
