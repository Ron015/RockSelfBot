import discord
from discord.ext import commands

async def setup(bot):
    @bot.command(
        name="leaveallguild",
        aliases=['leaveguilds', 'quitallguild'],
        help="🚪 Leave all servers (guilds) you're in. Be careful!"
    )
    async def leaveall(ctx, confirm: str = None):
        """Leaves all guilds after confirmation."""
        if not confirm or confirm.lower() != "yes":
            return await ctx.send(f"⚠️ Are you sure? Use `{bot.command_prefix}leaveall yes` to confirm.", delete_after=10)

        left_count = 0
        for guild in bot.guilds:
            try:
                await guild.leave()
                print(f"✅ Left {guild.name} ({guild.id})")
                left_count += 1
            except Exception as e:
                print(f"❌ Failed to leave {guild.name}: {e}")

        await ctx.send(f"🚀 Successfully left **{left_count}** servers.")