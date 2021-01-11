from dotenv import load_dotenv
import asyncio
import os
import discord
from discord.ext import commands

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

# Create bot client.
intents = discord.Intents.default()
client = commands.Bot(command_prefix="", intents=intents)


@client.event
async def on_ready():
    print("Started! Logged in as", client.user.name)
    client.add_cog(Greetings(client))


@client.command()
async def pride(ctx):

    quetes = "Love is patient", "Love is kind", "Love does not boast", "Love isn't prous", "Love protects", "Love doesn't envy", "Love isn't self-sekking", "Love keeps no records of wrongs", "Love always trusts", "Love always hopes", "Love never fails"
    colors = 0xff0000, 0xffa500, 0xffff00, 0x008000, 0x0000ff, 0x4b0082, 0xee82ee

    embed = discord.Embed(title=":rainbow_flag: PRIDE",
                          description=quetes[0], color=colors[0])
    embed.set_author(name="hryszkoDev")
    msg = await ctx.send(embed=embed)

    await msg.add_reaction("🇱")
    await msg.add_reaction("🇬")
    await msg.add_reaction("🇧")
    await msg.add_reaction("🇹")
    await msg.add_reaction("🇶")
    await msg.add_reaction("➕")

    for i in range(200):
        await asyncio.sleep(1.5)
        embed = discord.Embed(title=":rainbow_flag: PRIDE", description=quetes[i % len(
            quetes)], color=colors[i % len(colors)])
        await msg.edit(embed=embed)


@client.command()
async def repeat(ctx, arg):
    await ctx.send(arg)


@client.command()
async def repeat2(ctx, arg1, arg2):
    await ctx.send('You passed {} and {}'.format(arg1, arg2))


@client.command()
async def repeatge2(ctx, *args):
    await ctx.send('{} arguments: {}'.format(len(args), ', '.join(args)))


@client.command()
async def hi(ctx):
    await ctx.send('Hi {}\nHow are you?'.format(ctx.author))


@client.command()
async def calc(ctx, a: int, oper, b: int):
    if oper == "+":
        await ctx.send('{} {} {} = **{}**'.format(a, oper, b, a + b))
    elif oper == "-":
        await ctx.send('{} {} {} = **{}**'.format(a, oper, b, a - b))
    elif oper == "*":
        await ctx.send('{} {} {} = **{}**'.format(a, oper, b, a * b))
    elif oper == "/" or oper == ":":
        if b == 0:
            await ctx.send('**MATH ERROR**: you cannot devide by zero. That\'s math rule!')
        else:
            await ctx.send('{} {} {} = **{}**'.format(a, oper, b, a / b))
    elif oper == "%":
        await ctx.send('{} {} {} = **{}**'.format(a, oper, b, a % b))
    else:
        await ctx.send('Unrecognised operator try: **+**, **-**, **/**, *****, **%**')


class Greetings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command()
    async def hello(self, ctx, *, member: discord.Member = None):
        member = member or ctx.author
        if self._last_member is None or self._last_member.id != member.id:
            await ctx.send('Hello {0.name}~'.format(member))
        else:
            await ctx.send('Hello {0.name}... This feels familiar.'.format(member))
        self._last_member = member


@client.command()
async def test(ctx):
    msg = await ctx.send("xD")
    await msg.edit(content="xDD")
    await msg.edit(content="xDDD")
    await msg.edit(content="xDDDD")
    await msg.edit(content="xDDDDD")
    await msg.edit(content="xDDDDDD")
    await msg.edit(content="xDDDDDDD")
    await msg.edit(content="xDDDDDDDD")
    await msg.edit(content="xDDDDDDDDD")
    await msg.edit(content="xDDDDDDDDDD")
    await msg.edit(content="xDDDDDDDDDDD")
    await msg.edit(content="xDDDDDDDDDDDD")
    await msg.edit(content="xDDDDDDDDDDDDD")


@client.command()
async def d(ctx):
    # I do not actually recommend doing this.
    async for user in reaction.users():
        await channel.send('{0} has reacted with {1.emoji}!'.format(user, reaction))

client.run(DISCORD_TOKEN)
