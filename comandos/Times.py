from discord.ext import commands
import sqlite3

class TimeCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def time(self, ctx, *jogadores):
        db_connection = sqlite3.connect('times.db')  # Conexão com o banco de dados
        cursor = db_connection.cursor()
        jogadores_str = ' '.join(jogadores)
        cursor.execute('INSERT INTO times (jogadores) VALUES (?)', (jogadores_str,))
        db_connection.commit()
        db_connection.close()
        await ctx.send(f'Time adicionado: {jogadores_str}')

    @commands.command()
    async def times(self, ctx):
        db_connection = sqlite3.connect('times.db')  # Conexão com o banco de dados
        cursor = db_connection.cursor()
        cursor.execute('SELECT * FROM times')
        rows = cursor.fetchall()
        response = 'Times registrados:\n'
        for row in rows:
            response += f'Time {row[0]}: {row[1]}\n'
        db_connection.close()
        await ctx.send(response)

async def setup(bot):
    await bot.add_cog(TimeCog(bot))
