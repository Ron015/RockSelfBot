import discord
from discord.ext import commands
import random
from functions import *

async def setup(bot):
    @bot.command()
    async def rate(ctx, arg1: str = None, arg2: str = None):
        valid_categories = {
            "good": "👍 Good",
            "bad": "👎 Bad", 
            "gay": "🌈 Gay",
            "gamer": "🎮 Gamer",
            "simp": "😍 Simp",
            "smart": "🧠 Smart",
            "funny": "😂 Funny"
        }
    
        category = None
        member = None
    
        # Identify category and mention
        if arg1 is None or arg2 is None:
            await ctx.send("❌ Usage: `!rate <category> <@user>` or `!rate <@user> <category>`", delete_after=7)
            return
    
        # Try both positions
        if arg1.lower() in valid_categories:
            category = arg1.lower()
            member = await commands.MemberConverter().convert(ctx, arg2)
        elif arg2.lower() in valid_categories:
            category = arg2.lower()
            member = await commands.MemberConverter().convert(ctx, arg1)
        else:
            await ctx.send("❌ Invalid category or member! Example: `!rate gay @someone`", delete_after=7)
            return
    
        if member is None:
            await ctx.send("❌ Could not find mentioned user.", delete_after=7)
            return
    
        # Continue as before from here...
        user_id = str(member.id)
        display_category = valid_categories[category]
    
        all_ratings = ratings_db.get_all()
        if user_id not in all_ratings:
            all_ratings[user_id] = {}
            ratings_db.set(user_id, {})
        user_ratings = ratings_db.get(user_id)
    
        if category not in user_ratings:
            rating = random.randint(1, 100)
            user_ratings[category] = rating
            ratings_db.set(user_id, user_ratings)
    
        current_rating = user_ratings[category]
    
        response = (
            f"**{member.display_name}'s {display_category} Rating**\n"
            f"```\n"
            f"╔══════════════════════╗\n"
            f"║                      ║\n"
            f"║       {current_rating:3d}/100        ║\n"
            f"║                      ║\n"
            f"╚══════════════════════╝\n"
            f"```"
        )
    
        if current_rating < 20:
            response += "\n*Yikes... that's rough* 😬"
        elif current_rating > 90:
            response += "\n*Now that's impressive!* 🏆"
    
        await ctx.send(response)