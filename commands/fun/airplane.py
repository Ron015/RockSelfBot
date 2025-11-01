import discord
import asyncio

async def setup(bot):
    @bot.command(aliases=['911'])
    async def airplane(ctx):
        frames = [
            ':man_wearing_turban::airplane:    :office:',
            ':man_wearing_turban: :airplane:   :office:',
            ':man_wearing_turban:  :airplane:  :office:',
            ':man_wearing_turban:   :airplane: :office:',
            ':man_wearing_turban:    :airplane::office:',
            ':boom::boom::boom:'
        ]
        msg = await ctx.send(frames[0])
        for frame in frames[1:]:
            await asyncio.sleep(0.5)
            await msg.edit(content=frame)