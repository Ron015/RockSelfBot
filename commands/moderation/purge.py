import discord
from discord.ext import commands

async def setup(bot):
    @bot.command(
        help="Delete a number of messages in the current channel (1–100).\nUsage: purge <number>"
    )
    @commands.has_permissions(manage_messages=True)
    async def purge(ctx, num: int = 1):
        if not 1 <= num <= 100:
            await ctx.send("❌ You must specify a number between 1 and 100.", delete_after=5)
            return

        try:
            deleted = await ctx.channel.purge(limit=num)
            await ctx.send(f"🧹 Deleted {len(deleted)} messages.", delete_after=5)
        except Exception as e:
            await ctx.send(f"❌ Failed to purge messages: {str(e)}")

    @purge.error
    async def purge_error(ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("❌ You need **Manage Messages** permission to use this command!", delete_after=5)
