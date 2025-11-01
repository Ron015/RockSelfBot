import discord
import requests
from discord.ext import commands

async def setup(bot):

    @bot.command(help="Puts a user's avatar in a trashcan")
    async def trash(ctx, user: discord.Member = None):
        if user is None:
            user = ctx.author

        avatar_url = user.display_avatar.replace(format='png').url
        api_url = f"https://nekobot.xyz/api/imagegen?type=trash&url={avatar_url}"

        headers = {
            "User-Agent": "Mozilla/5.0 (DiscordBot)",
            "Accept": "application/json"
        }

        try:
            response = requests.get(api_url, headers=headers, timeout=10)

            if response.status_code != 200:
                await ctx.send(f"❌ API returned non-200 status code: {response.status_code}")
                return

            if not response.text.startswith("{"):
                await ctx.send("❌ API did not return JSON. Content was:")
                await ctx.send(f"```\n{response.text[:500]}\n```")
                return

            data = response.json()

            if not data.get("success", False):
                await ctx.send("❌ API returned failure.")
                return

            await ctx.send(data.get("message", "❌ No image found."))

        except requests.exceptions.RequestException as e:
            await ctx.send(f"❌ Error contacting API: `{e}`")
        except Exception as e:
            await ctx.send(f"❌ Unexpected error: `{e}`")
