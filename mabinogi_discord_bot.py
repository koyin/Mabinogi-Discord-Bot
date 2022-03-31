import os
import discord
import random
import re
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
print(TOKEN)

client = discord.Client()

@client.event
async def on_ready():
    print(
        f'{client.user} is connected'
    )
    for guild in client.guilds:
        print(
            f'{guild.name}(id: {guild.id})\n'
        )
        members = '\n - '.join([member.name for member in guild.members])
        print(f'Guild Members:\n - {members}')
        print(f'\n\n')

    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="a movie"))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if "占卜" not in message.channel.name and "豬肉榮" not in message.channel.name and "鯊" not in message.channel.name:
        return

    print(message)

    if (message.content.startswith("!lucky ")):

        split_message = message.content.split(" ", 1)

        lucky_result = [
            "大鯊",
            "鯊",
            "小鯊",
            "小魚",
            "魚",
            "大魚"
        ]

        response = random.choice(lucky_result)
        print(response)
        await message.channel.send((
            f"<@{message.author.id}> {split_message[1]}"
            "\n"
            f"抽到了「{response}」！"
        ))

    elif (message.content.startswith("!yesno ")):

        split_message = message.content.split(" ", 1)

        lucky_result = [
            "⭕",
            "❌"
        ]

        response = random.choice(lucky_result)
        print(response)
        await message.channel.send((
            f"<@{message.author.id}> {split_message[1]}"
            "\n"
            f"「{response}」！"
        ))
    
    elif (message.content.startswith("!dice ")):

        split_message = message.content.split(" ", 2)

        pattern = re.compile("^\d+d\d+$")
        pattern_d = re.compile("\d+")
        print(split_message[1])
        print(pattern_d.findall(split_message[1]))

        if (len(split_message) < 3 or not pattern.match(split_message[1])):
            await message.channel.send((
                f"<@{message.author.id}>"
                f"指令錯誤鯊！"
            ))
            return

        d = pattern_d.findall(split_message[1])

        add = []
        sum = 0
        for i in range(int(d[0])):
            rand_int = random.randrange(1, int(d[1]) + 1, 1)
            add.append(str(rand_int))
            sum = sum + rand_int

        await message.channel.send((
            f"<@{message.author.id}> {split_message[2]}"
            "\n"
        ) + (f"結果是 {' + '.join(add)} = {sum}" if len(add) > 1 else f"結果是 {sum}"))
    
    elif (message.content.startswith("!摸頭")):

        image_url = [
            "https://upload.cc/i1/2022/03/31/bFlJfv.jpg"
        ]

        embed = discord.Embed(color=0x000000)
        embed.set_image(url=random.choice(image_url))

        await message.channel.send((
            f"<@{message.author.id}>"
        ), embed=embed)
    
    elif (message.content.startswith("!裝死")):

        image_url = [
            "https://upload.cc/i1/2022/03/31/SjGqv1.jpeg"
        ]

        embed = discord.Embed(color=0x000000)
        embed.set_image(url=random.choice(image_url))

        await message.channel.send((
            f"<@{message.author.id}>"
        ), embed=embed)
    
    elif (message.content.startswith("!help")):

        await message.channel.send((
            f"<@{message.author.id}> 指令說明鯊鯊！"
            "\n"
            "====================================="
            "\n"
            "`!摸頭`"
            "\n"
            "`!裝死`"
            "\n"
            "====================================="
            "\n"
            "`!lucky 一些事情` 碰一下運氣"
            "\n"
            "`!yesno 一些事情` 幫你做決定"
            "\n"
            "`!dice NdM 一些事情` 來擲個骰子 (例子：`!dice 1d13` 投擲一顆13面骰子、`!dice 2d7` 投擲兩顆骰子，每顆骰子7面)"
            "\n"
            "====================================="
        ))

    else:

        random_response = [
            '我是鯊鯊！',
            '鯊！鯊鯊！',
            '我要宵夜！',
            '蛤？'
        ]

        response = random.choice(random_response)
        await message.channel.send((
            f"<@{message.author.id}> "
            f"{response}"
        ))

client.run(TOKEN)