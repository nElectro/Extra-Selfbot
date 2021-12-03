import discord
from discord.ext import commands

class Spam(commands.Cog):

    def __init__(self, user):
        self.user = user

    @commands.command(name='spam', help='Spams the input message for x number of times')
    async def spam(self, ctx, *, message):
        for i in range(10000): # Do the next thing amount times
            await ctx.send(message)

def setup(user):
    user.add_cog(Spam(user))   