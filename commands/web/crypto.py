import discord
from discord.ext import commands
import requests

async def setup(bot):
    @bot.command()
    async def crypto(ctx, *, coins: str = None):
        if not coins:
            await ctx.send("❗ Please provide cryptocurrency names, e.g., `crypto bitcoin, ethereum`", delete_after=5)
            return

        # Clean and split the coin input
        coins_list = [coin.strip().lower() for coin in coins.split(",")]
        coin_ids = ",".join(coins_list)

        # Fetch prices from CoinGecko API
        try:
            response = requests.get(f"https://api.coingecko.com/api/v3/simple/price?ids={coin_ids}&vs_currencies=usd")
            if response.status_code != 200:
                await ctx.send("❌ Failed to fetch prices. Please try again later.", delete_after=5)
                return

            crypto_data = response.json()
        except Exception as e:
            await ctx.send(f"❌ Error fetching data: {str(e)}", delete_after=5)
            return

        # Prepare the message
        result_message = "**💰 Cryptocurrency Prices (USD):**\n"
        for coin in coins_list:
            if coin in crypto_data and "usd" in crypto_data[coin]:
                price = crypto_data[coin]["usd"]
                result_message += f"**{coin.capitalize()}**: ${price}\n"
            else:
                result_message += f"❌ No data for **{coin}**.\n"

        await ctx.send(result_message)
