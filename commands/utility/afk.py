import discord
from discord.ext import commands
from functions import config

async def setup(bot):

    @bot.command()
    async def afk(ctx, status: str = None, *, message: str = None):
        configdata = config.load()  # <- correct variable name

        if not status or status.lower() not in ["on", "off"]:
            await ctx.send(f"`{ctx.prefix}afk <ON|OFF> [message]`", delete_after=5)
            return

        status = status.lower()

        if "afk" not in configdata:
            configdata["afk"] = {"enabled": False, "message": ""}

        if status == "on":
            configdata["afk"]["enabled"] = True
            configdata["afk"]["message"] = message or "AFK"
            config.save(configdata)
            await ctx.send(f"```js\nAFK ON:\nMessage Is: `{configdata['afk']['message']}`\n```", delete_after=5)

        elif status == "off":
            configdata["afk"]["enabled"] = False
            config.save(configdata)
            await ctx.send("AFK OFF", delete_after=5)