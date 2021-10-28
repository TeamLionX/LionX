from userbot import lionub

from ..funcs.logger import logging
from ..funcs.managers import edit_or_reply

LOGS = logging.getLogger(os.path.basename(__name__))
plugin_category = "extra"

import os

from multiutility import EmojiCreator

Emoji = EmojiCreator()


@lionub.lion_cmd(
    pattern="randomoji",
    command=("randommoji", plugin_category),
    info={
        "header": "get random emoji in image format",
        "usage": ["{tr}randomoji"],
        "examples": ["{tr}randomoji"],
    },
)
async def _(event):
    mmmm = await edit_or_reply(event, "**Generating Your Random Emoji ⏰✍️**")
    emoji = Emoji.get_random()
    await event.respond("**--- Random Emoji For You ---**", file=emoji)
    os.remove(emoji)
    await mmmm.delete()
