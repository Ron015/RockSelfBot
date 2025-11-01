import discord
from discord.ext import commands
import re
from functions import *

async def setup(bot):
    @bot.command()
    async def snipe(ctx, number: int = 1):
        """Show recently deleted messages in this channel"""
        try:
            all_deleted = delete_db.get_all()
            key_prefix = f"{ctx.guild.id}:{ctx.channel.id}:"
            channel_deletions = {
                k: v for k, v in all_deleted.items() 
                if k.startswith(key_prefix)
            }
            
            if not channel_deletions:
                return await ctx.send("No deleted messages found.", delete_after=5)
    
            sorted_deletions = sorted(
                channel_deletions.values(),
                key=lambda x: x["deleted_at"],
                reverse=True
            )
            
            if number < 1 or number > len(sorted_deletions):
                return await ctx.send(f"Only {len(sorted_deletions)} deleted messages found.", delete_after=5)
    
            msg = sorted_deletions[number-1]
            author = ctx.guild.get_member(msg["author"]["id"]) or msg["author"]["name"]
            
            content = (
                f"```js\n**Deleted message #{number} from {author}:**\n"
                f"{msg['content'] or '[No content]'}\n"
                f"🗑️ Deleted at: {msg['deleted_at'][:19]}\n"
                f"📅 Originally sent: {msg['created_at'][:19]}\n```"
            )
    
            if msg["attachments"]:
                content += "\n\n**Attachments:**\n" + "\n".join([att["url"] for att in msg["attachments"]])
    
            await ctx.send(content, delete_after=15)
    
        except Exception as e:
            print(f"Snipe error: {e}")
            await ctx.send("Failed to snipe message.", delete_after=5)
            