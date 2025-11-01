import discord
from discord.ext import commands
import random
import string

async def setup(bot):
    @bot.command()
    async def nitro(ctx):
        """Generate a fake Discord Nitro gift link"""
        try:
            # Generate random gift code
            code = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
            nitro_link = f"https://discord.gift/{code}"
            
            await ctx.send(nitro_link)
            
        except Exception as e:
            await ctx.send(f"❌ Error: {str(e)}", delete_after=5)