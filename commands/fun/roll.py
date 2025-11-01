import random
from discord.ext import commands

async def setup(bot):
    @bot.command(help="🎲 Roll a six-sided dice and get a random number")
    async def roll(ctx):
        roll_result = random.randint(1, 6)
        emoji = '🎲'
        await ctx.send(f"""```js        
{ctx.author} Rolled dice: **{roll_result}** {emoji}```""")
