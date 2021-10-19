import discord
from discord.ext import commands
from discord.ext.commands.core import command
import asyncio
import os
import random
import re
import asyncpraw
from pretty_help import PrettyHelp
import datetime

TOKEN = str(os.environ["TOKEN"])

# bot configs
intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix="amanda ", intents=intents)

# pretty help configs
color = 0x179C34
bot.help_command = PrettyHelp(color=color)

# REGULAR EXPRESSIONS
marcos_regex = re.compile(r"\bmarcos\b")

# reddit config
reddit = asyncpraw.Reddit(
    client_id="oZjbB_dKb_RUhw",
    client_secret=os.environ["secret"],
    username="_marcos123",
    password=os.environ["password"],
    user_agent="marcos",
)

alternas = [
    "https://i.pinimg.com/564x/d2/ed/a1/d2eda1b3036aa94ded3381b3495b79d3.jpg",
    "https://i.pinimg.com/564x/cb/a8/86/cba8867e6df8f06582d5f8b41527e145.jpg",
    "https://i.pinimg.com/564x/92/9e/1e/929e1eeba07ce47f27f4448635ec9e29.jpg",
    "https://i.pinimg.com/564x/a1/0c/87/a10c877037b4296fa6c783dd983c62db.jpg",
    "https://i.pinimg.com/564x/82/01/09/820109f708a5a5657a5b4a088a71315c.jpg",
    "https://cdn.discordapp.com/attachments/759882556744663040/824573836468158484/booba.png",
    "https://i.pinimg.com/564x/44/63/0b/44630b852978a3102c543acf4b3d79cd.jpg",
    "https://i.pinimg.com/564x/c6/87/43/c68743aadb118de38ac690e8bdd3d2a0.jpg",
    "https://i.pinimg.com/564x/d9/e2/b0/d9e2b09a7c22658d77ce454dc93ea6a6.jpg",
    "https://i.pinimg.com/564x/61/e9/b9/61e9b9889cfd16f894604b672c51f432.jpg",
    "https://i.pinimg.com/564x/f4/6b/51/f46b517b5c31090fd1ac6c025fea3e63.jpg",
    "https://i.pinimg.com/564x/fc/59/ab/fc59ab3cc05dc204980a16d6e0b56750.jpg",
    "https://i.pinimg.com/564x/3e/9b/68/3e9b681c43b59c116fd8b4e20f114c5c.jpg",
    "https://i.pinimg.com/564x/5b/6f/9a/5b6f9ac06ca76ecbd507a9552cbe5cff.jpg",
    "https://i.pinimg.com/564x/14/f3/1d/14f31de2e7e96e8eb514c898d74241fe.jpg",
    "https://i.pinimg.com/564x/98/8a/b7/988ab7dcde08b86f5a26925beba4f9db.jpg",
    "https://i.pinimg.com/564x/71/74/f6/7174f6dc7f9787eb046fdcffa4cbe46b.jpg",
    "https://i.pinimg.com/564x/99/ee/fd/99eefd6adecea6b9575a530fdd57cf86.jpg",
    "https://i.pinimg.com/originals/63/cc/1c/63cc1c23ab98d4f726efb75321c75b67.jpg",
    "https://cdn.discordapp.com/attachments/813841826666250291/860170891266490418/63cc1c23ab98d4f726efb75321c75b67.jpg",
    "https://cdn.discordapp.com/attachments/813841826666250291/860171325950787614/unknown.png",
    "https://cdn.discordapp.com/attachments/813841826666250291/860171384323833896/unknown.png",
    "https://cdn.discordapp.com/attachments/813841826666250291/860171540115750932/unknown.png",
    "https://cdn.discordapp.com/attachments/813841826666250291/860171600674291752/unknown.png",
    "https://cdn.discordapp.com/attachments/813841826666250291/860171660232753182/unknown.png",
    "https://cdn.discordapp.com/attachments/813841826666250291/860171711533809694/unknown.png",
    "https://cdn.discordapp.com/attachments/813841826666250291/860171763736248340/unknown.png",
]

