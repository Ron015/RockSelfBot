import discord
from discord.ext import commands

async def setup(bot):
    @bot.command(
        aliases=['gbanner'],
        help="Show the server's banner image."
    )
    async def guildbanner(ctx):
        """Display the server's banner image if set."""
        if not ctx.guild:
            return await ctx.send("⚠️ This command can only be used in a server.", delete_after=5)

        banner = ctx.guild.banner
        if banner:
            await ctx.send(f"🖼️ **{ctx.guild.name}** banner:\n{banner.url}")
        else:
            await ctx.send(f"ℹ️ **{ctx.guild.name}** has no banner set.", delete_after=5)
