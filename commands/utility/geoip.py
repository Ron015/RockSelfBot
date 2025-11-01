import discord
from discord.ext import commands
import requests

async def setup(bot):
    @bot.command(
        help="Get geolocation information about an IP address."
    )
    async def geoip(ctx, ip: str = None):
        """Look up geographic info for an IP address using FreeIPAPI."""
        if not ip:
            return await ctx.send("❗ Please provide an IP address to look up, e.g., `geoip 8.8.8.8`", delete_after=5)

        try:
            url = f"https://freeipapi.com/api/json/{ip}"
            response = requests.get(url, timeout=5)
            ip_data = response.json()

            if 'ipAddress' not in ip_data:
                raise ValueError("Invalid IP or no data found")

            # Format output
            output = (
                f"```py\n"
                f"IP Lookup for {ip}:\n"
                f"Country   : {ip_data.get('countryName', 'N/A')}\n"
                f"City      : {ip_data.get('cityName', 'N/A')}\n"
                f"Region    : {ip_data.get('regionName', 'N/A')}\n"
                f"Timezone  : {ip_data.get('timeZone', 'N/A')}\n"
                f"Zip Code  : {ip_data.get('zipCode', 'N/A')}\n"
                f"Latitude  : {ip_data.get('latitude', 'N/A')}\n"
                f"Longitude : {ip_data.get('longitude', 'N/A')}\n"
                f"Currency  : {ip_data.get('currency', {}).get('name', 'N/A')}\n"
                f"Language  : {ip_data.get('language', 'N/A')}\n"
                f"Continent : {ip_data.get('continent', 'N/A')}\n"
                f"```"
            )

            await ctx.send(output)

        except Exception as e:
            await ctx.send(f"❌ Failed to look up IP `{ip}`: {str(e)}", delete_after=5)
