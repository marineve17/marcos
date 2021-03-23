import discord
from discord.ext import commands
from discord.ext.commands.core import command
import asyncio
import os
import random
import re
import asyncpraw

TOKEN = str(os.environ['TOKEN'])

intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix="amanda ", intents = intents)

# REGULAR EXPRESSIONS
marcos_regex = re.compile(r"\bmarcos\b")

#reddit settings
reddit = asyncpraw.Reddit(client_id = "oZjbB_dKb_RUhw",
                     client_secret = os.environ['secret'],
                     username = "_marcos123",
                     password = os.environ['password'],
                     user_agent = "marcos")


@bot.command()
async def sapo(ctx):
    subreddit = await reddit.subreddit("frog")
    all_subs = []

    top = subreddit.top("month", limit = 20)

    async for submission in top:
        all_subs.append(submission)

    random_submission = random.choice(all_subs)

    name = random_submission.title
    url = random_submission.url

    emb = discord.Embed(title = url)
    emb.set_image(url = url)

    await ctx.send(embed = emb)


sapos = ["https://cdn.wallpapersafari.com/41/15/xZomb3.jpg", "http://2.bp.blogspot.com/-VirjBRtnyIU/TyfUR2dSi_I/AAAAAAAAB8E/8jDDSBmWs1E/s1600/Cute+Frog4.jpg",
         "https://shopzoki.com/wp-content/uploads/2019/09/IMG_5617.jpg", "https://shopzoki.com/wp-content/uploads/2019/09/DSC_1370.jpg", 
         "https://i.pinimg.com/236x/f1/1f/c9/f11fc918f1aafa2ec38dccb0e5e3b338.jpg", "https://i.pinimg.com/474x/df/33/5e/df335ea92fe0a565859a1dbe0aeed2e0.jpg",
         "https://i.pinimg.com/474x/8e/d9/64/8ed9641c7ce86176250727efd8f80d75.jpg", "https://cdn.discordapp.com/attachments/813841826666250291/823972345882345492/Waldo.png",
         "https://i.pinimg.com/564x/61/e3/67/61e3671e1a30d3d6369d9923f884dd2f.jpg", "https://i.pinimg.com/564x/fb/c1/4d/fbc14d43bf507209c379fd32be9c5e16.jpg",
         "https://i.pinimg.com/564x/c1/9a/27/c19a27513bba99b27755395b329414e0.jpg", "https://i.pinimg.com/564x/85/d4/b8/85d4b80df2a79db4d429f51ca5792431.jpg",
         "https://i.pinimg.com/474x/be/a6/5f/bea65f563cd5993ebf6b52bd4ae9f3d2.jpg", "https://i.pinimg.com/564x/39/77/de/3977debb17a4aac4c78e7aff4f1c668a.jpg",
         "https://i.pinimg.com/474x/7b/e5/ce/7be5ceb27a15b131cc8c276162b4ae17.jpg", "https://tenor.com/view/h%C3%A2m-frog-toad-frog-l%E1%BA%AFc-wiggle-gif-14557565",
         "https://tenor.com/view/frog-spinning-vinyl-animal-carnivorous-gif-17270183", "https://tenor.com/view/frog-gail-fail-let-me-have-it-gif-12024489"]

#changes discord presence
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game('Shawty'))
    print('Connected to bot: {}'.format(bot.user.name))
    print('Bot ID: {}'.format(bot.user.id))


@bot.command()
async def frog(ctx):
    sapo = random.choice(sapos)
    await ctx.reply(sapo)

@bot.command()
async def shawty(ctx):
    await ctx.reply("https://www.youtube.com/watch?v=c6gV5J5C1Cg")

#replies to marcos
@bot.event
async def on_message(msg: discord.Message):
    await bot.process_commands(msg) 
    m: str = msg.content.lower()

    if marcos_regex.search(m) is not None:
        await msg.reply("https://cdn.discordapp.com/attachments/796509327997403156/823914978397388831/badady.mp4")




bot.run(TOKEN)