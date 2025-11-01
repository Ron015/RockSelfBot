import discord
from discord.ext import commands

async def setup(bot):
    @bot.command(
        name="leaveallgroup",
        aliases=["leavegroups", "quitgroups"],
        help="🚪 Leaves all group DMs you are part of."
    )
    async def leaveallgroups(ctx, confirm: str = None):
        if not confirm or confirm.lower() != "yes":
            return await ctx.send(f"⚠️ Are you sure? Use `{bot.command_prefix}leaveallgroups yes` to confirm.", delete_after=10)

        left_count = 0

        for channel in bot.private_channels:
            if isinstance(channel, discord.GroupChannel):
                try:
                    await channel.leave()
                    print(f"✅ Left group: {channel.name}")
                    left_count += 1
                except Exception as e:
                    print(f"❌ Failed to leave group {channel.name}: {e}")

        await ctx.send(f"✅ Successfully left **{left_count}** group DMs.", delete_after=10)