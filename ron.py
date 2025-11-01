import discord
from discord.ext import commands
from discord import DMChannel

import asyncio
import datetime
import io
import json
import os
import random
import re
import requests
import string
import sys
import time
import base64
import math
import pkgutil
import threading
from gtts import gTTS
import pyfiglet
from dateutil.parser import parse
from dateutil.relativedelta import relativedelta
import whois as whoislib
from typing import Union
from functions import *
import warnings
warnings.filterwarnings("ignore", category=ResourceWarning)
configdata = config.load()
commands_list = custom_commands.load()
TOKEN = configdata.get("token", None)


if not TOKEN:
    raise ValueError("❌ Bot token not found in!")

start_time = datetime.datetime.now()

# Custom bot class to hold our databases
class RonBot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

# Initialize bot
bot = RonBot(command_prefix=get_prefix(), user_bot=True, help_command=None)

# Logger setup
class Logger:
    def write(self, message):
        if message.strip() != "":
            consolelog.add_console_log(message.strip())
        sys.__stdout__.write(message)

    def flush(self):
        pass

sys.stdout = Logger()
sys.stderr = Logger()

# Event handlers
@bot.event
async def on_ready():
    print(f"Connected to {bot.user}")
    print(f"Prefix: {get_prefix()}")


#command logger
@bot.event
async def on_command(ctx):
    try:
        command = ctx.command.name if ctx.command else "unknown"
        username = str(ctx.author)
        server = str(ctx.guild) if ctx.guild else "DM"
        channel = str(ctx.channel)
        datetime_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        cmdlog.add_log(
            command=command,
            username=username,
            server=server,
            channel=channel,
            datetime=datetime_now
        )
    except Exception as e:
        print(f"Error logging command: {e}")

#All utility message functions
@bot.event
async def on_message(message):
    if message.author.bot:
        return

    configdata = config.load()
    allowedIDs = configdata.get("allowedID", [])
    content = message.content
    author_id = str(message.author.id)

    # 💬 Copycat
    if author_id in configdata["copycat"]["users"]:
        if message.content.startswith(get_prefix()):
            await message.reply(message.content[len(get_prefix()):])
        else:
            await message.reply(message.content)

    # 💤 AFK
    if configdata["afk"]["enabled"] and message.author != bot.user:
        if bot.user in message.mentions or isinstance(message.channel, discord.DMChannel):
            await message.reply(f"**USER IS AFK**\nMessage: ```{configdata['afk']['message']}```")
            return

    # 🤖 Autoreply
    if message.author != bot.user:
        user_id = author_id
        channel_id = str(message.channel.id)

        if user_id in configdata["autoreply"]["users"] or channel_id in configdata["autoreply"]["channels"]:
            message_list = configdata["autoreply"]["messages"]
            if message_list:
                selected = random.choice(message_list)
                await message.reply(selected)
                return

    # ✅ Process normal commands ONLY IF in allowedIDs
    if author_id in allowedIDs:
        await bot.process_commands(message)

    # ✅ Custom Command Handler
    for cmd_name, cmd in commands_list.items():
        name = cmd.get("name", cmd_name)
        aliases = cmd.get("aliases", [])
        with_prefix = cmd.get("with_prefix", True)
        triggers = [name] + aliases
        matched = False
        args = []

        if with_prefix:
            for trig in triggers:
                full_trigger = get_prefix() + trig
                if content.startswith(full_trigger):
                    matched = True
                    remainder = content[len(full_trigger):].strip()
                    args = remainder.split() if remainder else []
                    break
        else:
            for trig in triggers:
                if content.startswith(trig):
                    matched = True
                    remainder = content[len(trig):].strip()
                    args = remainder.split() if remainder else []
                    break

        if not matched:
            continue

        # 🔐 Permission check
        bypass_checks = message.author.id in allowedIDs
        is_global_allowed = cmd.get("allowed_global_users", True)

        if not bypass_checks and not is_global_allowed:
            if message.author.id not in cmd.get("allowed_users", []):
                continue

            allowed_in = cmd.get("allowed_in", ["guild", "dm"])
            if message.guild is None and "dm" not in allowed_in:
                continue
            if message.guild and "guild" not in allowed_in:
                continue
            if "user" in allowed_in and message.author.id not in cmd.get("allowed_users", []):
                continue
            if "channel" in allowed_in and message.channel.id not in cmd.get("allowed_channels", []):
                continue

            allowed_guilds = cmd.get("allowed_guilds", [])
            if allowed_guilds and message.guild and message.guild.id not in allowed_guilds:
                continue

        # 🧠 Respond
        response = parse_variables(cmd.get("response", ""), message, args)

        if cmd.get("reply", False):
            await message.reply(response, mention_author=False)
        else:
            await message.channel.send(response)

        if cmd.get("delete_command_trigger", False):
            try:
                await message.delete()
            except:
                pass

        return  # ✅ Only one custom command runs

