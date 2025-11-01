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
from gtts import gTTS
import pyfiglet
from dateutil.parser import parse
from dateutil.relativedelta import relativedelta
import whois as whoislib

from config_manager import FlagChecker, ConfigManager, CommandLogManager, ConsoleLogManager, RonDB, CustomCommandsManager


# Global instances (singletons)
flag_check = FlagChecker()
config = ConfigManager()
cmdlog = CommandLogManager()
consolelog = ConsoleLogManager()
bday_db = RonDB("birthdays.json")
ratings_db = RonDB("user_ratings.json")
delete_db = RonDB("deleted_messages.json")
edit_db = RonDB("edited_messages.json")
custom_commands = CustomCommandsManager()
# Helper functions

async def username_from_id(bot, guild, uid: int) -> str:
    """Get username without mention. Handles guild or DM context."""
    member = None
    if guild is not None:
        member = guild.get_member(uid)
        if member is None:
            try:
                member = await guild.fetch_member(uid)
            except discord.NotFound:
                member = None
    if member is None:
        try:
            user = await bot.fetch_user(uid)
            return f"{user.name}#{user.discriminator}"
        except:
            return f"User_{uid}"
    return member.display_name or f"{member.name}#{member.discriminator}"


def get_time():
    """Get current time as ISO format string"""
    return datetime.datetime.now().isoformat()


def format_date(date_obj):
    """Format datetime object to 'dd Mmm YYYY' or return string as is"""
    if isinstance(date_obj, datetime.datetime):
        return date_obj.strftime('%d %b %Y')
    return str(date_obj)


def random_string(length, characters):
    """Generate a random string of given length from characters"""
    return ''.join(random.choice(characters) for _ in range(length))


def format_attachments(message):
    """Format message attachments into list of dicts with metadata"""
    return [{
        "url": att.url,
        "filename": att.filename,
        "size": att.size,
        "content_type": att.content_type
    } for att in message.attachments] if message.attachments else []

def parse_any(date_str):
    """Parse date in DD-MM or DD-MM-YYYY format"""
    try:
        dt = parse(date_str, dayfirst=True)
        has_year = dt.year != 1900  # Default year when not provided
        return dt.date(), has_year
    except ValueError:
        raise ValueError("Invalid date format")

def days_until(target_date):
    """Calculate days until next occurrence of the date"""
    today = datetime.date.today()
    next_date = target_date.replace(year=today.year)
    
    if next_date < today:
        next_date = next_date.replace(year=today.year + 1)
    return (next_date - today).days

def full_age(birth_date):
    """Calculate full age (years, months, days)"""
    today = datetime.date.today()
    delta = relativedelta(today, birth_date)
    return delta.years, delta.months, delta.days
    
def set_rating(self, user_id, category, rating):
    db = self.load()
    if user_id not in db:
        db[user_id] = {}
    db[user_id][category] = rating
    self.save(db)
    return True



def get_prefix():
    configdata = config.load()
    return configdata.get("prefix", "!")

# Explicit exports when using: from functions import *
__all__ = [
    "flag_check",
    "config",
    "cmdlog",
    "consolelog",
    "username_from_id",
    "get_time",
    "format_date",
    "random_string",
    "format_attachments",
    "delete_db",
    "edit_db",
    "ratings_db",
    "bday_db",
    "custom_commands",
    "get_prefix",
    "full_age",
    "days_until",
    "parse_any",
    "set_rating"
]