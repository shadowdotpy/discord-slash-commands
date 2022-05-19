import discord # Normal Discord Environment
from discord.ext import commands # Normal Commands (@bot.command)
from discord_slash import SlashCommand # Slash Commands (@slash.slash)

bot = commands.Bot(command_prefix=".", intents=discord.Intents.all()) 
slash = SlashCommand(bot, sync_commands=True)

@bot.event
async def on_ready():
    print("Bot Ready")


@bot.command()
async def test(ctx):
    await ctx.send("Das ist ein Test Chat Command")


@slash.slash(name="test", description="Ein Test Command")
async def test(ctx):
    await ctx.send("Das ist ein Test Slash Command")


bot.run("DEIN_TOKEN")
