import discord
from discord.ext import commands
import youtube_dl
import time

class music(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command()
  async def setprefix(ctx, prefix):
    commands.Bot.command_prefix=prefix
    
  @commands.command()
  async def join(self,ctx):
    voice_channel = ctx.author.voice.channel
    if ctx.author.voice is None:
      await ctx.send("You are not in a voice channel.")
      voice_channel = ctx.author.voice.channel
    if ctx.voice_client is None:
      await voice_channel.connect()
    else:
      await ctx.voice_client.move_to(voice_channel)
   
  @commands.command()
  async def kidnap(self,ctx):
    voice_channel = ctx.author.voice.channel
    if ctx.author.voice is None:
      await ctx.send("You are not in a voice channel.")
      voice_channel = ctx.author.voice.channel
    if ctx.voice_client is None:
      await voice_channel.connect()
    else:
      await ctx.voice_client.move_to(voice_channel)


  @commands.command()
  async def disconnect(self,ctx):
    await ctx.voice_client.disconnect()
  
  @commands.command()
  async def play(self,ctx,url):
    #voice_client = discord.utils.get(self.client.voice_clients, guild=ctx.guild)
    if ctx.author.voice == None:
      await ctx.send("You are not in a voice channel.")
    else:
      if ctx.voice_client == None:
        voice_channel = ctx.author.voice.channel
        await voice_channel.connect()
        FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
        YDL_OPTIONS = {'format':'bestaudio'}
        vc = ctx.voice_client
        with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
          embedVar = discord.Embed(title="Downloading webpage...", description="Using youtube-dl", color=0xff0000)
          await ctx.send(embed=embedVar)
          info = ydl.extract_info(url, download=False)
          url2 = info['formats'][0]['url']
          source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
          vc.play(source)
      else:
          ctx.voice_client.stop()
          FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
          YDL_OPTIONS = {'format':'bestaudio'}
          vc = ctx.voice_client
          with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
            embedVar = discord.Embed(title="Downloading webpage...", description="Using youtube-dl", color=0xff0000)
            await ctx.send(embed=embedVar)
            info = ydl.extract_info(url, download=False)
            url2 = info['formats'][0]['url']
            source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
            vc.play(source)

  @commands.command()
  async def p(self,ctx,url):
    #voice_client = discord.utils.get(self.client.voice_clients, guild=ctx.guild)
    if ctx.author.voice == None:
      await ctx.send("You are not in a voice channel.")
    else:
      if ctx.voice_client == None:
        voice_channel = ctx.author.voice.channel
        await voice_channel.connect()
        FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
        YDL_OPTIONS = {'format':'bestaudio'}
        vc = ctx.voice_client
        with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
          embedVar = discord.Embed(title="Downloading webpage...", description="Using youtube-dl", color=0xff0000)
          await ctx.send(embed=embedVar)
          info = ydl.extract_info(url, download=False)
          url2 = info['formats'][0]['url']
          source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
          vc.play(source)
      else:
          ctx.voice_client.stop()
          FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
          YDL_OPTIONS = {'format':'bestaudio'}
          vc = ctx.voice_client
          with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
            embedVar = discord.Embed(title="Downloading webpage...", description="Using youtube-dl", color=0xff0000)
            await ctx.send(embed=embedVar)
            info = ydl.extract_info(url, download=False)
            url2 = info['formats'][0]['url']
            source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
            vc.play(source)
  
  @commands.command()
  async def pause(self,ctx):
    await ctx.voice_client.pause()
    await ctx.send("Paused current song.")
  
  @commands.command()
  async def resume(self,ctx):
    await ctx.voice_client.resume()
    await ctx.send("Resumed current song.")
    
  @commands.command()
  async def cmds(self,ctx):
    embedVar = discord.Embed(title="Commands", description="Commands for bot07", color=0xff0000)
    embedVar.add_field(name="!join", value="Move bot to your vc.", inline=False)
    embedVar.add_field(name="!play", value="Only plays youtube links for now.", inline=False)
    embedVar.add_field(name="!pause", value="Pause music.", inline=False)
    embedVar.add_field(name="!resume", value="Resume music.", inline=False)
    embedVar.add_field(name="!disconnect", value="Disconnect the bot.", inline=False)
    await ctx.send(embed=embedVar)
    
  @commands.command()  
  async def on_command_error(ctx, error):
      if isinstance(error, commands.CommandNotFound):
          embedVar = discord.Embed(title="Invalid command", description="Use !cmds for a list of commands", color=0xff0000)
          await ctx.send(embed=embedVar)

 


def setup(client):
  client.add_cog(music(client))
