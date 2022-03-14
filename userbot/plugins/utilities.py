import asyncio
import random
from datetime import timedelta

from telethon import functions
from telethon.errors import FloodWaitError
from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot import lionub

from ..funcs.managers import edit_delete, edit_or_reply
from . import mention

plugin_category = "utils"

chr = Config.COMMAND_HAND_LER
GBOT = "@HowGayBot"
FBOT = "@FsInChatBot"


@lionub.lion_cmd(
    pattern=r"timer(?:\s|$)([\s\S]*)",
    command=("timer", plugin_category),
    info={
        "header": "timer, try yourself",
        "note": "May not be accurate, especially for DC 5 users.",
        "description": "Timer like in clock, counts till 0 from given seconds.",
        "usage": "{tr}timer <seconds>",
    },
)
async def _(event):
    "Timer like in clock, counts till 0 from given seconds."
    if event.fwd_from:
        return
    try:
        total = event.pattern_match.group(1)
        if not total:
            await edit_delete(event, f"**Usage:** `{chr}timer <seconds>`", 10)
            return
        t = int(total)
        pluto = await edit_or_reply(event, "**Starting...**")
        while t >= 0:
            x = 3 if t > 300 else 1
            try:
                timer = timedelta(seconds=t)
                czy = str(timer).split(".")[0]
                await pluto.edit(czy)
                await asyncio.sleep(x - 0.01)
                t -= x
            except FloodWaitError as e:
                t -= e.seconds
                await asyncio.sleep(e.seconds)
        await pluto.edit(f"**⏱ Time Up!\n⌛️ Time: {total} seconds.**")
    except Exception as e:
        await edit_delete(event, f"`{e}`", 7)


@lionub.lion_cmd(
    pattern=r"gey(?:\s|$)([\s\S]*)",
    command=("gey", plugin_category),
    info={
        "header": "try yourself.",
        "description": "try yourself.",
        "usage": "{tr}gey <name>.",
    },
)
async def app_search(event):
    "try yourself"
    name = event.pattern_match.group(1)
    if not name:
        name = " "
    event = await edit_or_reply(event, "`Calculating!..`")
    id = await reply_id(event)
    try:
        score = await event.client.inline_query(GBOT, name)
        await score[0].click(event.chat_id, reply_to=id, hide_via=True)
        await event.delete()
    except Exception as err:
        await event.edit(str(err))


@lionub.lion_cmd(
    pattern=r"fr(?:\s|$)([\s\S]*)",
    command=("fr", plugin_category),
    info={
        "header": "Pay Respect.",
        "description": "Press F to Pay Respect.",
        "usage": "{tr}fr <text>.",
    },
)
async def app_search(event):
    "Press F to Pay Respect."
    czy = event.pattern_match.group(1)
    if not czy:
        czy = " "
    event = await edit_or_reply(event, "`Processing!..`")
    id = await reply_id(event)
    try:
        pluto = await event.client.inline_query(FBOT, czy)
        await pluto[0].click(event.chat_id, reply_to=id, hide_via=True)
        await event.delete()
    except Exception as err:
        await event.edit(str(err))


@lionub.lion_cmd(
    pattern=r"iapp(?:\s|$)([\s\S]*)",
    command=("iapp", plugin_category),
    info={
        "header": "To search any app in playstore via inline.",
        "description": "Searches the app in the playstore and provides the link to the app in playstore and fetches app details via inline.",
        "usage": "{tr}iapp <name>",
    },
)
async def app_search(event):
    "To search any app in playstore via inline."
    app_name = event.pattern_match.group(1)
    if not app_name:
        await edit_delete(event, f"**Usage:** `{chr}iapp <name>`", 10)
        return
    reply_to_id = await reply_id(event)
    APPBOT = "@nedzbot"
    cozyneko = "app" + app_name
    event = await edit_or_reply(event, "`Searching!..`")
    try:
        score = await event.client.inline_query(APPBOT, cozyneko)
        await score[0].click(event.chat_id, reply_to=reply_to_id, hide_via=True)
        await event.delete()
    except Exception as err:
        await event.edit("Exception Occured:- " + str(err))


@lionub.lion_cmd(
    pattern=r"cid(?:\s|$)([\s\S]*)",
    command=("cid", plugin_category),
    info={
        "header": "To search a phone number in Truecaller",
        "description": "Searches the given number in the truecaller and provides the details.",
        "usage": "{tr}cid <phone>",
    },
)
async def _(event):
    "To search a phone number in Truecaller"
    args = event.pattern_match.group(1)
    if not args:
        await edit_or_reply(event, f"**Usage:** `{chr}cid <number>`")
        return
    pluto = await edit_or_reply(event, "**__Fetching details...__**")
    chat = "@RespawnRobot"
    await reply_id(event)
    async with event.client.conversation(chat) as conv:
        try:
            await conv.send_message("/start")
            await conv.get_response()
            await conv.send_message("🏙 Theme")
            await conv.get_response()
            await conv.send_message("Box")
            await conv.get_response()
            await conv.send_message(args)
            check = await conv.get_response()
            replace = check.text
            info = replace.replace(chat, f"{mention}")
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await event.client(functions.contacts.UnblockRequest(chat))
            await edit_delete(
                pluto,
                f"__**An error occurred. Please try again!\n☞**__ `{chr}cid {args}`",
                10,
            )
            return
        await pluto.edit(info)
    await event.client.delete_dialog(chat)


@lionub.lion_cmd(
    pattern="mcq ?(.*)",
    command=("mcq", plugin_category),
    info={
        "header": "Chooses a random item in the given options, give a comma ',' to add multiple option",
        "usage": ["{tr}mcq <options>", "{tr}mcq a,b,c,d", "{tr}mcq cat,dog,life,death"],
    },
)
async def Gay(event):
    "Chooses a random item in the given options, give a comma ',' to add multiple option"
    osho = event.pattern_match.group(1)
    if not osho:
        return await edit_delete(event, "`What to choose from`", 10)
    options = osho.split(",")
    await event.edit(f"**Input:** `{osho}`\n**Random:** `{random.choice(options)}`")
