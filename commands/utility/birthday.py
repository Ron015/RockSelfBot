import discord
from discord.ext import commands
import re
from functions import *

async def setup(bot):
    @bot.command()
    async def birthday(ctx, mention: str = None, date: str = None):
        """
        Set or check birthdays
        Usage:
          !birthday DD-MM          - Set your birthday
          !birthday DD-MM-YYYY     - Set birthday with year
          !birthday @user          - Check someone's birthday
          !birthday                - Check your birthday
        """
        uid = str(ctx.author.id) if mention is None or re.match(r"^\d{1,2}-\d{1,2}", mention) else re.sub(r"[<@!>]", "", mention)
        data = bday_db.load()

        # ---------- SAVE / UPDATE ----------
        if date:
            try:
                _bday, _has_year = parse_any(date)  # Validate date format
            except ValueError:
                return await ctx.send("❌ Invalid format! Use `DD-MM` or `DD-MM-YYYY`", delete_after=7)

            data[uid] = date  # Store as-is
            bday_db.save(data)
            return await ctx.send(f"✅ Birthday saved for <@{uid}>: **{date}** 🎂", delete_after=7)

        # ---------- FETCH ----------
        if uid not in data:
            msg = (
                "⚠️ Your birthday not saved. Use:\n"
                f"`{ctx.prefix}birthday DD-MM` or `{ctx.prefix}birthday DD-MM-YYYY`"
                if mention is None else "⚠️ Birthday not found!"
            )
            return await ctx.send(msg, delete_after=7)

        saved = data[uid]
        bday, has_year = parse_any(saved)
        left = days_until(bday)

        if has_year:
            y, m, d = full_age(bday)
            await ctx.send(
                f"🎉 <@{uid}> is **{y}y {m}m {d}d** old!\n"
                f"⏳ Next birthday in **{left} days** 🥳"
            )
        else:
            await ctx.send(
                f"📅 <@{uid}> birthday: **{saved}**\n"
                f"⏳ Next birthday in **{left} days** 🎈"
            )