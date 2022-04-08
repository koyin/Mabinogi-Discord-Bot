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

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if "占卜" not in message.channel.name and "豬肉榮" not in message.channel.name:
        return

    print(message)

    if (message.content.startswith("!lucky ")):

        split_message = message.content.split(" ", 1)

        lucky_result = [
            "大兇",
            "兇",
            "小兇",
            "小吉",
            "吉",
            "大吉"
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
                f"指令錯誤汪！"
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
    
    elif (message.content.startswith("!range ")):

        split_message = message.content.split(" ", 2)

        pattern = re.compile("^\d+t\d+$")
        pattern_d = re.compile("\d+")
        print(split_message[1])
        print(pattern_d.findall(split_message[1]))

        if (len(split_message) < 3 or not pattern.match(split_message[1])):
            await message.channel.send((
                f"<@{message.author.id}>"
                f"指令錯誤汪！"
            ))
            return

        d = pattern_d.findall(split_message[1])

        rand_int = random.randint(d[0], d[1])

        await message.channel.send((
            f"<@{message.author.id}> {split_message[2]}"
            "\n"
        ) + (f"結果是 {rand_int}"))
    
    elif (message.content.startswith("!摸頭")):

        image_url = [
            "https://upload.cc/i1/2022/03/22/dSwHvO.jpeg",
            "https://upload.cc/i1/2022/03/23/y0DX4f.jpg"
        ]

        embed = discord.Embed(color=0x000000)
        embed.set_image(url=random.choice(image_url))

        await message.channel.send((
            f"<@{message.author.id}>"
        ), embed=embed)
    
    elif (message.content.startswith("!裝死")):

        image_url = [
            "https://upload.cc/i1/2022/03/23/Z3SwRI.jpg"
        ]

        embed = discord.Embed(color=0x000000)
        embed.set_image(url=random.choice(image_url))

        await message.channel.send((
            f"<@{message.author.id}>"
        ), embed=embed)
    
    elif (message.content.startswith("!help")):

        await message.channel.send((
            f"<@{message.author.id}> 指令說明汪汪！"
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
            "`!range NtM 一些事情` 抽範圍數值 (例子：`!range 3d9` 抽選一個3至9的數字)"
            "\n"
            "====================================="
        ))

    else:

        random_response = [
            '汪！',
            '汪！汪汪！',
            '我要肉肉！',
            '蛤？'
        ]

        response = random.choice(random_response)
        await message.channel.send((
            f"<@{message.author.id}> "
            f"{response}"
        ))

client.run(TOKEN)