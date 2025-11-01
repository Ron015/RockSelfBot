import discord
from discord.ext import commands
from functions import config

async def setup(bot):
    @bot.command(aliases=['autor'])
    async def autoreply(ctx, command: str = None, user: discord.User = None):
        if not command or command.upper() not in ["ON", "OFF"]:
            await ctx.send(f"`{ctx.prefix}autoreply <ON|OFF> [@user]`", delete_after=5)
            return

        command = command.upper()
        configdata = config.load()

        # Make sure config keys exist
        if "autoreply" not in configdata:
            configdata["autoreply"] = {}
        if "users" not in configdata["autoreply"]:
            configdata["autoreply"]["users"] = []
        if "channels" not in configdata["autoreply"]:
            configdata["autoreply"]["channels"] = []

        target = str(user.id) if user else str(ctx.channel.id)
        key = "users" if user else "channels"

        if command == "ON" and target not in configdata["autoreply"][key]:
            configdata["autoreply"][key].append(target)
            config.save(configdata)
            await ctx.send(f"Autoreply ON for {'user' if user else 'channel'}", delete_after=5)

        elif command == "OFF" and target in configdata["autoreply"][key]:
            configdata["autoreply"][key].remove(target)
            config.save(configdata)
            await ctx.send(f"Autoreply OFF for {'user' if user else 'channel'}", delete_after=5)