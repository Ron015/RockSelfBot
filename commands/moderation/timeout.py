import discord
from discord.ext import commands
import datetime

async def setup(bot):
    @bot.command(
        aliases=['mute'],
        help=(
            "Timeout a member for a specified duration.\n"
            "Duration supports s (seconds), m (minutes), h (hours), d (days).\n"
            "Usage: timeout @member <duration> [reason]\n"
            "Example: timeout @User 30m spamming"
        )
    )
    @commands.has_permissions(moderate_members=True)
    async def timeout(ctx, member: discord.Member, duration: str = "10m", *, reason="No reason provided"):
        try:
            unit = duration[-1].lower()
            value = duration[:-1]

            if not value.isdigit():
                raise ValueError("Invalid duration format")

            value = int(value)

            if unit == 's':
                delta = datetime.timedelta(seconds=value)
            elif unit == 'm':
                delta = datetime.timedelta(minutes=value)
            elif unit == 'h':
                delta = datetime.timedelta(hours=value)
            elif unit == 'd':
                delta = datetime.timedelta(days=value)
            else:
                raise ValueError("Invalid time unit (use s/m/h/d)")

            if delta.total_seconds() > 2419200:  # 28 days max
                raise ValueError("Timeout cannot exceed 28 days")

            # Send DM to muted user
            try:
                await member.send(
                    f"You were timed out in {ctx.guild.name}\n"
                    f"Duration: {delta}\n"
                    f"Reason: {reason}\n"
                    f"Moderator: {ctx.author}"
                )
            except discord.Forbidden:
                pass  # Couldn't send DM

            until = datetime.datetime.utcnow() + delta
            await member.timeout(until, reason=f"{ctx.author}: {reason}")

            await ctx.send(
                f"✅ {member} has been timed out for {delta}.\n"
                f"Reason: {reason}\n"
                f"Until: {until.strftime('%Y-%m-%d %H:%M:%S UTC')}"
            )

        except Exception as e:
            await ctx.send(
                f"❌ Failed to timeout {member}: {str(e)}\n"
                f"Usage: timeout @user 30m [reason] (s=seconds, m=minutes, h=hours, d=days)"
            )

    @timeout.error
    async def timeout_error(ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("❌ You don't have permission to timeout members!", delete_after=5)
