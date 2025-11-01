import discord
from discord.ext import commands
import requests
import asyncio

async def setup(bot):
    @bot.command(help="Spam on webhook")
    async def webhook(ctx, webhook_url: str = None, count: int = 10, *, message: str = "Spamming..."):
        """
        Send a message multiple times to a webhook URL.
        Usage: !webhook <webhook_url> <count> <message>
        Example: !webhook https://discord.com/api/webhooks/... 5 Hello!
        """
        if not webhook_url:
            await ctx.send(
                "❗ Please provide a valid webhook URL, e.g., `!webhook <webhook_url> 10 <message>`",
                delete_after=5
            )
            return

        # Limit count to avoid abuse
        if count > 20:
            await ctx.send("⚠️ Maximum count is 20 to avoid spam.", delete_after=5)
            return

        for i in range(count):
            data = {"content": message}
            try:
                response = requests.post(webhook_url, json=data)
                if response.status_code == 204:
                    print(f"Message {i+1}/{count} sent successfully.")
                else:
                    print(f"Failed to send message {i+1}/{count}: HTTP {response.status_code}")
            except requests.RequestException as e:
                print(f"Error sending message {i+1}/{count}: {e}")

            await asyncio.sleep(1)
