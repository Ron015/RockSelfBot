import discord
from discord.ext import commands
from functions import config

async def setup(bot):
    @bot.command(aliases=["copycatuser", "copyuser"])
    async def copycat(ctx, action: str = None, user: discord.User = None):
        if not action or not user or action.upper() not in ["ON", "OFF"]:
            await ctx.send(f"`{ctx.prefix}copycat <ON|OFF> <@user>`", delete_after=5)
            return

        action = action.upper()

        configdata = config.load()  # Load config at start

        # Ensure the 'copycat' and 'users' list exist in config
        if "copycat" not in configdata:
            configdata["copycat"] = {}
        if "users" not in configdata["copycat"]:
            configdata["copycat"]["users"] = []

        uid = user.id

        if action == "ON" and uid not in configdata["copycat"]["users"]:
            configdata["copycat"]["users"].append(uid)
            config.save(configdata)  # Save updated config
            await ctx.send(f"Copying {user.mention}", delete_after=5)

        elif action == "OFF" and uid in configdata["copycat"]["users"]:
            configdata["copycat"]["users"].remove(uid)
            config.save(configdata)  # Save updated config
            await ctx.send(f"Stopped copying {user.mention}", delete_after=5)