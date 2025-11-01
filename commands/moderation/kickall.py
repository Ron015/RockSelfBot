import discord
from discord.ext import commands


async def setup(bot):

    @bot.command(
        help="Kicks all real (non-bot) members from the server.\nUsage: kickall"
    )
    @commands.has_permissions(kick_members=True)
    async def kickall(ctx):
        kicked_count = 0
        failed = []

        for member in ctx.guild.members:
            if not member.bot and member != ctx.author and member != ctx.guild.owner:
                try:
                    await member.kick(reason="Kicked by kickall command.")
                    kicked_count += 1
                except Exception:
                    failed.append(member)

        await ctx.send(f"✅ Kicked {kicked_count} members.")
        if failed:
            await ctx.send(f"❌ Failed to kick {len(failed)} members.")

    @kickall.error
    async def kickall_error(ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(
                "❌ You need the Kick Members permission to use this command!",
                delete_after=5)
