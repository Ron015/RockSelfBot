import discord
from discord.ext import commands

async def setup(bot):
    @bot.command(
        aliases=['ginfo'],
        help="Show basic information about the server."
    )
    async def guildinfo(ctx):
        """Displays basic server information."""
        if not ctx.guild:
            return await ctx.send("⚠️ This command can only be used in a server.", delete_after=5)

        guild = ctx.guild
        await ctx.send(
            f"🏰 **Server Info**\n"
            f"**Name:** `{guild.name}`\n"
            f"**ID:** `{guild.id}`\n"
            f"**Created:** `{guild.created_at.strftime('%Y-%m-%d %H:%M:%S')}`\n"
            f"**Owner:** `{guild.owner}`\n"
            f"**Members:** `{guild.member_count}`"
        )
