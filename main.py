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
    await ctx.send(f'''Extra Selfbot
    ```Extra Help
    No Perm: {prefix}noperm
    Embed Perms: {prefix}perm
    
Electro#7777```''')


@user.command(pass_context=True)
async def perm(ctx):
    embed=discord.Embed(title="Extra Help", color=0x5cff67)
    embed.add_field(name="Spam", value={prefix}"`spam <amt> <msg>`", inline=True)
    embed.add_field(name="MassDM", value=f"`{prefix}massdm`", inline=True)
    embed.add_field(name="Meme", value=f"`{prefix}meme`", inline=True)
    embed.add_field(name="SetPresence", value=f"`{prefix}setpresence <name>`", inline=True)    
    embed.set_footer(text=f"Made by; Electro#7777")
    await ctx.send(embed=embed)

@user.command(pass_context=True)
async def noperm(ctx):
    await ctx.send(f'''Extra Selfbot
    ```Extra Help
    Spam: {prefix}spam <amt> <msg>
    Mass DM:{prefix}massdm
    Meme:{prefix}meme
    
Extra On Top```''')



user.run(token, bot=False)
