import discord
from discord.ext import commands
from discord.commands import slash_command, Option

prefix = '.'
token = 'MTAxNjIzMjQwNTE0NjgwMDE4OQ.GggG0e.4T22YxTkGr6vdpw_sgrS7wo8t6W85niOueqQZM'

client = commands.Bot(command_prefix=prefix, help_command=None, intents=intents)

THEME_COLOUR = discord.Colour.blurple()
ERROR_COLOUR = discord.Colour.red()

class ping(commands.Cog):
    def __init__(self, client):
        self.client = client
        
#сам код пинга
    @slash_command(guild_ids=[GUILD_IDS], name="ping", description="просмотреть пинг бота")
    async def ping(self,ctx):
        pingEm = discord.Embed(title=f"пинг понг", description=f"задержка бота : `{round(self.client.latency * 1000)} ms`", color=THEME_COLOUR)
        await ctx.respond(embed=pingEm)
#код ошибки команды пинга
    @ping.error
    async def ping_error(self, ctx, error):
        pingErEm = discord.Embed(title=f" ошибка команды", description=f"похоже чтото пошло не так. попробуйте пожже", color=ERROR_COLOUR)
        await ctx.respond(embed=pingErEm, ephemeral=True)

from random import choice
rand = random.choice(["Удачно","Неудачно"])
@client.command()
async def удача(ctx,*,text = None):
    if text is None:
        embed=discord.Embed(title="❌|Ошибка",
        description="Вы не ввели вопрос!",
        color = discord.Colour.red())
    else:
        embed = discord.Embed(title="🍀|Удача",
        description=f"""Вопрос: {text}
Ответ: {rand}""",color = discord.Colour.orange())
    embed.set_footer(text=f"{ctx.author.name}")
    await ctx.send(embed=embed)

client.run(token)