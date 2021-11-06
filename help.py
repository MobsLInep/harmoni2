import discord
from discord.ext import commands

class Helping(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
#Events
#  @commands.Cog.listener()


#Commands
  @commands.command()
  #help
  async def help(self, ctx, argument='', member: discord.Member=None):
      member=ctx.author
      if argument.lower()=='utility':
          embed=discord.Embed(title="Utility Commands", description='''`-changeprefix [new prefix]`
Changes the prefix of Harmoni for the server

`-whois [member mention/id]`
Gives information about the user

`-avatar (optional:Member)`
Get the avatar of yourself or another user.

`-serverinfo`
Gives information about the guild
''', color=0x109319)
          await ctx.send(embed=embed)
      elif argument.lower()=='moderator':
          embed=discord.Embed(title="Moderator Commands", description='''`-ban [member] (optional:reason)`
Bans a member from the server.

`-unban [member]`
Unbans a pre-banned member from the server.

`-kick [member] (optional reason)`
Kicks a member from the server.

`-mute [member] (optional:reason)`
Temporarily mutes a member in the server.
''', color=0x109319)
          await ctx.send(embed=embed)
      elif argument.lower()=='waifu' or argument.lower()=='anime':
          embed=discord.Embed(title="Anime/Waifu Commands", description='''`-waifu`
Display an image with the "waifu" tag.

`-maid`
Display an image with the "maid" tag.

`-random`
Display an image with the "all" tag.
''', color=0x109319)
          await ctx.send(embed=embed)
      elif argument.lower()=='music':
#`join`, `play`, `pause`, `resume`, `repeat`, `download`, `queue`, `reset`,
# `skip`, `song-info`, `volume`, `stop`, `leave`
          embed=discord.Embed(title="Music Commands(Delayed Music)", description='''`-join`
Joins the voice channel.

`-play [title/youtube url or playlist]`
Plays the song.

`-pause`
Pause the current song

`-resume`
Resumes the current song.

`-repeat`
Loops the current song.

`-download [title/youtube url or playlist]`
Downloads the song in mp3 format and sends in it discord.

`-queue`
Shows up the current queue.

`-reset`
Starts the song from beginning.

`-skip`
Skips the current song playing and plays the next soong in the queue if any.

`-song-info`
Gives info of the current song playing.

`-volume [integer]`
Adjust volume of Harmoni. [Default=50]

`-stop`
Stops the current song playing.

`-leave`
Leaves the voice channel.''', color=0x109319)
          await ctx.send(embed=embed)
      elif argument.lower()=='aboutdev':
          embed=discord.Embed(title="About Commands", description='''`-aboutdev`
Gives a general info about the developer of Harmoni Bot.

`-ping`
Tells you the current latency of Hormoni bot.

`-invite`
Gives a invite link for Harmoni Bot.
''', color=0x109319)
          await ctx.send(embed=embed)
      else:
          embed=discord.Embed(title="Harmoni Bot", description='''**All Harmoni Commands Categories:**
You could type .help <command_category> for more info.''', color=0x109319)
          embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/865876260748132353/17cc0e8ff24cbcdf4c2ea1a0f8456206.png?size=128")
          embed.add_field(name="1. :gear:Utility:", value='''`whois`, `avatar`, `serverinfo`

Type "-help utility" will give more info about all the bot commands.''', inline=False)
          embed.add_field(name="2. :hammer:Moderator:", value='''`ban`, `kick`, `mute`, `purge`

Type "-help moderator" to get more info about all the moderator commands.''', inline=False)
          embed.add_field(name="3. :musical_note:Music(Delayed):", value='''`join`, `play`, `pause`, `resume`, `repeat`, `download`, `queue`, `reset`, `skip`, `song-info`, `volume`, `stop`, `leave`

Type "-help waifu" to get more info about all the music commands.''', inline=False)
          embed.add_field(name="4. Anime/Waifu:", value='''`waifu`, `maid`, `random`

Type "-help music" to get more info about all the music commands.''', inline=False)
          embed.add_field(name="5. :robot:About Bot and Dev(Just for fun)", value='''`aboutdev`, `ping`, `invite`

Type "-help aboutdev" to get more info about all the About commands.
[**Invite Link**](https://discord.com/api/oauth2/authorize?client_id=865876260748132353&permissions=8&scope=bot)  ||   [**Support Server**](https://discord.gg/ReTdc9dFuP)''', inline=False)
          embed.set_footer(text=f'''Harmoni Bot version-Beta 1.4. More features will be added in the upcoming version.
Requested by:{member}''', icon_url=member.avatar_url)
          await ctx.send(embed=embed)

def setup(bot):
  bot.add_cog(Helping(bot))
