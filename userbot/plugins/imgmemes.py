#  Copyright (C) 2020  Criminal786
# credits to @copyless786 (@TeamLionX)
import asyncio
import os
import re

from userbot import lionxub

from ..funcs.managers import edit_delete, edit_or_reply
from ..helpers.utils import reply_id
from . import (
    changemymind,
    deEmojify,
    fakegs,
    kannagen,
    moditweet,
    reply_id,
    trumptweet,
    tweets,
)

plugin_category = "fun"


@lionxub.lionx_cmd(
    pattern="fakegs(?:\s|$)([\s\S]*)",
    command=("fakegs", plugin_category),
    info={
        "header": "Fake google search meme",
        "usage": "{tr}fakegs search query ; what you mean text",
        "examples": "{tr}fakegs LionX ; One of the Popular userbot",
    },
)
async def nekobot(lionx):
    "Fake google search meme"
    text = lionx.pattern_match.group(1)
    reply_to_id = await reply_id(lionx)
    if not text:
        if lionx.is_reply and not reply_to_id.media:
            text = reply_to_id.message
        else:
            return await edit_delete(lionx, "`What should i search in google.`", 5)
    lion = await edit_or_reply(lionx, "`Connecting to https://www.google.com/ ...`")
    text = deEmojify(text)
    if ";" in text:
        search, result = text.split(";")
    else:
        await edit_delete(
            lionx,
            "__How should i create meme follow the syntax as show__ `.fakegs top text ; bottom text`",
            5,
        )
        return
    lionxfile = await fakegs(search, result)
    await asyncio.sleep(2)
    await lionx.client.send_file(lionx.chat_id, lionxfile, reply_to=reply_to_id)
    await lion.delete()
    if os.path.exists(lionxfile):
        os.remove(lionxfile)


@lionxub.lionx_cmd(
    pattern="trump(?:\s|$)([\s\S]*)",
    command=("trump", plugin_category),
    info={
        "header": "trump tweet sticker with given custom text",
        "usage": "{tr}trump <text>",
        "examples": "{tr}trump LionX is One of the Popular userbot",
    },
)
async def nekobot(lionx):
    "trump tweet sticker with given custom text_"
    text = lionx.pattern_match.group(1)
    text = re.sub("&", "", text)
    reply_to_id = await reply_id(lionx)

    reply = await lionx.get_reply_message()
    if not text:
        if lionx.is_reply and not reply.media:
            text = reply.message
        else:
            return await edit_delete(lionx, "**Trump : **`What should I tweet`", 5)
    lion = await edit_or_reply(lionx, "`Requesting trump to tweet...`")
    text = deEmojify(text)
    await asyncio.sleep(2)
    lionxfile = await trumptweet(text)
    await lionx.client.send_file(lionx.chat_id, lionxfile, reply_to=reply_to_id)
    await lion.delete()
    if os.path.exists(lionxfile):
        os.remove(lionxfile)


@lionxub.lionx_cmd(
    pattern="modi(?:\s|$)([\s\S]*)",
    command=("modi", plugin_category),
    info={
        "header": "modi tweet sticker with given custom text",
        "usage": "{tr}modi <text>",
        "examples": "{tr}modi LionX is One of the Popular userbot",
    },
)
async def nekobot(lionx):
    "modi tweet sticker with given custom text"
    text = lionx.pattern_match.group(1)
    text = re.sub("&", "", text)
    reply_to_id = await reply_id(lionx)

    reply = await lionx.get_reply_message()
    if not text:
        if lionx.is_reply and not reply.media:
            text = reply.message
        else:
            return await edit_delete(lionx, "**Modi : **`What should I tweet`", 5)
    lion = await edit_or_reply(lionx, "Requesting modi to tweet...")
    text = deEmojify(text)
    await asyncio.sleep(2)
    lionxfile = await moditweet(text)
    await lionx.client.send_file(lionx.chat_id, lionxfile, reply_to=reply_to_id)
    await lion.delete()
    if os.path.exists(lionxfile):
        os.remove(lionxfile)


@lionxub.lionx_cmd(
    pattern="cmm(?:\s|$)([\s\S]*)",
    command=("cmm", plugin_category),
    info={
        "header": "Change my mind banner with given custom text",
        "usage": "{tr}cmm <text>",
        "examples": "{tr}cmm LionX is One of the Popular userbot",
    },
)
async def nekobot(lionx):
    text = lionx.pattern_match.group(1)
    text = re.sub("&", "", text)
    reply_to_id = await reply_id(lionx)

    reply = await lionx.get_reply_message()
    if not text:
        if lionx.is_reply and not reply.media:
            text = reply.message
        else:
            return await edit_delete(lionx, "`Give text to write on banner, man`", 5)
    lion = await edit_or_reply(lionx, "`Your banner is under creation wait a sec...`")
    text = deEmojify(text)
    await asyncio.sleep(2)
    lionxfile = await changemymind(text)
    await lionx.client.send_file(lionx.chat_id, lionxfile, reply_to=reply_to_id)
    await lion.delete()
    if os.path.exists(lionxfile):
        os.remove(lionxfile)


@lionxub.lionx_cmd(
    pattern="kanna(?:\s|$)([\s\S]*)",
    command=("kanna", plugin_category),
    info={
        "header": "kanna chan sticker with given custom text",
        "usage": "{tr}kanna text",
        "examples": "{tr}kanna LionX is One of the Popular userbot",
    },
)
async def nekobot(lionx):
    "kanna chan sticker with given custom text"
    text = lionx.pattern_match.group(1)
    text = re.sub("&", "", text)
    reply_to_id = await reply_id(lionx)

    reply = await lionx.get_reply_message()
    if not text:
        if lionx.is_reply and not reply.media:
            text = reply.message
        else:
            return await edit_delete(lionx, "**Kanna : **`What should i show you`", 5)
    lion = await edit_or_reply(lionx, "`Kanna is writing your text...`")
    text = deEmojify(text)
    await asyncio.sleep(2)
    lionxfile = await kannagen(text)
    await lionx.client.send_file(lionx.chat_id, lionxfile, reply_to=reply_to_id)
    await lion.delete()
    if os.path.exists(lionxfile):
        os.remove(lionxfile)


@lionxub.lionx_cmd(
    pattern="tweet(?:\s|$)([\s\S]*)",
    command=("tweet", plugin_category),
    info={
        "header": "The desired person tweet sticker with given custom text",
        "usage": "{tr}tweet <username> ; <text>",
        "examples": "{tr}tweet iamsrk ; LionX is One of the Popular userbot",
    },
)
async def nekobot(lionx):
    "The desired person tweet sticker with given custom text"
    text = lionx.pattern_match.group(1)
    text = re.sub("&", "", text)
    reply_to_id = await reply_id(lionx)

    reply = await lionx.get_reply_message()
    if not text:
        if lionx.is_reply and not reply.media:
            text = reply.message
        else:
            return await edit_delete(
                lionx,
                "what should I tweet? Give some text and format must be like `.tweet username ; your text` ",
                5,
            )
    if ";" in text:
        username, text = text.split(";")
    else:
        await edit_delete(
            lionx,
            "__what should I tweet? Give some text and format must be like__ `.tweet username ; your text`",
            5,
        )
        return
    lion = await edit_or_reply(lionx, f"`Requesting {username} to tweet...`")
    text = deEmojify(text)
    await asyncio.sleep(2)
    lionxfile = await tweets(text, username)
    await lionx.client.send_file(lionx.chat_id, lionxfile, reply_to=reply_to_id)
    await lion.delete()
    if os.path.exists(lionxfile):
        os.remove(lionxfile)