sapos = [
    "https://cdn.wallpapersafari.com/41/15/xZomb3.jpg",
    "http://2.bp.blogspot.com/-VirjBRtnyIU/TyfUR2dSi_I/AAAAAAAAB8E/8jDDSBmWs1E/s1600/Cute+Frog4.jpg",
    "https://shopzoki.com/wp-content/uploads/2019/09/IMG_5617.jpg",
    "https://shopzoki.com/wp-content/uploads/2019/09/DSC_1370.jpg",
    "https://i.pinimg.com/236x/f1/1f/c9/f11fc918f1aafa2ec38dccb0e5e3b338.jpg",
    "https://i.pinimg.com/474x/df/33/5e/df335ea92fe0a565859a1dbe0aeed2e0.jpg",
    "https://i.pinimg.com/474x/8e/d9/64/8ed9641c7ce86176250727efd8f80d75.jpg",
    "https://cdn.discordapp.com/attachments/813841826666250291/823972345882345492/Waldo.png",
    "https://i.pinimg.com/564x/61/e3/67/61e3671e1a30d3d6369d9923f884dd2f.jpg",
    "https://i.pinimg.com/564x/fb/c1/4d/fbc14d43bf507209c379fd32be9c5e16.jpg",
    "https://i.pinimg.com/564x/c1/9a/27/c19a27513bba99b27755395b329414e0.jpg",
    "https://i.pinimg.com/564x/85/d4/b8/85d4b80df2a79db4d429f51ca5792431.jpg",
    "https://i.pinimg.com/474x/be/a6/5f/bea65f563cd5993ebf6b52bd4ae9f3d2.jpg",
    "https://i.pinimg.com/564x/39/77/de/3977debb17a4aac4c78e7aff4f1c668a.jpg",
    "https://i.pinimg.com/474x/7b/e5/ce/7be5ceb27a15b131cc8c276162b4ae17.jpg",
    "https://tenor.com/view/h%C3%A2m-frog-toad-frog-l%E1%BA%AFc-wiggle-gif-14557565",
    "https://tenor.com/view/frog-spinning-vinyl-animal-carnivorous-gif-17270183",
    "https://tenor.com/view/frog-gail-fail-let-me-have-it-gif-12024489",
]

sexos = [
    "https://tenor.com/view/horny-jail-bonk-dog-hit-head-stop-being-horny-gif-17298755",
    "https://media.discordapp.net/attachments/409313701888393218/715292714622517328/meme.gif",
    "https://media.discordapp.net/attachments/635466696609759232/762026840457871390/caption.gif",
    "https://cdn.discordapp.com/attachments/813841826666250291/838803483745845298/unknown.png",
]

geral = bot.get_channel(int(os.environ["geral"]))
guild = bot.get_guild(int(os.environ["server"]))

# ya isto não correu bem :/
@bot.event
async def acabou():
    while True:
        await bot.wait_until_ready()
        if (
            datetime.datetime.now().strftime("%Y") == 2021
            and datetime.datetime.now().strftime("%m") == 7
            and datetime.datetime.now().strftime("%d") == 9
            and datetime.datetime.now().strftime("%H") == 5
            and datetime.datetime.now().strftime("%M") == 30
        ):
            await geral.send("https://cdn.discordapp.com/attachments/844974741130313779/860170459441004564/caption.gif")

        await asyncio.sleep(59)


bot.loop.create_task(acabou())

# changes discord presence
@bot.event
async def on_ready():
    global guild
    await bot.change_presence(activity=discord.Game("Shawty"))
    print("Connected to bot: {}".format(bot.user.name))
    print("Bot ID: {}".format(bot.user.id))
    print(guild)


# send random frog image
@bot.command(help="🐸")
async def sapinho(ctx):
    sapo = random.choice(sapos)
    await ctx.reply(sapo)


# send shawty
@bot.command(help="na na na na everyday")
async def shawty(ctx):
    await ctx.reply("https://www.youtube.com/watch?v=c6gV5J5C1Cg")


# send sexo gif
@bot.command(help="bonk, go to horny jail")
async def sexo(ctx):
    sexo = random.choice(sexos)
    await ctx.reply(sexo)


