import discord
from discord.ext import commands

async def setup(bot):
    @bot.command(
        help="Rename all channels in the server to a given name.\nUsage: massrenamechannels [new_channel_name]"
    )
    @commands.has_permissions(manage_channels=True)
    async def massrenamechannels(ctx, *, new_name: str = None):
        if not new_name:
            await ctx.send("❌ Please provide a new name to rename all channels.", delete_after=5)
            return

        count = 0
        for channel in ctx.guild.channels:
            try:
                await channel.edit(name=new_name)
                count += 1
            except:
                pass

        await ctx.send(f"✅ Renamed {count} channels to **{new_name}**.")

    @massrenamechannels.error
    async def massrenamechannels_error(ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("❌ You need the Manage Channels permission to use this command!", delete_after=5)
