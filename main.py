import discord
from discord.ext import commands
from colorama import * 
import json
import os

with open('./json/config.json') as f:
    config = json.load(f)

token = config.get('token')
prefix = config.get('prefix')


user = commands.Bot(command_prefix=prefix, self_bot=True)
user.remove_command('help')
for filename in os.listdir('./cogs'):
	if filename.endswith('.py'):
		user.load_extension(f'cogs.{filename[:-3]}')

@user.event
async def on_ready():
    print("Online")

@user.command(pass_context=True)
async def help(ctx):
    await ctx.send('''Extra Selfbot
    ```Extra Help
    No Perm: z!help noperm
    Embed Perms: z!perm
    
Electro#7777```''')


@user.command(pass_context=True)
async def perm(ctx):
    embed=discord.Embed(title="Extra Help", color=0x5cff67)
    embed.add_field(name="Spam", value="`z!spam <amt> <msg>`", inline=True)
    embed.add_field(name="Nuke", value="`z!nuke` (Need Perms)", inline=True)
    embed.add_field(name="MassDM", value="`z!massdm`", inline=True)
    embed.add_field(name="Meme", value="`z!meme`", inline=True)
    embed.add_field(name="SetPresence", value="`z!setpresence <name>`", inline=True)    
    embed.set_footer(text="Buy Extra: tiys.tk/extra | Electro#7777")
    await ctx.send(embed=embed)

@user.command(pass_context=True)
async def noperm(ctx):
    await ctx.send('''Extra Selfbot
    ```Extra Help
    Spam: z!spam <amt> <msg>
    Nuke: z!nuke
    Mass DM: z!massdm
    Meme: z!meme
    
Extra On Top```''')



user.run(token, bot=False)