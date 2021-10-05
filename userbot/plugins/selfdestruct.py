from asyncio import sleep

from userbot import lionub
from userbot.funcs.logger import logging

plugin_category = "tools"
LOGS = logging.getLogger(__name__)


@lionub.lion_cmd(
    pattern="sdm (\d*) ([\s\S]*)",
    command=("sdm", plugin_category),
    info={
        "header": "To self destruct the message after paticualr time.",
        "description": "Suppose if you use .sdm 10 hi then message will be immediately send new message as hi and then after 10 sec this message will auto delete.",
        "usage": "{tr}sdm [number] [text]",
        "examples": "{tr}sdm 10 hi",
    },
)
async def selfdestruct(destroy):
    "To self destruct the sent message"
    lion = ("".join(destroy.text.split(maxsplit=1)[1:])).split(" ", 1)
    message = lion[1]
    ttl = int(lion[0])
    await destroy.delete()
    smsg = await destroy.client.send_message(destroy.chat_id, message)
    await sleep(ttl)
    await smsg.delete()


@lionub.lion_cmd(
    pattern="selfdm (\d*) ([\s\S]*)",
    command=("selfdm", plugin_category),
    info={
        "header": "To self destruct the message after paticualr time. and in message will show the time.",
        "description": "Suppose if you use .sdm 10 hi then message will be immediately will send new message as hi and then after 10 sec this message will auto delete.",
        "usage": "{tr}selfdm [number] [text]",
        "examples": "{tr}selfdm 10 hi",
    },
)
async def selfdestruct(destroy):
    "To self destruct the sent message"
    lion = ("".join(destroy.text.split(maxsplit=1)[1:])).split(" ", 1)
    message = lion[1]
    ttl = int(lion[0])
    text = message + f"\n\n`This message shall be self-destructed in {ttl} seconds`"

    await destroy.delete()
    smsg = await destroy.client.send_message(destroy.chat_id, text)
    await sleep(ttl)
    await smsg.delete()


@lionub.lion_cmd(
    pattern="slfchk$",
    command=("slfchk", plugin_category),
    info={
        "header": "To save any destructive pic",
        "usage": [
            "{tr}slfchk",
        ],
    },
)
async def oho(event):
    if not event.is_reply:
        return await event.edit("Reply to a self distructing pic !.!.!")
    k = await event.get_reply_message()
    pic = await k.download_media()
    await lionub.send_file(event.chat_id, pic)
    await event.delete()