#snipe
@bot.event
async def on_message_delete(message):
    """Log deleted messages to database"""
    if message.author == bot.user:
        return

    deleted_at = get_time()
    channel_type = "DM" if isinstance(message.channel, DMChannel) else "GUILD"

    data = {
        "content": message.content,
        "author": {
            "id": message.author.id,
            "name": str(message.author),
            "discriminator": message.author.discriminator,
        },
        "channel": {
            "id": message.channel.id,
            "name": getattr(message.channel, "name", "DM"),
            "type": channel_type
        },
        "attachments": format_attachments(message),
        "deleted_at": deleted_at,
        "message_id": message.id,
        "created_at": message.created_at.isoformat()
    }

    if isinstance(message.channel, DMChannel):
        key = f"DM:{message.author.id}:{message.id}"
    else:
        key = f"{message.guild.id}:{message.channel.id}:{message.id}"

    delete_db.set(key, data)

#edit snipe
@bot.event
async def on_message_edit(before, after):
    """Log edited messages to database"""
    if after.author == bot.user or isinstance(after.channel, DMChannel):
        return

    if before.content == after.content:
        return

    edited_at = get_time()

    data = {
        "before": {
            "content": before.content,
            "attachments": format_attachments(before)
        },
        "after": {
            "content": after.content,
            "attachments": format_attachments(after)
        },
        "author": {
            "id": after.author.id,
            "name": str(after.author),
            "discriminator": after.author.discriminator,
        },
        "channel": {
            "id": after.channel.id,
            "name": after.channel.name,
            "type": "GUILD"
        },
        "edited_at": edited_at,
        "message_id": after.id,
        "created_at": after.created_at.isoformat(),
        "last_edited": after.edited_at.isoformat() if after.edited_at else None
    }

    key = f"{after.guild.id}:{after.channel.id}:{after.id}"
    edit_db.set(key, data)

# Command loading system
async def load_commands():
    command_categories = ['fun', 'utility', 'moderation', 'nsfw', 'web']

    for category in command_categories:
        try:
            files = __import__(f"commands.{category}", fromlist=['']).__path__
        except Exception as e:
            print(f"Category {category} could not be imported: {e}")
            continue

        for _, module_name, ispkg in pkgutil.iter_modules(files):
            if not ispkg and not module_name.startswith('_'):
                try:
                    module = __import__(f'commands.{category}.{module_name}', fromlist=['setup'])
                    if hasattr(module, 'setup'):
                        await module.setup(bot)
                        print(f"✅ Loaded command: {module_name}")
                    else:
                        print(f"⚠️ No setup() in: {module_name}")
                except Exception as e:
                    print(f"❌ Failed to load {module_name}: {e}")


# Error handler
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        return
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send("You don't have permission to use this command.")
    elif isinstance(error, commands.CommandOnCooldown):
        await ctx.send(f"This command is on cooldown. Try again in {error.retry_after:.2f} seconds.")
    else:
        print(f"Error in command {ctx.command}: {error}")

@bot.listen("on_command_completion")
async def delete_command_message(ctx):
    try:
        if configdata.get("delete_commands", True):
            await ctx.message.delete()
    except:
        pass


def replace_args_simple(text, args):
    def replacer(match):
        try:
            index = int(match.group(1))
            return args[index] if 0 <= index < len(args) else ""
        except (ValueError, IndexError):
            return ""
    return re.sub(r"\$arg\[(\d+)\]", replacer, text)

# --- Helper function for $random(min-max) replacement ---

