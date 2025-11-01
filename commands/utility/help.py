import discord
import pkgutil
from functions import *
from discord.ext import commands

async def setup(bot):
    @bot.command(aliases=['h'])
    async def help(ctx, category: str = None):
        all_commands = sorted(bot.commands, key=lambda c: c.name)
        custom_cmds = list(custom_commands.load().values())
        total_count = len(all_commands) + len(custom_cmds)  # ✅ Added custom count

        categories = {
            'fun': 'Fun and entertainment commands',
            'utility': 'Useful utilities and tools',
            'moderation': 'Server moderation commands',
            'web': 'Web-based information commands',
            'nsfw': 'NSFW fun commands',
            'customcommand': 'Custom user-defined commands',
            'all': 'Show all commands'
        }

        prefix = bot.command_prefix

        if not category:
            help_text = (
                f"```js\n"
                f"**Rock SelfBot | Prefix: `{prefix}`**\n\n"
                f"**Total Commands: {total_count}**\n\n"  # ✅ Total count includes customs
                f"Available Categories:\n"
            )
            for cat, desc in categories.items():
                help_text += f"\n`{prefix}help {cat}` - {desc}"
            help_text += (
                f"\n\nType `{prefix}help <category>` to see commands in that category\n"
                f"Example: `{prefix}help fun`\n"
                f"```"
            )
            return await ctx.send(help_text)

        category = category.lower()

        if category == 'all':
            pages = []
            current = f"```js\n**All Commands ({total_count})**\n\n"

            def append_line(line):
                nonlocal current
                if len(current) + len(line) >= 1900:
                    current += "```"
                    pages.append(current)
                    current = "```js\n" + line
                else:
                    current += line

            for cmd in all_commands:
                line = f"`{prefix}{cmd.name}`"
                if cmd.aliases:
                    line += f" (aliases: {', '.join([f'{prefix}{a}' for a in cmd.aliases])})"
                line += f" - {cmd.short_doc if cmd.short_doc else 'No description'}\n"
                append_line(line)

            for cmd in sorted(custom_cmds, key=lambda c: c['name']):
                line = f"`{prefix}{cmd['name']}`"
                if cmd.get("aliases"):
                    line += f" (aliases: {', '.join([f'{prefix}{a}' for a in cmd['aliases']])})"
                line += f" - {cmd.get('description', 'No description')}\n"
                append_line(line)

            current += "```"
            pages.append(current)

            for p in pages:
                await ctx.send(p)
            return

        if category not in categories:
            return await ctx.send(
                f"```js\n"
                f"Invalid category! Available categories:\n"
                f"{', '.join([f'`{c}`' for c in categories.keys()])}\n"
                f"Example: `{prefix}help fun`"
                f"```",
                delete_after=10
            )

        if category == "customcommand":
            if not custom_cmds:
                return await ctx.send("No custom commands found!", delete_after=5)

            help_text = f"```js\n**Custom Commands ({len(custom_cmds)})**\n\n"
            for cmd in sorted(custom_cmds, key=lambda c: c['name']):
                name = cmd["name"]
                aliases = cmd.get("aliases", [])
                desc = cmd.get("description", "") or "No description"

                line = f"`{prefix}{name}`"
                if aliases:
                    line += f" (aliases: {', '.join([f'{prefix}{a}' for a in aliases])})"
                line += f" - {desc}\n"

                if len(help_text) + len(line) > 1990:
                    help_text += "```"
                    await ctx.send(help_text)
                    help_text = "```js\n" + line
                else:
                    help_text += line

            help_text += "```"
            return await ctx.send(help_text)

        # Normal category
        try:
            category_package = __import__(f"commands.{category}", fromlist=[''])
            category_path = category_package.__path__
        except Exception as e:
            return await ctx.send(f"Error accessing category '{category}': {e}", delete_after=10)

        category_cmd_names = [name for _, name, ispkg in pkgutil.iter_modules(category_path) if not ispkg and not name.startswith('_')]
        category_commands = [cmd for cmd in all_commands if cmd.name in category_cmd_names]

        if not category_commands:
            return await ctx.send(f"No commands found in the {category} category!", delete_after=5)

        help_text = f"```js\n**{category.capitalize()} Commands ({len(category_commands)})**\n\n"
        for cmd in sorted(category_commands, key=lambda c: c.name):
            doc = cmd.help or cmd.short_doc or "No description available"
            short_doc = doc.split('\n')[0]

            line = f"`{prefix}{cmd.name}`"
            if cmd.aliases:
                line += f" (aliases: {', '.join([f'{prefix}{a}' for a in cmd.aliases])})"
            line += f" - {short_doc}\n"

            if len(help_text) + len(line) > 1990:
                help_text += "```"
                await ctx.send(help_text)
                help_text = "```js\n" + line
            else:
                help_text += line

        help_text += "```"
        await ctx.send(help_text)