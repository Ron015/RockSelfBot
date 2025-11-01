import discord
from discord.ext import commands

async def setup(bot):
    @bot.command(
        help="Rename all non-bot members to a given nickname.\nUsage: massrename [new_nickname]"
    )
    @commands.has_permissions(manage_nicknames=True)
    async def massrename(ctx, *, new_name: str = None):
        if not new_name:
            await ctx.send("❌ Please provide a new nickname to set for all members.", delete_after=5)
            return

        count = 0
        for member in ctx.guild.members:
            if not member.bot:
                try:
                    await member.edit(nick=new_name)
                    count += 1
                except:
                    pass

        await ctx.send(f"✅ Renamed {count} members to **{new_name}**.")

    @massrename.error
    async def massrename_error(ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("❌ You need the Manage Nicknames permission to use this command!", delete_after=5)