# replies with class link
@bot.command(help="links da primeira semana")
async def aulas(ctx):
    embed = discord.Embed()
    embed.add_field(
        name=f"**Segunda**",
        value=f"> 14:00 - 15:30 : [🔭 FII](https://us02web.zoom.us/j/5187730519?pwd=VUpVUGFjVVZXeE1PakFKSHBIa2IwZz09)\n> 15:30 - 16:30 : [💻 AED](https://videoconf-colibri.zoom.us/j/86106401089?pwd=TElEQnJsSWxobEdsK2VqZ0JQWnhXUT09)\n> 16:30 - 17:30 : 💾 BD [par](https://videoconf-colibri.zoom.us/j/83134112659) [ímpar](https://videoconf-colibri.zoom.us/j/87348858347)",
        inline=False,
    )
    embed.add_field(
        name=f"**Quinta**",
        value=f"> 14:00 - 15:00 : [💻 AED](https://videoconf-colibri.zoom.us/j/86106401089?pwd=TElEQnJsSWxobEdsK2VqZ0JQWnhXUT09)\n> 15:00 - 16:00 : 💾 BD [par](https://videoconf-colibri.zoom.us/j/83482649273) [ímpar](https://videoconf-colibri.zoom.us/j/81363366128)\n> 16:00 - 18:00 : 🤔 [TC](https://teams.microsoft.com/l/team/19%3aD1SnJs22lq4oSAVpoLsnpEtmPx2raH6yYh02FExCSVY1%40thread.tacv2/conversations?groupId=04da93b5-66cc-42ca-9123-69099c8e2fd8&tenantId=b7821bc8-67cc-447b-b579-82f7854174fc) \n > 18:00 - 20:00 : 🧑‍🔬 [LDTS](https://videoconf-colibri.zoom.us/j/83509609332?pwd=dzBKczF2akIySVlZcHZValJIZERLZz09)",
        inline=False,
    )
    embed.color = 0x00A0A0
    await ctx.reply(embed=embed)


# embed_aulas1 = discord.Embed()
# embed_aulas1.title = "Aulas L.EIC"
# embed_aulas1.description = '''\nBDAD IMPAR \n([seg](https://videoconf-colibri.zoom.us/j/87348858347) 15:00-16:00 | [qui](https://videoconf-colibri.zoom.us/j/81363366128) 19:00-20:00)
# BDAD PAR \n([seg](https://videoconf-colibri.zoom.us/j/83134112659) 16:30-17:30 | [qui](https://videoconf-colibri.zoom.us/j/83482649273) 15:00-16:00)
# [AEDA](https://videoconf-colibri.zoom.us/j/86106401089?pwd=TElEQnJsSWxobEdsK2VqZ0JQWnhXUT09 )
# FISI2 \n([14:00-15:30](https://us02web.zoom.us/j/5187730519?pwd=VUpVUGFjVVZXeE1PakFKSHBIa2IwZz09) | [16:00-17:30](https://videoconf-colibri.zoom.us/j/87471710064?pwd=WGQ5N2xDdFl5ckVLOHVXUThka1VXZz09))
# [LDTS](https://videoconf-colibri.zoom.us/j/83509609332?pwd=dzBKczF2akIySVlZcHZValJIZERLZz09)
# [TCOM](https://teams.microsoft.com/l/team/19%3aD1SnJs22lq4oSAVpoLsnpEtmPx2raH6yYh02FExCSVY1%40thread.tacv2/conversations?groupId=04da93b5-66cc-42ca-9123-69099c8e2fd8&tenantId=b7821bc8-67cc-447b-b579-82f7854174fc)'''

# if (guild.get_member(809036224957513748).status == discord.Status.offline):  #replacing botinha's shifts
#    await ctx.reply(embed = embed_aulas1)

# await ctx.reply(embed = embed_aulas1)

# shipping an alterna right to your door!
@bot.command(help="shipping an altena right away!!")
async def alterna(ctx):
    tracking = random.randint(29719301, 91739173)

    emb = discord.Embed()
    emb.title = "Thank you for your purchase!"
    emb.description = """An alterna was shipped to you and should arrive soon!
                         You can use {} to track your package!""".format(
        tracking
    )

    channel = await ctx.message.author.create_dm()
    dm = discord.Embed()
    dm.title = "Your alterna has arrived! 🤤"
    dm.set_image(url=random.choice(alternas))

    await ctx.reply(embed=emb)
    await channel.send(embed=dm)


# gets reddit frog
@bot.command(help="sends top forggo on reddit !")
async def sapo(ctx):
    subreddit = await reddit.subreddit("frog")
    all_subs = []

    top = subreddit.top("month", limit=100)

    async for submission in top:
        if ("i.redd.it" in submission.url) and (len(submission.title) < 256):
            all_subs.append(submission)

    random_submission = random.choice(all_subs)

    name = random_submission.title
    url = random_submission.url

    emb = discord.Embed(title=name, timestamp=datetime.datetime.utcnow())
    emb.set_image(url=url)
    emb.color = 0xC4FFED

    await ctx.reply(embed=emb)


# gets reddit danger noodle
@bot.command(help="sends top danger noodles on reddit !")
async def snek(ctx):
    subreddit = await reddit.subreddit("Sneks")
    all_subs = []

    top = subreddit.top("month", limit=70)

    async for submission in top:
        if ("i.redd.it" in submission.url) and (len(submission.title) < 256):
            all_subs.append(submission)

    random_submission = random.choice(all_subs)

    name = random_submission.title
    url = random_submission.url

    emb = discord.Embed(title=name, timestamp=datetime.datetime.utcnow())
    emb.set_image(url=url)
    emb.color = 0xC4FFED

    await ctx.reply(embed=emb)


