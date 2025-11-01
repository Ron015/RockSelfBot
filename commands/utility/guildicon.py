import discord
from discord.ext import commands

async def setup(bot):
    @bot.command(
        aliases=['gicon'],
        help="Show the server's icon."
    )
    async def guildicon(ctx):
        """Display the server's icon image if set."""
        if not ctx.guild:
            return await ctx.send("⚠️ This command can only be used in a server.", delete_after=5)

        icon = ctx.guild.icon
        if icon:
            await ctx.send(f"🖼️ **{ctx.guild.name}** icon:\n{icon.url}")
        else:
            await ctx.send(f"ℹ️ **{ctx.guild.name}** has no icon set.", delete_after=5)
