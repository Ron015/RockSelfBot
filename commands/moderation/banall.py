import discord
from discord.ext import commands

async def setup(bot):
    @bot.command(
        help="Bans all real (non-bot) members from the server.\nUsage: banall"
    )
    @commands.has_permissions(ban_members=True)
    async def banall(ctx):
        failed = []
        banned_count = 0

        for member in ctx.guild.members:
            if not member.bot and member != ctx.author and member != ctx.guild.owner:
                try:
                    await member.ban(reason="Banned by banall command.")
                    banned_count += 1
                except Exception:
                    failed.append(member)

        await ctx.send(f"✅ Banned {banned_count} members.")
        if failed:
            await ctx.send(f"❌ Failed to ban {len(failed)} members.")

    @banall.error
    async def banall_error(ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("❌ You need the Ban Members permission to use this command!", delete_after=5)
