import discord, random, os
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot you can command to $bikin_sampah and $poster_lingkungan {bot.user}!')

@bot.command()
async def bikin_sampah(ctx):
    img_name = random.choice(os.listdir('kerajinan'))
    with open(f'kerajinan/{img_name}', 'rb') as f:  
        picture = discord.File(f)
        f.close()
    await ctx.send(file=picture)

@bot.command()
async def poster_lingkungan(ctx):
    image_name = random.choice(os.listdir('poster'))
    with open(f'poster/{image_name}', 'rb') as f:  
        picture = discord.File(f)
        f.close()
    await ctx.send(file=picture)
  
bot.run("YOU MUST ADD HERE IN TOKEN!!!")
