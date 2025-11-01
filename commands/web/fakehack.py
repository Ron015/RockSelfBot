import discord
from discord.ext import commands
import asyncio
import random
import string
import base64

# Helper function to generate a random string
def random_string(length, chars):
    return ''.join(random.choice(chars) for _ in range(length))

async def setup(bot):
    @bot.command()
    async def fakehack(ctx, user: discord.User = None):
        if user is None:
            return await ctx.send("❗ Usage: `!fakehack @user` — Please mention a user.")

        loading_messages = [
            "🔍 Hacking... Please wait.", 
            "🔓 Bypassing security...",
            "🧠 Cracking passwords...",
            "🐍 Injecting malware...",
            "🛰 Accessing server..."
        ]
        
        for msg in loading_messages:
            await ctx.send(msg)
            await asyncio.sleep(1)

        fake_email = f"{user.name.lower()}@gmail.com"
        fake_password = f"{user.name.lower()}{random.randint(1000, 9999)}"
        created_at_str = user.created_at.strftime("%Y-%m-%d %H:%M:%S")

        # Simulated fake token
        user_id_bytes = str(user.id).encode('utf-8')
        b64_id = base64.b64encode(user_id_bytes).decode('utf-8').rstrip("=")
        part1 = random_string(4, string.ascii_letters + string.digits)
        part2 = random.choice(string.ascii_uppercase)
        part3 = random_string(27, string.ascii_letters + string.digits)
        fake_token = f"{b64_id}.{part1}_{part2}.{part3}"

        final_msg = f"""```js
💻 {user.name}#{user.discriminator} has been successfully hacked! 💻

Discord ID       : {user.id}
Account Created  : {created_at_str}
Email            : {fake_email}
Password         : {fake_password}
Token            : {fake_token}
```"""

        await ctx.send(final_msg)
