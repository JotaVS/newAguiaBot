from discord.ext import commands
from discord import Intents
import os
import sqlite3


bot = commands.Bot(command_prefix='!', intents=Intents.all())

@bot.event
async def on_ready():
    await setup_database()
    await print_times()
    print(f'Bot conectado como {bot.user.name}')
    for filename in os.listdir('./comandos'):
        if filename.endswith('.py'):
            await bot.load_extension(f'comandos.{filename[:-3]}')

async def setup_database():
    db_connection = sqlite3.connect('times.db')
    cursor = db_connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS times
                      (time_id INTEGER PRIMARY KEY AUTOINCREMENT, jogadores TEXT)''')
    db_connection.commit()
    db_connection.close()


async def print_times():
    db_connection = sqlite3.connect('times.db')
    cursor = db_connection.cursor()
    cursor.execute('SELECT * FROM times')
    rows = cursor.fetchall()
    db_connection.close()

bot.run('Insira o Token Aqui')
