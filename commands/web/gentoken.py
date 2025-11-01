import discord
from discord.ext import commands
import random
import string

# Helper to generate fake token
def generate_fake_token():
    part1 = "ODA" + random.choice(string.ascii_letters) + ''.join(random.choices(string.ascii_letters + string.digits, k=20))
    part2 = random.choice(string.ascii_letters).upper() + ''.join(random.choices(string.ascii_letters + string.digits, k=5))
    part3 = ''.join(random.choices(string.ascii_letters + string.digits, k=27))
    return f"{part1}.{part2}.{part3}"

async def setup(bot):
    @bot.command()
    async def gentoken(ctx, user: str = None):
        token = generate_fake_token()

        if user:
            await ctx.send(f"> **{user}'s token:** ||{token}||")
        else:
            await ctx.send(f"> Fake Token: ||{token}||")
