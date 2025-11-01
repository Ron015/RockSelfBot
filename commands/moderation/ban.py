import discord
from discord.ext import commands

async def setup(bot):
    @bot.command(
        help="Ban a specific member from the server.\nUsage: ban @user [reason]"
    )
    @commands.has_permissions(ban_members=True)
    async def ban(ctx, member: discord.Member, *, reason="No reason provided"):
        try:
            await member.ban(reason=reason)
            await ctx.send(f"✅ Banned {member.mention} | Reason: {reason}")
        except Exception as e:
            await ctx.send(f"❌ Failed to ban: {str(e)}")

    @ban.error
    async def ban_error(ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("❌ You need the Ban Members permission!")
