import discord
from discord.ext import commands

async def setup(bot):
    @bot.command(
        aliases=['grename'],
        help="Rename the server (requires Manage Server permission)."
    )
    async def guildrename(ctx, *, name: str = None):
        """Renames the server to the specified name."""
        if not name:
            return await ctx.send("❗ Usage: `guildrename <new name>`", delete_after=5)

        if not ctx.guild:
            return await ctx.send("⚠️ This command can only be used in a server.", delete_after=5)

        if not ctx.guild.me.guild_permissions.manage_guild:
            return await ctx.send("🚫 I don't have permission to manage the server name.", delete_after=5)

        try:
            await ctx.guild.edit(name=name)
            await ctx.send(f"✅ Renamed the server to `{name}`")
        except discord.HTTPException as e:
            await ctx.send(f"❌ Failed to rename server: {e}", delete_after=5)
