import discord
from bot_logic import gen_pass
from discord.ext import commands

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
bot = commands.Bot(command_prefix="$",intents=intents)

@bot.event
async def on_ready():
    print(f'Acabamos de recargar como {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send("Hi")

@bot.command()
async def chau(ctx):
    await ctx.send("chao")

@bot.command()
async def password(ctx, PW=10):
    await ctx.send(gen_pass(int(PW))) 

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def sumar(ctx, left: int, right: int):
    await ctx.send(left + right)


bot.run("XD")
