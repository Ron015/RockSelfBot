import discord
import asyncio
from discord.ext import commands

async def setup(bot):
    @bot.command(help="🦠 Send animated fake virus message")
    async def virus(ctx, type: str = "trojan"):
        # Delete original command message
        # Virus message stages (animated)
        stages = [
            f"`[▓▓▓                    ] / {type}.exe Packing files.`",
            f"`[▓▓▓▓▓▓▓                ] - {type}.exe Packing files..`",
            f"`[▓▓▓▓▓▓▓▓▓▓▓▓           ] \\ {type}.exe Packing files...`",
            f"`[▓▓▓▓▓▓▓▓▓▓▓▓▓▓         ] | {type}.exe Packing files.`",
            f"`[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓      ] - {type}.exe Packing files..`",
            f"`[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓   ] \\ {type}.exe Packing files...`",
            f"`[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ] | {type}.exe Packing files...`",
            f"`[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓] - {type}.exe Packing complete ✅`",
            f"`✅ Successfully downloaded {type}.exe`",
            "`Injecting virus.   |`",
            "`Injecting virus..  /`",
            "`Injecting virus... -`",
            f"`💀 Successfully injected {type}.exe.`"
        ]

        # Send first message and animate
        msg = await ctx.send(stages[0])
        for stage in stages[1:]:
            await asyncio.sleep(0.5)
            await msg.edit(content=stage)