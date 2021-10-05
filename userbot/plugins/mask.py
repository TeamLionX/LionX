# credits to @Simpleboy786 and @SimpleBoy786

import os

from telegraph import exceptions, upload_file
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot import lionub

from ..Config import Config
from ..funcs.managers import edit_or_reply
from . import awooify, baguette, convert_toimage, iphonex, lolice

plugin_category = "extra"


@lionub.lion_cmd(
    pattern="mask$",
    command=("mask", plugin_category),
    info={
        "header": "reply to image to get hazmat suit for that image.",
        "usage": "{tr}mask",
    },
)
async def _(lionbot):
    "Hazmat suit maker"
    reply_message = await lionbot.get_reply_message()
    if not reply_message.media or not reply_message:
        return await edit_or_reply(lionbot, "```reply to media message```")
    chat = "@hazmat_suit_bot"
    if reply_message.sender.bot:
        return await edit_or_reply(lionbot, "```Reply to actual users message.```")
    event = await lionbot.edit("```Processing```")
    async with lionbot.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=905164246)
            )
            await lionbot.client.send_message(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            return await event.edit(
                "```Please unblock @hazmat_suit_bot and try again```"
            )
        if response.text.startswith("Forward"):
            await event.edit(
                "```can you kindly disable your forward privacy settings for good?```"
            )
        else:
            await lionbot.client.send_file(event.chat_id, response.message.media)
            await event.delete()


@lionub.lion_cmd(
    pattern="awooify$",
    command=("awooify", plugin_category),
    info={
        "header": "Check yourself by replying to image.",
        "usage": "{tr}awooify",
    },
)
async def lionbot(lionmemes):
    "replied Image will be face of other image"
    replied = await lionmemes.get_reply_message()
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    if not replied:
        return await edit_or_reply(lionmemes, "reply to a supported media file")
    if replied.media:
        lionevent = await edit_or_reply(lionmemes, "passing to telegraph...")
    else:
        return await edit_or_reply(lionmemes, "reply to a supported media file")
    download_location = await lionmemes.client.download_media(
        replied, Config.TMP_DOWNLOAD_DIRECTORY
    )
    if download_location.endswith((".webp")):
        download_location = convert_toimage(download_location)
    size = os.stat(download_location).st_size
    if download_location.endswith((".jpg", ".jpeg", ".png", ".bmp", ".ico")):
        if size > 5242880:
            os.remove(download_location)
            return await lionevent.edit(
                "the replied file size is not supported it must me below 5 mb"
            )
        await lionevent.edit("generating image..")
    else:
        os.remove(download_location)
        return await lionevent.edit("the replied file is not supported")
    try:
        response = upload_file(download_location)
        os.remove(download_location)
    except exceptions.TelegraphException as exc:
        os.remove(download_location)
        return await lionevent.edit("ERROR: " + str(exc))
    lion = f"https://telegra.ph{response[0]}"
    lion = await awooify(lion)
    await lionevent.delete()
    await lionmemes.client.send_file(lionmemes.chat_id, lion, reply_to=replied)


@lionub.lion_cmd(
    pattern="lolice$",
    command=("lolice", plugin_category),
    info={
        "header": "image masker check your self by replying to image.",
        "usage": "{tr}lolice",
    },
)
async def lionbot(lionmemes):
    "replied Image will be face of other image"
    replied = await lionmemes.get_reply_message()
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    if not replied:
        return await edit_or_reply(lionmemes, "reply to a supported media file")
    if replied.media:
        lionevent = await edit_or_reply(lionmemes, "passing to telegraph...")
    else:
        return await edit_or_reply(lionmemes, "reply to a supported media file")
    download_location = await lionmemes.client.download_media(
        replied, Config.TMP_DOWNLOAD_DIRECTORY
    )
    if download_location.endswith((".webp")):
        download_location = convert_toimage(download_location)
    size = os.stat(download_location).st_size
    if download_location.endswith((".jpg", ".jpeg", ".png", ".bmp", ".ico")):
        if size > 5242880:
            os.remove(download_location)
            return await lionevent.edit(
                "the replied file size is not supported it must me below 5 mb"
            )
        await lionevent.edit("generating image..")
    else:
        os.remove(download_location)
        return await lionevent.edit("the replied file is not supported")
    try:
        response = upload_file(download_location)
        os.remove(download_location)
    except exceptions.TelegraphException as exc:
        os.remove(download_location)
        return await lionevent.edit("ERROR: " + str(exc))
    lion = f"https://telegra.ph{response[0]}"
    lion = await lolice(lion)
    await lionevent.delete()
    await lionmemes.client.send_file(lionmemes.chat_id, lion, reply_to=replied)


@lionub.lion_cmd(
    pattern="bun$",
    command=("bun", plugin_category),
    info={
        "header": "reply to image and check yourself.",
        "usage": "{tr}bun",
    },
)
async def lionbot(lionmemes):
    "replied Image will be face of other image"
    replied = await lionmemes.get_reply_message()
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    if not replied:
        return await edit_or_reply(lionmemes, "reply to a supported media file")
    if replied.media:
        lionevent = await edit_or_reply(lionmemes, "passing to telegraph...")
    else:
        return await edit_or_reply(lionmemes, "reply to a supported media file")
    download_location = await lionmemes.client.download_media(
        replied, Config.TMP_DOWNLOAD_DIRECTORY
    )
    if download_location.endswith((".webp")):
        download_location = convert_toimage(download_location)
    size = os.stat(download_location).st_size
    if download_location.endswith((".jpg", ".jpeg", ".png", ".bmp", ".ico")):
        if size > 5242880:
            os.remove(download_location)
            return await lionevent.edit(
                "the replied file size is not supported it must me below 5 mb"
            )
        await lionevent.edit("generating image..")
    else:
        os.remove(download_location)
        return await lionevent.edit("the replied file is not supported")
    try:
        response = upload_file(download_location)
        os.remove(download_location)
    except exceptions.TelegraphException as exc:
        os.remove(download_location)
        return await lionevent.edit("ERROR: " + str(exc))
    lion = f"https://telegra.ph{response[0]}"
    lion = await baguette(lion)
    await lionevent.delete()
    await lionmemes.client.send_file(lionmemes.chat_id, lion, reply_to=replied)


@lionub.lion_cmd(
    pattern="iphx$",
    command=("iphx", plugin_category),
    info={
        "header": "replied image as iphone x wallpaper.",
        "usage": "{tr}iphx",
    },
)
async def lionbot(lionmemes):
    "replied image as iphone x wallpaper."
    replied = await lionmemes.get_reply_message()
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    if not replied:
        return await edit_or_reply(lionmemes, "reply to a supported media file")
    if replied.media:
        lionevent = await edit_or_reply(lionmemes, "passing to telegraph...")
    else:
        return await edit_or_reply(lionmemes, "reply to a supported media file")
    download_location = await lionmemes.client.download_media(
        replied, Config.TMP_DOWNLOAD_DIRECTORY
    )
    if download_location.endswith((".webp")):
        download_location = convert_toimage(download_location)
    size = os.stat(download_location).st_size
    if download_location.endswith((".jpg", ".jpeg", ".png", ".bmp", ".ico")):
        if size > 5242880:
            os.remove(download_location)
            return await lionevent.edit(
                "the replied file size is not supported it must me below 5 mb"
            )
        await lionevent.edit("generating image..")
    else:
        os.remove(download_location)
        return await lionevent.edit("the replied file is not supported")
    try:
        response = upload_file(download_location)
        os.remove(download_location)
    except exceptions.TelegraphException as exc:
        os.remove(download_location)
        return await lionevent.edit("ERROR: " + str(exc))
    lion = f"https://telegra.ph{response[0]}"
    lion = await iphonex(lion)
    await lionevent.delete()
    await lionmemes.client.send_file(lionmemes.chat_id, lion, reply_to=replied)
