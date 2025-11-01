import discord
from discord.ext import commands

async def setup(bot):
    @bot.command(
        help="Delete and recreate the current channel to clear all messages.\nUsage: nukechannel"
    )
    @commands.has_permissions(manage_channels=True)
    async def nukechannel(ctx):
        """Delete and recreate this channel to clear all messages"""
        try:
            channel = ctx.channel
            name = channel.name
            position = channel.position
            category = channel.category
            overwrites = channel.overwrites
            topic = channel.topic
            slowmode_delay = channel.slowmode_delay
            nsfw = channel.is_nsfw()

            await channel.delete(reason=f"Channel nuked by {ctx.author}")

            new_channel = await ctx.guild.create_text_channel(
                name=name,
                position=position,
                category=category,
                overwrites=overwrites,
                topic=topic,
                slowmode_delay=slowmode_delay,
                nsfw=nsfw,
                reason=f"Channel recreation after nuke by {ctx.author}"
            )

            await new_channel.send(
                f"💥 Channel was nuked by {ctx.author.mention}\n"
                f"All messages have been cleared!"
            )

        except Exception as e:
            await ctx.send(f"❌ Failed to nuke channel: {str(e)}")

    @nukechannel.error
    async def nukechannel_error(ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("❌ You need **Manage Channels** permission to use this command!", delete_after=5)