# gets reddit star wars meme
@bot.command(help="sends poggers prequel meme")
async def palpatine(ctx):
    subreddit = await reddit.subreddit("PrequelMemes")
    all_subs = []

    top = subreddit.top("month", limit=70)

    async for submission in top:
        if ("i.redd.it" in submission.url) and (len(submission.title) < 256):
            all_subs.append(submission)

    random_submission = random.choice(all_subs)

    name = random_submission.title
    url = random_submission.url

    emb = discord.Embed(title=name, timestamp=datetime.datetime.utcnow())
    emb.set_image(url=url)
    emb.color = 0xC4FFED

    await ctx.reply(embed=emb)


# gets super awesome kanye meme
@bot.command(help="kayne")
async def kanye(ctx):
    subreddit = await reddit.subreddit("WestSubEver")
    all_subs = []

    top = subreddit.top("month", limit=50)

    async for submission in top:
        if ("i.redd.it" in submission.url) and (len(submission.title) < 256):
            all_subs.append(submission)

    random_submission = random.choice(all_subs)

    name = random_submission.title
    url = random_submission.url

    emb = discord.Embed(title=name, timestamp=datetime.datetime.utcnow())
    emb.set_image(url=url)
    emb.color = 0xE6C655

    await ctx.reply(embed=emb)


# replies with nerdices
@bot.command(help="sends relatable nerd shid")
async def src(ctx):
    subreddit = await reddit.subreddit("ProgrammerHumor")
    all_subs = []

    top = subreddit.top("month", limit=70)

    async for submission in top:
        if ("i.redd.it" in submission.url) and (len(submission.title) < 256):
            all_subs.append(submission)

    random_submission = random.choice(all_subs)

    name = random_submission.title
    url = random_submission.url

    emb = discord.Embed(title=name, timestamp=datetime.datetime.utcnow())
    emb.set_image(url=url)
    emb.color = 0xC4FFED

    await ctx.reply(embed=emb)


# replies with nerdices
@bot.command(help="communism")
async def comuna(ctx):
    subreddit = await reddit.subreddit("CommunismMemes")
    all_subs = []

    top = subreddit.top("month", limit=50)

    async for submission in top:
        if ("i.redd.it" in submission.url) and (len(submission.title) < 256):
            all_subs.append(submission)

    random_submission = random.choice(all_subs)

    name = random_submission.title
    url = random_submission.url

    emb = discord.Embed(title=name, timestamp=datetime.datetime.utcnow())
    emb.set_image(url=url)
    emb.color = 0xFF0015
    await ctx.reply(embed=emb)


# replies with epicc anime meme
@bot.command(help="epicc anime")
async def weeb(ctx):
    subreddit = await reddit.subreddit("animememes")
    all_subs = []

    top = subreddit.top("month", limit=70)

    async for submission in top:
        if ("i.redd.it" in submission.url) and (len(submission.title) < 256):
            all_subs.append(submission)

    random_submission = random.choice(all_subs)

    name = random_submission.title
    url = random_submission.url

    emb = discord.Embed(title=name, timestamp=datetime.datetime.utcnow())
    emb.set_image(url=url)
    emb.color = 0xBDFFFD
    await ctx.reply(embed=emb)


# replies to marcos
@bot.event
async def on_message(msg: discord.Message):
    await bot.process_commands(msg)
    m: str = msg.content.lower()

    if marcos_regex.search(m) is not None:
        emb = discord.Embed(
            url="https://cdn.discordapp.com/attachments/796509327997403156/823914978397388831/badady.mp4"
        )

        print(msg.author)
        if "footvaalvica" in str(msg.author):
            await msg.reply(emb)
        else:
            await msg.reply("https://cdn.discordapp.com/attachments/796509327997403156/823914978397388831/badady.mp4")

    if msg.content == "69":
        await msg.reply("nice")

    if msg.content == "420":
        await msg.reply("blaze it")

    if msg.author == msg.guild.get_member(335110897297129475):
        if ("matar" in msg.content) and ("sapos" in m) or ("odeio" in m) and ("sapos" in m):

            channel = await msg.author.create_dm()
            dm = discord.Embed()
            dm.title = "Volta a dizer isso que tu vês >:C"
            dm.set_image(url=random.choice(sapos))

            await channel.send(embed=dm)
            await msg.reply("https://tenor.com/view/kermit-evil-slapping-smack-kermit-the-frog-gif-17875825")


bot.run(TOKEN)
