import discord
from discord.ext import commands
import whois as whoislib
from dateutil.parser import parse

async def setup(bot):
    @bot.command()
    async def dominfo(ctx, domain: str = None):
        """
        Get WHOIS information for a domain
        Usage: {prefix}dominfo <domain>
        Example: {prefix}dominfo google.com
        """
        if not domain:
            await ctx.send("❗ Please provide a domain (e.g., `!dominfo google.com`)", delete_after=5)
            return

        def format_date(date_obj):
            """Helper function to format date objects"""
            if isinstance(date_obj, list):
                date_obj = date_obj[0]
            if not date_obj:
                return "N/A"
            try:
                if isinstance(date_obj, str):
                    date_obj = parse(date_obj)
                return date_obj.strftime('%d %b %Y')
            except:
                return "N/A"

        try:
            domain_info = whoislib.whois(domain)
            
            if not domain_info.domain_name:
                await ctx.send(f"❌ No WHOIS data found for `{domain}`.", delete_after=10)
                return

            # Format name servers
            name_servers = domain_info.name_servers
            if name_servers:
                if isinstance(name_servers, list):
                    name_servers = ", ".join(name_servers)
                name_servers = name_servers[:100] + "..." if len(name_servers) > 100 else name_servers

            response = (
                f"```js\n"
                f"WHOIS Lookup for: {domain}\n\n"
                f"Domain: {domain_info.domain_name or 'N/A'}\n"
                f"Registrar: {domain_info.registrar or 'N/A'}\n"
                f"Creation Date: {format_date(domain_info.creation_date)}\n"
                f"Expiration Date: {format_date(domain_info.expiration_date)}\n"
                f"Updated Date: {format_date(domain_info.updated_date)}\n"
                f"Name Servers: {name_servers or 'N/A'}\n"
                f"Status: {domain_info.status or 'N/A'}\n"
                f"```"
            )
            await ctx.send(response)

        except Exception as e:
            print(f"[WHOIS Error] {e}")
            await ctx.send(f"❌ Failed to fetch WHOIS data for `{domain}`. Error: {str(e)}", delete_after=10)