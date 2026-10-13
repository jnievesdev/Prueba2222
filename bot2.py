import discord 
from discord.ext import commands
from bot_logic import gen_pass

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as ({bot.user.id})')
    print('------')
    
@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user.name}!')
    
@bot.command()
async def bye(ctx):
    await ctx.send("\U0001f642")
    
@bot.command()
async def password(ctx):
    length = int(input("Enter the length of password: "))
    await ctx.send(gen_pass(length))

@bot.command()
async def chiste(ctx):
    await ctx.send("¿Por qué los programadores confunden Halloween con Navidad? Porque OCT 31 = DEC 25.")
bot.run('')
