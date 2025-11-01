import discord
from discord.ext import commands
import time

async def setup(bot):
    @bot.command()
    async def ping(ctx):
        """Check bot latency"""
        try:
            # Calculate ping
            start = time.perf_counter()
            message = await ctx.send("🏓 Pinging...")
            end = time.perf_counter()
            
            # Latency in milliseconds
            latency = (end - start) * 1000
            ws_latency = bot.latency * 1000  # WebSocket latency
            
            await message.edit(
                content=f"🏓 Pong!\n📶 API: `{latency:.0f}ms`\n📡 WebSocket: `{ws_latency:.0f}ms`"
            )
        except Exception as e:
            await ctx.send(f"❌ Error: {str(e)}", delete_after=5)