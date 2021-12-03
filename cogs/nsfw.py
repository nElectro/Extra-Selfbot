import discord
from discord.ext import commands
import aiohttp
import random

class Nsfw(commands.Cog):

    def __init__(self, user):
        self.user = user
        
    @commands.command(pass_context=True)
    @commands.is_nsfw()
    async def porn(self, ctx):

        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://www.reddit.com/r/nsfw/new.json') as r:
                res = await r.json()
                await ctx.send(res['data']['children'] [random.randint(0, 25)]['data']['url'])

def setup(user):
    user.add_cog(Nsfw(user)) 