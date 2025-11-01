import discord
from discord.ext import commands

async def setup(bot):
    @bot.command(
        help="Send a message to all text channels in the server.\nUsage: sendall <message>"
    )
    async def sendall(ctx, *, message: str = "Hello"):
        if not ctx.guild:
            await ctx.send("❌ This command must be used in a server.", delete_after=5)
            return

        success = 0
        for channel in ctx.guild.text_channels:
            try:
                await channel.send(message)
                success += 1
            except:
                pass

        await ctx.send(f"📢 Message sent to {success} channel(s).", delete_after=5)
