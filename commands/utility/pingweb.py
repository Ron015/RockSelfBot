import discord
from discord.ext import commands
import requests
import time

async def setup(bot):
    @bot.command(help="Ping a website and show response time.")
    async def pingweb(ctx, url: str = None):
        if not url:
            await ctx.send(f"`{ctx.prefix}pingweb <url>`", delete_after=5)
            return

        if not url.startswith(('http://', 'https://')):
            url = 'http://' + url

        try:
            start = time.perf_counter()
            response = requests.get(url, timeout=5)
            end = time.perf_counter()
            response_time = (end - start) * 1000

            if response.status_code == 200:
                await ctx.send(f"✅ `{url}` is **up!**\nResponse Time: `{response_time:.2f} ms`")
            else:
                await ctx.send(f"⚠️ `{url}` responded with status `{response.status_code}`", delete_after=10)

        except Exception as e:
            await ctx.send(f"❌ `{url}` is **down or unreachable!**\nError: `{e}`", delete_after=10)
