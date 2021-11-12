import discord, aiohttp, asyncio
from discord.ext import commands
from discord_components import DiscordComponents, Button, ButtonStyle, Select, SelectOption, ComponentsBot

class Helping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        DiscordComponents(bot)
#Events
#  @commands.Cog.listener()


#Commands
    @commands.command()
    async def waifu(self,ctx):
        member=ctx.author
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://api.waifu.im/sfw/waifu/?exclude=3867126be8e260b5.jpeg,ca52928d43b30d6a&gif=false") as rep:
                api= await rep.json()
                if rep.status != 200:
                    ctx.send('Looks like an unexpected error has occurred❗❗')
                else:
                    url=api.get('tags')[0].get('images')[0].get('url')
                    col=api.get('tags')[0].get('images')[0].get('dominant_color')
                    embed=discord.Embed(title='Waifu',colour=discord.Color(int(col.replace("#",""), 16)))
                    embed.set_image(url=url)
                    embed.set_footer(text=f'''Requested by:{member}''', icon_url=member.avatar_url)
                    msg=await ctx.send(embed=embed, components=[Button(label='', custom_id="button1",emoji=self.bot.get_emoji(888657398213017660), style=ButtonStyle.red)])
                    while True:
                        try:
                            interaction = await self.bot.wait_for(
                                'button_click',
                                check=lambda inter: inter.message.id == msg.id and inter.author.id == ctx.author.id,
                                timeout=120)
                            if interaction.author.id == ctx.author.id:
                                await msg.delete()
                                break
                        except asyncio.TimeoutError:
                            await msg.edit(components=[])

    @commands.command()
    async def maid(self,ctx):
        member=ctx.author
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://api.waifu.im/sfw/maid/?exclude=3867126be8e260b5.jpeg,ca52928d43b30d6a&gif=false") as rep:
                api= await rep.json()
                if rep.status != 200:
                    ctx.send('Looks like an unexpected error has occurred❗❗')
                else:
                    url=api.get('tags')[0].get('images')[0].get('url')
                    col=api.get('tags')[0].get('images')[0].get('dominant_color')
                    embed=discord.Embed(title='Maid',colour=discord.Color(int(col.replace("#",""), 16)))
                    embed.set_image(url=url)
                    embed.set_footer(text=f'''Requested by:{member}''', icon_url=member.avatar_url)
                    msg=await ctx.send(embed=embed, components=[Button(label='', custom_id="button1",emoji=self.bot.get_emoji(888657398213017660), style=ButtonStyle.red)])
                    while True:
                        try:
                            interaction = await self.bot.wait_for(
                                'button_click',
                                check=lambda inter: inter.message.id == msg.id and inter.author.id == ctx.author.id,
                                timeout=120)
                            if interaction.author.id == ctx.author.id:
                                await msg.delete()
                                break
                        except asyncio.TimeoutError:
                            await msg.edit(components=[])

    @commands.command()
    async def random(self,ctx):
        member=ctx.author
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://api.waifu.im/sfw/all/?exclude=3867126be8e260b5.jpeg,ca52928d43b30d6a&gif=false") as rep:
                api= await rep.json()
                if rep.status != 200:
                    ctx.send('Looks like an unexpected error has occurred❗❗')
                else:
                    url=api.get('tags')[0].get('images')[0].get('url')
                    col=api.get('tags')[0].get('images')[0].get('dominant_color')
                    embed=discord.Embed(title='Random Waifu',colour=discord.Color(int(col.replace("#",""), 16)))
                    embed.set_image(url=url)
                    embed.set_footer(text=f'''Requested by:{member}''', icon_url=member.avatar_url)
                    msg=await ctx.send(embed=embed, components=[Button(label='', custom_id="button1",emoji=self.bot.get_emoji(888657398213017660), style=ButtonStyle.red)])
                    while True:
                        try:
                            interaction = await self.bot.wait_for(
                                'button_click',
                                check=lambda inter: inter.message.id == msg.id and inter.author.id == ctx.author.id,
                                timeout=120)
                            if interaction.author.id == ctx.author.id:
                                await msg.delete()
                                break
                        except asyncio.TimeoutError:
                            await msg.edit(components=[])
                            
        @commands.command()
        async def neko(self, ctx):
            member=ctx.author
            r = requests.get("https://neko-love.xyz/api/v1/neko")
            if r.status_code != 200:
            msg1 = "An error has occurred"
            else:
                msg1=r.json()["url"]
            embed=discord.Embed(title='Waifu',colour=0xe91e63)
            embed.set_image(url=msg1)
            embed.set_footer(text=f'''Requested by:{member}''', icon_url=member.avatar_url)
            msg=await ctx.send(embed=embed, components=[Button(label='',emoji=self.bot.get_emoji(888657398213017660), style=ButtonStyle.red)])
            while True:
                try:
                    interaction = await self.bot.wait_for(
                            'button_click',
                            check=lambda inter: inter.message.id == msg.id and inter.author.id == ctx.author.id,
                            timeout=120)
                    if interaction.author.id == ctx.author.id:
                        await msg.delete()
                        break
                except asyncio.TimeoutError:
                    await msg.edit(components=[])

def setup(bot):
    bot.add_cog(Helping(bot))
