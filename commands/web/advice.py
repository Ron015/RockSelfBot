import discord
from discord.ext import commands
import requests

async def setup(bot):
    """
    Sets up the advice command for the Discord bot.

    Args:
        bot: The instance of the Discord bot.
    """

    @bot.command()
    async def advice(ctx):
        """
        Fetches a random piece of advice from an external API and sends it to the Discord channel.

        Args:
            ctx: The context in which the command was invoked.
        """
        # Attempt to delete the user's command message
        try:
            response = requests.get("https://api.adviceslip.com/advice", timeout=5)

            # Check if the response status is OK (200)
            if response.status_code != 200:
                await ctx.send("❌ Couldn't fetch advice. Try again later.", delete_after=5)
                return

            # Parse the JSON response to extract advice
            data = response.json()
            advice = data.get("slip", {}).get("advice", "No advice available at the moment.")

        except Exception as e:
            # Handle any exceptions that occur during the request
            await ctx.send(f"❌ Error: {str(e)}", delete_after=5)
            return

        # Send the fetched advice to the Discord channel
        await ctx.send(f"💡 **Advice:** {advice}")
