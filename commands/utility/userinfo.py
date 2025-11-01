import discord
from discord.ext import commands

async def setup(bot):
    @bot.command(help="Show information about a user.")
    async def userinfo(ctx, user: discord.User = None):
        if user is None:
            user = ctx.author

        created_at = user.created_at.strftime("%d-%m-%Y %H:%M:%S")
        avatar_url = user.avatar.url if user.avatar else "No Avatar"
        info = (
            f"```js\n"
            f"Username    : {user.name}#{user.discriminator}\n"
            f"ID          : {user.id}\n"
            f"Created At  : {created_at}\n"
            f"Bot?        : {user.bot}\n"
            f"Avatar URL  : {avatar_url}\n"
            f"```"
        )
        await ctx.send(info)
