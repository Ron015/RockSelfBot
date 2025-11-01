import discord
from discord.ext import commands

async def setup(bot):
    @bot.command(
        name="closealldm",
        aliases=['closedmall', 'closedms'],
        help="💬 Closes all your open DM channels."
    )
    async def closealldm(ctx, confirm: str = None):
        """Closes all DM channels after confirmation."""
        if not confirm or confirm.lower() != "yes":
            return await ctx.send(f"⚠️ Are you sure? Use `{bot.command_prefix}closealldm yes` to confirm.", delete_after=10)

        closed_count = 0
        for channel in bot.private_channels:
            if isinstance(channel, discord.DMChannel):
                try:
                    await channel.close()
                    print(f"✅ Closed DM with {channel.recipient}")
                    closed_count += 1
                except Exception as e:
                    print(f"❌ Failed to close DM with {channel.recipient}: {e}")

        await ctx.send(f"✅ Closed **{closed_count}** DMs.", delete_after=10)