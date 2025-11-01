import discord
from discord.ext import commands

async def setup(bot):
    @bot.command(
        help="Kick a specific member from the server.\nUsage: kick @user [reason]"
    )
    @commands.has_permissions(kick_members=True)
    async def kick(ctx, member: discord.Member, *, reason="No reason provided"):
        """Kick a member from the server"""
        try:
            # Attempt to DM the member
            try:
                await member.send(
                    f"You were kicked from **{ctx.guild.name}**\n"
                    f"Reason: {reason}\n"
                    f"Moderator: {ctx.author}"
                )
            except discord.Forbidden:
                pass  # Couldn't DM the member

            # Perform the kick
            await member.kick(reason=f"{ctx.author}: {reason}")
            await ctx.send(f"✅ {member.mention} has been kicked. Reason: {reason}")

        except Exception as e:
            await ctx.send(f"❌ Failed to kick {member}: {str(e)}")

    @kick.error
    async def kick_error(ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("❌ You don't have permission to kick members!", delete_after=5)
