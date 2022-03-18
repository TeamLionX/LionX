"""
designed By @Krishna_Singhal in userge
ported to telethon by @copyless786 and @TeamLionX
"""

import os

from glitch_this import ImageGlitcher
from PIL import Image

from userbot import lionxub

from ..funcs.managers import edit_delete
from ..helpers.utils import _lionxtools, _lionxutils, reply_id

plugin_category = "fun"


@lionxub.lionx_cmd(
    pattern="glitch(s)?(?: |$)([1-8])?",
    command=("glitch", plugin_category),
    info={
        "header": "Glitches the given Image.",
        "description": "Glitches the given mediafile (gif , stickers , image, videos) to a sticker/image and glitch range is from 1 to 8.\
                    If nothing is mentioned then by default it is 2",
        "options": {
            "glitch": "To output result as gif.",
            "glitchs": "To output result as sticker.",
        },
        "usage": ["{tr}glitch <1-8>", "{tr}glitch", "{tr}glitchs", "{tr}glitchs <1-8>"],
    },
)
async def glitch(event):
    "Glitches the given Image."
    cmd = event.pattern_match.group(1)
    lionxinput = event.pattern_match.group(2)
    reply = await event.get_reply_message()
    if not reply:
        return await edit_delete(event, "`Reply to supported Media...`")
    lionxid = await reply_id(event)
    if not os.path.isdir("./temp"):
        os.mkdir("./temp")
    lionxinput = int(lionxinput) if lionxinput else 2
    glitch_file = await _lionxtools.media_to_pic(event, reply)
    if glitch_file[1] is None:
        return await edit_delete(
            glitch_file[0], "__Unable to extract image from the replied message.__"
        )
    glitcher = ImageGlitcher()
    img = Image.open(glitch_file[1])
    if cmd:
        glitched = os.path.join("./temp", "glitched.webp")
        glitch_img = glitcher.glitch_image(img, lionxinput, color_offset=True)
        glitch_img.save(glitched)
        await event.client.send_file(event.chat_id, glitched, reply_to=lionxid)
    else:
        glitched = os.path.join("./temp", "glitched.gif")
        glitch_img = glitcher.glitch_image(img, lionxinput, color_offset=True, gif=True)
        DURATION = 200
        LOOP = 0
        glitch_img[0].save(
            glitched,
            format="GIF",
            append_images=glitch_img[1:],
            save_all=True,
            duration=DURATION,
            loop=LOOP,
        )
        amaan = await event.client.send_file(event.chat_id, glitched, reply_to=lionxid)
        await _lionxutils.unsavegif(event, amaan)
    await glitch_file[0].delete()
    for files in (glitch_file[1], glitched):
        if files and os.path.exists(files):
            os.remove(files)
