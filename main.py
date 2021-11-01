import discord,asyncio,youtube_dl,json
from discord.ext import commands
import os


def get_prefix(bot, message):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)
    return prefixes[str(message.guild.id)]


intents= discord.Intents.default()
intents.members = True
bot=commands.Bot(command_prefix = get_prefix, help_command = None, intents=intents)
#json.prefixes
@bot.event
async def on_guild_join(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(guild.id)] = "-"

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

@bot.event
async def on_guild_remove(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes.pop(str(guild.id))

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

@bot.command()
@commands.has_permissions(manage_guild=True)
async def changeprefix(ctx, prefix=''):
    try:
        if len(prefix)==0 or prefix==" " or len(prefix)>1:
            embed=discord.Embed(title="**Command triggered Insufficient/Wrong Data**", description='''Please give a appropriate single charcter
**Example**: <prefix>changeprefix *''', colour=0x3498db)
            mymessage = await ctx.send(embed=embed)
            await asyncio.sleep(4)
            await mymessage.delete()

        else:
            if prefix.isdigit()==True:

                embed=discord.Embed(title="**Command triggered Insufficient/Wrong Data**", description='''Please give a appropriate single charcter
**Example**: <prefix>changeprefix *''', colour=0x3498db)
                mymessage = await ctx.send(embed=embed)
                await asyncio.sleep(4)
                await mymessage.delete()

            else:
                with open('prefixes.json', 'r') as f:
                    prefixes = json.load(f)

                prefixes[str(ctx.guild.id)] = prefix

                with open('prefixes.json', 'w') as f:
                    json.dump(prefixes, f, indent=4)
                embed=discord.Embed(title=f'**Prefix is changed to **{prefix}', colour=0xe91e63)
                await ctx.send(embed=embed)

    except:
        embed=discord.Embed(title="**Command triggered Insufficient/Wrong Data**", description='''Please give a appropriate single charcter
**Example**: <prefix>changeprefix *''', colour=0x3498db)
        mymessage = await ctx.send(embed=embed)
        await asyncio.sleep(4)
        await mymessage.delete()



exts=['help','music','info','moderation','extra'] #Add your Cog extensions here


@bot.event
async def on_ready():
    activity = discord.Game(name=f'-help in {len(bot.guilds)} servers.', type=3)
    await bot.change_presence(status=discord.Status.online, activity=activity)
    print(bot.user.name)


for i in exts:
    bot.load_extension(i)


bot.run("ODY1ODc2MjYwNzQ4MTMyMzUz.YPKYGw.g8tU49N1Xku3HihLF6ze-FPNydo")
