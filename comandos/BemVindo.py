
from discord.ext import commands

class mensagemEntrada(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        canal = member.guild.system_channel
        await canal.send(f"Seja bem vido {member.mention}! Veja as Regras em #Regras")

async def setup(bot):
    await bot.add_cog(mensagemEntrada(bot))

