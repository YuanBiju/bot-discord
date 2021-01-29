import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
from meme_generator import meme_output

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.members = True

GUILD = 'Test'

client = commands.Bot(command_prefix='$', intents=intents)

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(client.user)
    print(f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})')

    '''
    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')
    '''
@client.command()
async def info(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}", description="Lorem Ipsum asdasd", color=discord.Color.blue())
    embed.add_field(name="Server created at", value=f"{ctx.guild.created_at}")
    await ctx.send(embed=embed)

@client.command()
async def slap(ctx):
    member = ctx.message.author
    mentions = ctx.message.mentions
    print(mentions)
    user_avatar = member.avatar_url_as(format=None, static_format='png', size=64)
    if len(mentions) == 0:
        mention_avatar = client.user.avatar_url_as(format=None, static_format='png', size=64)
        meme = meme_output("slap",user_avatar,mention_avatar)
        with open("imgs_temp/73ca653a156e4ad90d2e80a49cd43ba2.jpg",'rb') as fh:
            f = discord.File(fh, filename = "73ca653a156e4ad90d2e80a49cd43ba2.jpg")
        await ctx.send(file=f)
    else:
        for mention in mentions:
            mention_avatar = mention.avatar_url_as(format=None, static_format='png', size=64)
            meme = meme_output("slap",user_avatar,mention_avatar)
            with open("imgs_temp/73ca653a156e4ad90d2e80a49cd43ba2.jpg",'rb') as fh:
                f = discord.File(fh, filename = "73ca653a156e4ad90d2e80a49cd43ba2.jpg")
            await ctx.send(file=f)

@client.command()
async def crotchkick(ctx):
    member = ctx.message.author
    mentions = ctx.message.mentions
    print(mentions)
    user_avatar = member.avatar_url_as(format=None, static_format='png', size=64)
    if len(mentions) == 0:
        mention_avatar = client.user.avatar_url_as(format=None, static_format='png', size=64)
        meme = meme_output("crotchkick",user_avatar,mention_avatar)
        with open("imgs_temp/1wz0x7.jpg",'rb') as fh:
            f = discord.File(fh, filename = "1wz0x7.jpg")
        await ctx.send(file=f)
    else:
        for mention in mentions:
            mention_avatar = mention.avatar_url_as(format=None, static_format='png', size=64)
            meme = meme_output("crotchkick",user_avatar,mention_avatar)
            with open("imgs_temp/1wz0x7.jpg",'rb') as fh:
                f = discord.File(fh, filename = "1wz0x7.jpg")
            await ctx.send(file=f)
        
@client.command()
async def facekick(ctx):
    member = ctx.message.author
    mentions = ctx.message.mentions
    print(mentions)
    user_avatar = member.avatar_url_as(format=None, static_format='png', size=64)
    if len(mentions) == 0:
        mention_avatar = client.user.avatar_url_as(format=None, static_format='png', size=64)
        meme = meme_output("facekick",user_avatar,mention_avatar)
        with open("imgs_temp/8lvi0.jpg",'rb') as fh:
            f = discord.File(fh, filename = "8lvi0.jpg.jpg")
        await ctx.send(file=f)
    else:
        for mention in mentions:
            mention_avatar = mention.avatar_url_as(format=None, static_format='png', size=64)
            meme = meme_output("facekick",user_avatar,mention_avatar)
            with open("imgs_temp/8lvi0.jpg",'rb') as fh:
                f = discord.File(fh, filename = "8lvi0.jpg")
            await ctx.send(file=f)
'''
@client.command()
async def play(ctx, url_:str):
    voice_channel = discord.utils.get(ctx.guild.voice_channels, name = 'Music')
    voice = discord.utils.get(client.voice_clients, GUILD = ctx.guild)
    await voice_channel.connect()

@client.command()
async deff leave(ctx):
    voice_channel = discord.utils.get(ctx.guild.voice_channels, name = 'Music')
    voice = discord.utils.get(client.voice_clients, GUILD = ctx.guild)
    if voice.is_connected():
        await voice_channel.connect()
    else:
        await ctx.send('Not connected')
'''

client.run(TOKEN)
