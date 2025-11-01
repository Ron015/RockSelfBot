import discord
from discord.ext import commands
from functions import config

async def setup(bot):
    @bot.command(aliases=['remote'])
    async def remoteuser(ctx, action: str = None, user: discord.User = None):
        if not action or not user or action.upper() not in ["ADD", "REMOVE"]:
            await ctx.send(f"`{ctx.prefix}remoteuser <ADD|REMOVE> <@user>`", delete_after=5)
            return

        action = action.upper()
        configdata = config.load()

        if "allowedID" not in configdata:
            configdata["allowedID"] = []

        uid = str(user.id)

        if action == "ADD" and uid not in configdata["allowedID"]:
            configdata["allowedID"].append(uid)
            config.save(configdata)
            await ctx.send(f"Added {user.mention} to remote users", delete_after=5)

        elif action == "REMOVE" and uid in configdata["allowedID"]:
            configdata["allowedID"].remove(uid)
            config.save(configdata)
            await ctx.send(f"Removed {user.mention} from remote users", delete_after=5)