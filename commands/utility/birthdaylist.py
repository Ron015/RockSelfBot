import discord
from discord.ext import commands
from functions import *

async def setup(bot):
    @bot.command(name="birthdaylist", aliases=["bdaylist", "bday"])
    async def birthday_list(ctx):
        """📅 Show all saved birthdays sorted by upcoming dates"""
        data = bday_db.load()
        if not data:
            return await ctx.send("📭 Birthday list is empty!")
    
        line_objs = []
        for uid, saved in data.items():
            try:
                bday, has_year = parse_any(saved)
                left = days_until(bday)
                line_objs.append((left, uid, saved, has_year))
            except ValueError:
                continue  # Skip invalid entries
    
        if not line_objs:
            return await ctx.send("⚠️ No valid birthdays found in the list.")
    
        line_objs.sort(key=lambda t: t[0])  # Sort by how many days are left
    
        lines = []
        for left, uid, saved, has_year in line_objs:
            name = await username_from_id(ctx.bot, ctx.guild, int(uid))
            if not name:
                name = f"User ID {uid}"
    
            if has_year:
                y, m, d = full_age(parse_any(saved)[0])
                lines.append(f"🎂 {name}: **{saved}** → {y}y {m}m {d}d old | ⏳ in {left} days")
            else:
                lines.append(f"🎂 {name}: **{saved}** → ⏳ in {left} days")
    
        # Split into message chunks (avoid 2000 char Discord limit)
        MAX_LEN = 1990
        chunk = ""
        for line in lines:
            if len(chunk) + len(line) + 1 > MAX_LEN:
                await ctx.send(f"```\n{chunk}\n```")
                chunk = ""
            chunk += line + "\n"
        if chunk:
            await ctx.send(f"```\n{chunk}\n```")