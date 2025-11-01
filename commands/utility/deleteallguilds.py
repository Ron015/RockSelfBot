import discord
from discord.ext import commands

async def setup(bot):
    @bot.command(
        name="deleteallguilds",
        aliases=["deleteguilds", "nukeownservers"],
        help="💥 Deletes all guilds you own."
    )
    async def deleteallguilds(ctx, confirm: str = None):
        if not confirm or confirm.lower() != "yes":
            return await ctx.send(f"⚠️ Are you sure? Use `{bot.command_prefix}deleteallguilds yes` to confirm.", delete_after=10)

        deleted_count = 0

        for guild in bot.guilds:
            if guild.owner_id != bot.user.id:
                print(f"❌ Skipped {guild.name}: Not owner")
                continue

            try:
                await guild.delete()
                print(f"✅ Deleted: {guild.name}")
                deleted_count += 1
            except Exception as e:
                print(f"❌ Failed to delete {guild.name}: {e}")

        await ctx.send(f"💥 Successfully deleted **{deleted_count}** guild(s) where you are owner.", delete_after=10)