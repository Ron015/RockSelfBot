from discord.ext import commands
import random

async def setup(bot):
    @bot.command(help="🎱 Ask the magic 8-ball a question and get a random answer")
    async def eightball(ctx, *, question: str = None):
        if not question:
            await ctx.send("Ask a question, and I'll give you an answer!", delete_after=5)
            return

        responses = [
            "Yes", "No", "Maybe", "Definitely", "Ask again later",
            "Absolutely not", "Without a doubt", "Cannot predict now", "Don't count on it", "Yes, but be careful"
        ]

        answer = random.choice(responses)
        emoji = '🎱'
        await ctx.send(f"""```js
Question: {question}
By: {ctx.author}
Answer: {answer} {emoji}```""")
