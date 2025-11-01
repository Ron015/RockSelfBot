import discord
from discord.ext import commands
from functions import *

async def setup(bot):

    @bot.command(
        help="Show your recently deleted DMs. Usage: dmsnipe [number]")
    async def dmsnipe(ctx, number: int = 1):
        """Show your recently deleted DMs"""
        try:
            # This assumes delete_db is globally accessible
            all_deleted = delete_db.get_all()
            key_prefix = f"DM:{ctx.author.id}:"

            user_dms = {
                k: v
                for k, v in all_deleted.items() if k.startswith(key_prefix)
            }

            if not user_dms:
                return await ctx.send("No deleted DMs found.", delete_after=5)

            sorted_dms = sorted(user_dms.values(),
                                key=lambda x: x["deleted_at"],
                                reverse=True)

            if number < 1 or number > len(sorted_dms):
                return await ctx.send(
                    f"Only {len(sorted_dms)} deleted DMs found.",
                    delete_after=5)

            msg = sorted_dms[number - 1]

            content = (f"```js\n𓈀𓈀Deleted DM #{number}:𓈀𓈀\n"
                       f"{msg['content'] or '[No content]'}\n"
                       f"🗑️ Deleted at: {msg['deleted_at'][:19]}\n"
                       f"📅 Originally sent: {msg['created_at'][:19]}```")

            if msg["attachments"]:
                content += "\n\n**Attachments:**\n" + "\n".join(
                    [att["url"] for att in msg["attachments"]])

            await ctx.send(content, delete_after=15)

        except Exception as e:
            print(f"[Error - dmsnipe]: {e}")
            await ctx.send("Failed to snipe DM.", delete_after=5)
