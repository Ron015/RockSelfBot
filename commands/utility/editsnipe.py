import discord
from discord.ext import commands
from functions import *

async def setup(bot):
    @bot.command(
        help="Show recently edited messages in this channel.\nUsage: editsnipe [number]"
    )
    async def editsnipe(ctx, number: int = 1):
        """Show recently edited messages in this channel"""
        try:
            # Assuming edit_db is globally available or injected elsewhere
            all_edits = edit_db.get_all()
            key_prefix = f"{ctx.guild.id}:{ctx.channel.id}:"

            # Filter edits for this channel
            channel_edits = {
                k: v for k, v in all_edits.items()
                if k.startswith(key_prefix)
            }

            if not channel_edits:
                return await ctx.send("No edited messages found.", delete_after=5)

            # Sort edits by edit time
            sorted_edits = sorted(
                channel_edits.values(),
                key=lambda x: x["edited_at"],
                reverse=True
            )

            if number < 1 or number > len(sorted_edits):
                return await ctx.send(f"Only {len(sorted_edits)} edited messages found.", delete_after=5)

            msg = sorted_edits[number - 1]
            author = ctx.guild.get_member(msg["author"]["id"]) or msg["author"]["name"]

            content = (
                f"```js\n𓈀𓈀Edited message #{number} from {author}:𓈀𓈀\n"
                f"🔙 Before: {msg['before']['content'] or '[No content]'}\n"
                f"🔄 After: {msg['after']['content'] or '[No content]'}\n"
                f"✏️ Edited at: {msg['edited_at'][:19]}\n"
                f"📅 Originally sent: {msg['created_at'][:19]}```"
            )

            if msg["after"]["attachments"]:
                content += "\n\n**Attachments:**\n" + "\n".join(
                    [att["url"] for att in msg["after"]["attachments"]]
                )

            await ctx.send(content, delete_after=15)

        except Exception as e:
            print(f"[Error - editsnipe]: {e}")
            await ctx.send("Failed to snipe edit.", delete_after=5)
