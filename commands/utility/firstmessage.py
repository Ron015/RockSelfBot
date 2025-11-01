import discord
from discord.ext import commands

async def setup(bot):
    @bot.command(help="Get the first message in the current channel.")
    async def firstmessage(ctx):
        try:
            async for msg in ctx.channel.history(limit=1, oldest_first=True):
                guild_id = ctx.guild.id if ctx.guild else "@me"  # '@me' for DM link
                channel_id = ctx.channel.id
                message_id = msg.id

                link = f"https://discord.com/channels/{guild_id}/{channel_id}/{message_id}"
                await ctx.send(f"📩 First message: {link}", delete_after=5)
                break

        except discord.HTTPException:
            await ctx.send("❌ Failed to fetch the first message.", delete_after=5)