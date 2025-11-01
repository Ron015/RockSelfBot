import random
from discord.ext import commands

async def setup(bot):
    @bot.command(help="🪙 Flip a coin and get Heads or Tails")
    async def flip(ctx):
        result = random.choice(['Heads', 'Tails'])
        emoji = '🪙'
        await ctx.send(f"""```js
{ctx.author} Flip the coin,
The coin landed on: **{result}** {emoji}```""")
