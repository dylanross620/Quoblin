import json
import os.path

import asyncio
import discord
from discord.ext import commands

class DiscordBot(commands.Cog):
    def __init__(self, bot, settings):
        self.bot = bot
        self.admin_roles = settings['admin_roles']

    @commands.command()
    async def quote(self, ctx, *, command=None):
        if command is None:
            # User just typed '!quote', so give a random quote
            await self.send_random_quote(ctx)
        else:
            command = command.strip()

            roles = ctx.author.roles

            args = command.split(' ')
            resp = self.bot.quote_commands(args[0], args[1:], ctx.author.display_name, self.is_admin(roles))
            
            await ctx.reply(resp)

    @commands.command()
    async def roll(self, ctx, *, command=''):
        command = command.strip().lower()
        cmd = command.split(' ')[0]
        
        await ctx.reply(self.bot.roll_dice(cmd)[0])

    # Helper function to handle the case where a user wants a random quote
    async def send_random_quote(self, ctx):
        num, quote = self.bot.get_random_quote()
        if num == -1:
            await ctx.reply(quote)
        else:
            await ctx.reply(f"Quote #{num+1}: {quote}")

    # Helper function to figure out if a user that has the specified roles is considered an admin
    def is_admin(self, roles):
        is_admin = False
        for role in roles:
            if role.name in self.admin_roles:
                is_admin = True
                break

        return is_admin

async def create_bot(bot, settings):
    intents = discord.Intents.default()
    intents.message_content = True

    discord_bot = commands.Bot(command_prefix='!', intents=intents)

    await discord_bot.add_cog(DiscordBot(bot, settings))

    @discord_bot.event
    async def on_ready():
        print('Ready')

    return discord_bot

def get_settings():
    # Attempt to load settings from 'discord_settings.json'
    if os.path.exists('discord_settings.json'):
        # File attempts, so load it
        with open('discord_settings.json', 'r') as f:
            settings = json.load(f)

        print('Successfully loaded Discord settings')
    else:
        # File doesn't exist. Time to ask the user for settings and save them
        print('Settings not found. Entering Discord setup')

        bot_token = input('Enter your Discord bot token: ').strip()
        admin_roles = input('Enter the name of admin Discord roles (comma separated): ').strip().split(',')

        settings = {
            'bot_token': bot_token,
            'admin_roles': admin_roles
        }

        with open('discord_settings.json', 'w') as f:
            json.dump(settings, f)
        
        print('Successfully saved settings to discord_settings.json')

    return settings

def start(bot):
    settings = get_settings()

    discord_bot = asyncio.run(create_bot(bot, settings))

    discord_bot.run(settings['bot_token'])
