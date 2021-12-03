import discord
from discord.ext import commands

class SetPresence(commands.Cog):

    def __init__(self, user):
        self.user = user

    @commands.command(pass_context=True)
    async def setpresence(self, ctx, *, presence):
            await self.user.change_presence(status=discord.Status.idle, activity=discord.Game(f'{presence}'))


def setup(user):
    user.add_cog(SetPresence(user)) 