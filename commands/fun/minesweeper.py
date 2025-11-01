import discord
from discord.ext import commands
import random

async def setup(bot):
    @bot.command(aliases=['mine'])
    async def minesweeper(ctx, size: int = 5):
        """Play Minesweeper with customizable size"""
        try:
            # Validate and adjust size
            size = max(min(size, 8), 2)
            
            # Generate bombs
            bombs = [[random.randint(0, size - 1), random.randint(0, size - 1)] for _ in range(size - 1)]
            
            # Build the board
            board = ""
            for y in range(size):
                for x in range(size):
                    if [x, y] in bombs:
                        board += "||:bomb:||"
                    else:
                        # Count adjacent bombs
                        count = sum(1 for dx, dy in [(-1, -1), (0, -1), (1, -1), 
                                    (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)] 
                                if [x + dx, y + dy] in bombs and 0 <= x + dx < size and 0 <= y + dy < size)
                        board += f"||:{'zero one two three four five six'.split()[count]}:||" if count else "||:black_square_button:||"
                board += "\n"
            
            await ctx.send(f"**Minesweeper ({size}x{size})**\n{board}")
            
        except Exception as e:
            await ctx.send(f"❌ Error: {str(e)}", delete_after=5)