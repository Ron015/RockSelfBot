import discord
from discord.ext import commands
import requests
import json
from functions import *

async def setup(bot):
    @bot.command(aliases=['hs'], help="Change your HypeSquad house.")
    async def hypesquad(ctx, house: str = None):
        configdata = config.load()
        TOKEN = configdata.get("token")
        if not house:
            await ctx.send(
                '> **[**ERROR**]**: Invalid input\n> __Command__: `hypesquad <balance, brilliance, bravery>`',
                delete_after=5
            )
            return

        headers = {
            'Authorization': TOKEN,
            'Content-Type': 'application/json'
        }

        try:
            r = requests.get('https://discord.com/api/v8/users/@me', headers=headers)
            r.raise_for_status()
        except requests.exceptions.RequestException as e:
            await ctx.send(
                f'> **[**ERROR**]**: Invalid status code\n> __Error__: `{str(e)}`',
                delete_after=5
            )
            return

        headers['User-Agent'] = (
            'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
            '(KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 '
            'Electron/4.0.8 Safari/537.36'
        )

        payload = {}
        if house.lower() == "bravery":
            payload = {'house_id': 1}
        elif house.lower() == "brilliance":
            payload = {'house_id': 2}
        elif house.lower() == "balance":
            payload = {'house_id': 3}
        else:
            await ctx.send(
                '> **[**ERROR**]**: Invalid input\n> __Error__: Hypesquad house must be one of: `bravery`, `brilliance`, `balance`',
                delete_after=5
            )
            return

        try:
            r = requests.post(
                'https://discordapp.com/api/v6/hypesquad/online',
                headers=headers,
                json=payload,
                timeout=10
            )
            r.raise_for_status()

            if r.status_code == 204:
                await ctx.send(f'> Hypesquad House changed to `{house}`!')
        except requests.exceptions.RequestException as e:
            await ctx.send(
                f'> **[**ERROR**]**: Unable to change Hypesquad house\n> __Error__: `{str(e)}`',
                delete_after=5
            )
