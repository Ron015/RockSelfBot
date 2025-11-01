import discord
from discord.ext import commands
import requests

async def setup(bot):
    @bot.command()
    async def pokedex(ctx, *, pokemon_name: str = None):
        if not pokemon_name:
            await ctx.send("❗ Please provide a Pokémon name, e.g., `pokedex Pikachu`", delete_after=5)
            return

        url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
        try:
            response = requests.get(url, timeout=5)
        except requests.RequestException:
            await ctx.send("❌ Failed to reach the Pokémon API. Please try again later.", delete_after=5)
            return

        if response.status_code != 200:
            await ctx.send(f"❌ No Pokémon found with the name '{pokemon_name}'.", delete_after=5)
            return

        poke_data = response.json()

        name = poke_data.get('name', 'N/A').capitalize()
        poke_id = poke_data.get('id', 'N/A')
        height = poke_data.get('height', 0) / 10  # decimeters to meters
        weight = poke_data.get('weight', 0) / 10  # hectograms to kg
        types = ', '.join(t['type']['name'].capitalize() for t in poke_data.get('types', [])) or "N/A"
        abilities = ', '.join(a['ability']['name'].capitalize() for a in poke_data.get('abilities', [])) or "N/A"
        sprite = poke_data.get('sprites', {}).get('front_default', None)

        msg = (f"**Pokedex Entry for {name}:**\n"
               f"**ID:** {poke_id}\n"
               f"**Height:** {height} meters\n"
               f"**Weight:** {weight} kg\n"
               f"**Types:** {types}\n"
               f"**Abilities:** {abilities}\n")

        if sprite:
            msg += f"**Sprite:** {sprite}"

        await ctx.send(msg)
