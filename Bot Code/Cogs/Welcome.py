# Welcome which welcomes a user to the server and holds a custom image/format to welcome newer users,
# sends then a message in dm for server guide.

import discord
from discord.ext import commands

class Welcome(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.welcome_channel_id = None

    @commands.Cog.listener()
    async def on_member_join(self, member):
        """Sends welcome message to member"""
        channel = self.bot.get_channel(self.welcome_channel_id)
        if channel:
            await member.send(f'Welcome {member.mention} to {member.guild}!')