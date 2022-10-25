from typing import List
import string
import discord

from main import Parser

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

OUT_FILE = "log.txt"

DECODE_CMD = '.d '


parser = Parser()
parser.load_dict("log.txt")


def cleanup(s: str) -> str:
    return s.translate(str.maketrans('', '', string.punctuation))


def add_to_dict(s: str) -> List[str]:
    clean_content = cleanup(s)

    words = clean_content.split()

    with open(OUT_FILE, "a") as f:
        for w in words:
            f.write(w + '\n')

    return words


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if message.content.startswith(DECODE_CMD):
        resolved = parser.resolve_string(
            message.content.replace(DECODE_CMD, ""))

        print(resolved)

        await message.channel.send(resolved)
        return

    new_words = add_to_dict(message.content)
    parser.extend_dict(new_words)


client.run(
    'MTAzNDU4MjAzNzQwNDg0ODE3OA.GvtGbF.Yjba8MqYy4dJ5JjfMVgVyGcJIMsw8-tELbEEfQ')
