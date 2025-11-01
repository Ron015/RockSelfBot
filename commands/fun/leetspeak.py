from discord.ext import commands
import discord

async def setup(bot):
    @bot.command(aliases=["leet"], help="💻 Convert your message to leetspeak")
    async def leetspeak(ctx, *, content: str = None):
        if not content:
            await ctx.send("Usage: `leetspeak <message>`", delete_after=5)
            return

        leet = (
            content
            .replace('a', '4')
            .replace('e', '3')
            .replace('i', '1')
            .replace('o', '0')
            .replace('t', '7')
            .replace('b', '8')
        )

        await ctx.send(leet)
