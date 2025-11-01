import discord
from discord.ext import commands
import requests

async def setup(bot):
    @bot.command()
    async def btcprice(ctx):
        try:
            response = requests.get(
                "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd",
                timeout=5
            )
            if response.status_code != 200:
                await ctx.send("❌ Failed to fetch Bitcoin price. Try again later.", delete_after=5)
                return

            btc_data = response.json()
            btc_price = btc_data.get("bitcoin", {}).get("usd")

            if btc_price is None:
                await ctx.send("❌ Bitcoin price not available at the moment.", delete_after=5)
                return

            await ctx.send(f"💰 **Current Bitcoin (BTC) Price:** ${btc_price:,}")
        except Exception as e:
            await ctx.send(f"❌ Error: {str(e)}", delete_after=5)
