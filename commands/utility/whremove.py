import discord
from discord.ext import commands
import time
import requests

async def setup(bot):
    @bot.command(help="Delete Webhook.")
    async def whremove(ctx, webhook: str = None):
        if not webhook:
            await ctx.send(f"`{ctx.prefix}whremove <webhook>`", delete_after=5)
            return

        try:
            response = requests.delete(webhook, timeout=5)

            if response.status_code == 204:
                await ctx.send(f"✅ Successfully deleted webhook: `{webhook}`",
                               delete_after=5)
            else:
                await ctx.send(
                    f"⚠️ Failed to delete webhook!\n"
                    f"Status Code: `{response.status_code}`\n"
                    f"Response: `{response.text}`",
                    delete_after=10)
        except Exception as e:
            await ctx.send(f"❌ Error deleting webhook!\n`{e}`", delete_after=10)
