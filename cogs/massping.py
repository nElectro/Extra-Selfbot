import discord
from discord.ext import commands
import asyncio

class MassPing(commands.Cog):

    def __init__(self, user):
        self.user = user

    @commands.command(pass_context=True)
    async def massping(self, ctx, userid):
        for i in range(1000):
            await asyncio.sleep(0.1)
            await ctx.send(f"<@{userid}>", delete_after=0.001)    

    @commands.command(pass_context=True)
    async def masseveryone(self, ctx):
        for i in range(1000):
            await ctx.send("@everyone", delete_after=0.1)        
            
    @commands.command(pass_context=True)
    async def masshere(self, ctx):
         for i in range(1000):
        await ctx.send("@here", delete_after=0.1)

def setup(user):
    user.add_cog(MassPing(user))   