def replace_random(text: Union[str, None]) -> Union[str, None]:
    """Replace $random[...] patterns in text with random values.
    
    Supports two formats:
    1. $random[min-max] → Random number between min and max
    2. $random[opt1,opt2,opt3] → Random choice from options
    
    Args:
        text: Input string containing $random patterns
        
    Returns:
        String with patterns replaced, or original input if not a string
    """
    if not isinstance(text, str):
        return text

    # ✅ Uses standard square brackets instead of hidden chars
    pattern = r"\$random\[(\d+)-(\d+)\]|\$random\[([^\]]+)\]"

    def random_replacer(match: re.Match) -> str:
        try:
            # Case 1: $random[1-10] → Random number
            if match.group(1) and match.group(2):
                min_val = int(match.group(1))
                max_val = int(match.group(2))
                if min_val > max_val:
                    min_val, max_val = max_val, min_val  # Fix reversed ranges
                return str(random.randint(min_val, max_val))
            
            # Case 2: $random[yes,no,maybe] → Random choice
            elif match.group(3):
                options = [opt.strip() for opt in match.group(3).split(',') if opt.strip()]
                if options:
                    return random.choice(options)
        except (ValueError, AttributeError):
            pass  # Fallback to original if error
        
        return match.group(0)  # Return original if invalid pattern

    return re.sub(pattern, random_replacer, text)

# --- Helper function for $calc(expression) replacement ---
def replace_calc(text):
    def calc_replacer(match):
        expr = match.group(1)
        try:
            # Safe eval using eval with limited globals
            result = str(eval(expr, {"__builtins__": None}, {}))
            return result
        except Exception:
            return "InvalidCalc"
    
    return re.sub(r"\$calc\[([^\]]+)\]", calc_replacer, text)

def parse_variables(text, message, args=None):
    if args is None:
        args = []

    now = datetime.datetime.now()

    # Prepare args strings for replacement, including mentions etc
    processed_args = []
    for arg in args:
        if isinstance(arg, (discord.Member, discord.User)):
            processed_args.append(f"@{arg.name}")
        elif isinstance(arg, discord.TextChannel):
            processed_args.append(f"#{arg.name}")
        elif isinstance(arg, discord.Role):
            processed_args.append(f"@{arg.name}")
        else:
            processed_args.append(str(arg))
    args = processed_args

    # Get mentions
    mentioned_user = message.mentions[0] if message.mentions else None
    mentioned_channel = message.channel_mentions[0] if message.channel_mentions else None

    replacements = {
        "$cmdUserId": str(message.author.id),
        "$cmdUserName": message.author.name,
        "$cmdUserTag": str(message.author),
        "$cmdUserAvatar": str(message.author.display_avatar.url),

        "$botUserId": str(bot.user.id),
        "$botUserName": str(bot.user.name),

        "$cmdChannelId": str(message.channel.id),
        "$cmdChannelName": getattr(message.channel, "name", "DM"),

        "$cmdGuildId": str(message.guild.id) if message.guild else "",
        "$cmdGuildName": str(message.guild.name) if message.guild else "DM",

        "$mentionedUserId": str(mentioned_user.id) if mentioned_user else "",
        "$mentionedUserName": mentioned_user.name if mentioned_user else "",
        "$mentionedUserTag": str(mentioned_user) if mentioned_user else "",
        "$mentionedUserAvatar": str(mentioned_user.display_avatar.url) if mentioned_user else "",

        "$mentionedChannelId": str(mentioned_channel.id) if mentioned_channel else "",
        "$mentionedChannelName": mentioned_channel.name if mentioned_channel else "",

        "$args": " ".join(args),
        "$time": now.strftime("%H:%M:%S"),
        "$date": now.strftime("%Y-%m-%d"),
        "$year": str(now.year),
        "$month": str(now.month),
        "$day": str(now.day),
        "$weekday": now.strftime("%A"),
        
    }
    # Replace simple variables (like $cmdUserName, $time etc)
    for var, value in replacements.items():
        text = text.replace(var, value)
    # Replace $args[n] variables
    text = replace_args_simple(text, args)
    # Replace $random(min-max)
    text = replace_random(text)
    # Replace $calc(...)
    text = replace_calc(text)
    return text

def monitor_stop_file():
    while not bot.is_closed():
        if flag_check.is_flag_present():
            print(f"🛑 ROCK Stopped.")
            os.remove(flag_check.get_flag_path())
            asyncio.run_coroutine_threadsafe(bot.close(), bot.loop)
            break
        asyncio.run(asyncio.sleep(3))

def main():
    # Setup event loop
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(load_commands())
    # Initialize FlagChecker
    # Start monitor thread
    threading.Thread(target=monitor_stop_file, daemon=True).start()
    # Run bot
    bot.run(TOKEN)

main()