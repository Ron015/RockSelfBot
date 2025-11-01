import discord
from discord.ext import commands
from gtts import gTTS
import io

async def setup(bot):
    @bot.command()
    async def tts(ctx, *, content: str = None):
        """Convert text to speech (TTS)"""
        try:
            # Delete the command message if possible
            try:
                await ctx.message.delete()
            except:
                pass
            
            # Check if content exists
            if not content:
                await ctx.send(f"`{ctx.prefix}tts <text>`", delete_after=5)
                return
            
            # Create TTS audio
            tts = gTTS(text=content, lang="en")
            f = io.BytesIO()
            tts.write_to_fp(f)
            f.seek(0)
            
            # Send the audio file
            filename = f"{content[:10]}.wav" if len(content) > 10 else f"{content}.wav"
            await ctx.send(file=discord.File(f, filename))
            
        except Exception as e:
            await ctx.send(f"❌ Error: {str(e)}", delete_after=5)