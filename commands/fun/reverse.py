import discord
from discord.ext import commands

async def setup(bot):
    @bot.command()
    async def reverse(ctx, *, content: str = None):
        """Reverse your text message"""
        try:
            # Check if content exists
            if not content:
                await ctx.send(f"`{ctx.prefix}reverse <message>`", delete_after=5)
                return
            
            # Reverse the content and send
            reversed_content = content[::-1]
            await ctx.send(reversed_content)
            
        except Exception as e:
            await ctx.send(f"❌ Error: {str(e)}", delete_after=5)