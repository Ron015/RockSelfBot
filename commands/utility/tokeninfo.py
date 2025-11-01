import discord
from discord.ext import commands
import requests
import datetime

async def setup(bot):
    @bot.command(aliases=['tinfo'], help="Get info about a Discord token.")
    async def tokeninfo(ctx, usertoken: str = None):
        if not usertoken:
            await ctx.send(f"`{ctx.prefix}tokeninfo <token>`", delete_after=5)
            return

        headers = {
            'Authorization': usertoken,
            'Content-Type': 'application/json'
        }

        try:
            response = requests.get('https://discord.com/api/v9/users/@me', headers=headers)
            response.raise_for_status()
            user_data = response.json()

            username = f"{user_data['username']}#{user_data['discriminator']}"
            user_id = user_data['id']
            avatar_url = f"https://cdn.discordapp.com/avatars/{user_id}/{user_data['avatar']}.png" if user_data['avatar'] else "No avatar"
            email = user_data.get('email', 'Not provided')
            mfa_enabled = user_data.get('mfa_enabled', False)
            timestamp = ((int(user_id) >> 22) + 1420070400000) / 1000
            created_at = datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

            info = (
                f"**Token Info**\n"
                f"Username: `{username}`\n"
                f"User ID: `{user_id}`\n"
                f"Created: `{created_at}`\n"
                f"Avatar: {avatar_url}\n"
                f"Email: `{email}`\n"
                f"2FA Enabled: `{mfa_enabled}`"
            )
            await ctx.send(info)

        except requests.exceptions.RequestException as e:
            await ctx.send(f"Error: Invalid token or API issue (`{str(e)}`)", delete_after=5)
        except KeyError:
            await ctx.send("Error: Unexpected API response format", delete_after=5)
