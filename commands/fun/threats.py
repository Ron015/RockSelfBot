import discord
from discord.ext import commands
import aiohttp
import asyncio

async def setup(bot):

    @bot.command(help="Fake threatening message image")
    async def threats(ctx, user: discord.Member = None):
        if not user:
            await ctx.send("❌ Please mention a user.")
            return

        avatar_url = user.display_avatar.with_format('png').url
        msg = await ctx.send("⏳ Generating image, please wait...")

        try:
            url = f"https://nekobot.xyz/api/imagegen?type=threats&url={avatar_url}"

            timeout = aiohttp.ClientTimeout(total=5)  # 5 sec timeout

            async with aiohttp.ClientSession(timeout=timeout) as session:
                async with session.get(url) as response:
                    if response.status != 200:
                        return await msg.edit(content=f"❌ API Error! Status code: {response.status}")

                    data = await response.json()

            if "message" in data and data["message"].startswith("http"):
                await msg.edit(content=data["message"])
            else:
                await msg.edit(content="❌ Invalid response from API.")

        except asyncio.TimeoutError:
            await msg.edit(content="❌ Timed out! No response within 5 seconds.")
        except Exception as e:
            await msg.edit(content=f"❌ Unexpected error: {e}")