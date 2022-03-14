import asyncio
import io
import logging
import os
import urllib

from PIL import Image, ImageDraw, ImageFont

from ..funcs.managers import edit_delete, edit_or_reply
from ..helpers.functions import convert_tosticker, higlighted_text
from . import deEmojify, edit_delete, edit_or_reply, lionub, reply_id

plugin_category = "fun"
logger = logging.getLogger(__name__)


@lionub.lion_cmd(
    pattern="tgs ?(.*)",
    command=("tgs", plugin_category),
    info={
        "header": "Destory a sticker",
        "usage": "{tr}tgs <reply to a animated sticker>",
    },
)
async def tgscmd(message):
    """Tgs Killer"""
    reply = await message.get_reply_message()
    if not reply:
        await edit_delete(message, "`Reply to an animated sticker`", 3)
        return
    if not reply.file.name.endswith(".tgs"):
        await edit_delete(message, "`Reply to an animated sticker`", 3)
        return
    await reply.download_media("tgs.tgs")
    await edit_or_reply(message, "`Fixing this sticker...`")
    os.system("lottie_convert.py tgs.tgs json.json")
    with open("json.json", "r") as json:
        jsn = json.read()
    jsn = (
        jsn.replace("[1]", "[20]")
        .replace("[2]", "[30]")
        .replace("[3]", "[40]")
        .replace("[4]", "[50]")
        .replace("[5]", "[60]")
    )

    open("json.json", "w").write(jsn)
    os.system("lottie_convert.py json.json tgs.tgs")
    await message.reply(file="tgs.tgs")
    os.remove("json.json")
    os.remove("tgs.tgs")
    await message.delete()


@lionub.lion_cmd(
    pattern="doti ?(.*)",
    command=("doti", plugin_category),
    info={
        "header": "Image to Colorful dots",
        "description": "The bigger, the slower and bugger! Recommended not more than 1000",
        "usage": [
            "{tr}doti <reply to image> [deafult is 100]",
            "{tr}doti <count> <reply to image>",
        ],
    },
)
async def dotifycmd(message):
    """Image to RGB dots"""
    mode = False
    reply, pix = await parse(message)
    if reply:
        await dotify(message, reply, pix, mode)


@lionub.lion_cmd(
    pattern="doty ?(.*)",
    command=("doty", plugin_category),
    info={
        "header": "Image to BW dots",
        "description": "The bigger, the slower and bugger! Recommended not more than 1000",
        "usage": [
            "{tr}doty <reply to image> [deafult is 100]",
            "{tr}doty <count> <reply to image>",
        ],
    },
)
async def dotificmd(message):
    """Image to BW dots"""
    mode = True
    reply, pix = await parse(message)
    if reply:
        await dotify(message, reply, pix, mode)


async def parse(message):
    reply = await message.get_reply_message()
    if not reply:
        await edit_delete(message, "<b>Reply to an Image!</b>", 3, parse_mode="html")
        return None, None
    args = message.pattern_match.group(1).split(" ", 1)
    pix = 100
    if args:
        args = args[0]
        if args.isdigit():
            pix = int(args) if int(args) > 0 else 100
    return reply, pix


async def dotify(message, reply, pix, mode):
    await edit_or_reply(message, "<b>Putting dots...</b>", parse_mode="html")
    count = 24
    im_ = Image.open(io.BytesIO(await reply.download_media(bytes)))
    if im_.mode == "RGBA":
        temp = Image.new("RGB", im_.size, "#000")
        temp.paste(im_, (0, 0), im_)
        im_ = temp

    im = im_.convert("L")
    im_ = im if mode else im_
    [_.thumbnail((pix, pix)) for _ in [im, im_]]
    w, h = im.size
    img = Image.new(im_.mode, (w * count + (count // 2), h * count + (count // 2)), 0)
    ImageDraw.Draw(img)

    def cirsle(im, x, y, r, fill):
        x += r // 2
        y += r // 2
        draw = ImageDraw.Draw(im)
        draw.ellipse((x - r, y - r, x + r, y + r), fill)
        return im

    _x = _y = count // 2
    for x in range(w):
        for y in range(h):
            r = im.getpixel((x, y))
            fill = im_.getpixel((x, y))
            cirsle(img, _x, _y, r // count, fill)
            _y += count
        _x += count
        _y = count // 2

    out = io.BytesIO()
    out.name = "out.png"
    img.save(out)
    out.seek(0)
    await reply.reply(file=out)
    await message.delete()


@lionub.lion_cmd(
    pattern=r"(|h)pay(?:\s|$)([\s\S]*)",
    command=("pay", plugin_category),
    info={
        "header": "Send money to anyone through paytm.",
        "flags": {
            "h": "To create paytm sticker with highlighted font.",
        },
        "usage": [
            "{tr}pay <text/reply to msg>",
            "{tr}hpay <text/reply to msg>",
        ],
        "examples": [
            "{tr}pay Shasa",
            "{tr}hpay LionX",
        ],
    },
)
async def pay(event):
    "To create $1000 paytm payment sticker with the receiver name that you want."
    vinuxd = event.pattern_match.group(1).lower()
    text = event.pattern_match.group(2)
    czyneko = await reply_id(event)
    if not text and event.is_reply:
        text = (await event.get_reply_message()).message
    if not text:
        return await edit_delete(
            event, "__**To whom do you want to send money? Gib his/her name!**__", 7
        )
    cozyneko = await edit_or_reply(
        event, f"__**Wait, Transferring $1000 to {text}...**__"
    )
    await asyncio.sleep(1.2)
    if not os.path.isdir("./temp"):
        os.mkdir("./temp")
    temp_name = "./temp/pay_temp.jpg"
    file_name = "./temp/pay.jpg"
    vinu = urllib.request.urlretrieve(
        "https://telegra.ph/file/847a028fbf453f1c83fc8.jpg", temp_name
    )
    text = deEmojify(text)
    await cozyneko.edit("__**Processed Transferring! Waiting for confirmation...**__")
    await asyncio.sleep(1.2)
    font, wrap = (65, 1) if len(text) < 90 else (65, 1)
    bg, fg, alpha, ls = (
        ("black", "white", 255, "5") if vinuxd == "h" else ("white", "black", 0, "-40")
    )
    higlighted_text(
        temp_name,
        text,
        file_name,
        text_wrap=wrap,
        font_size=font,
        linespace=ls,
        position=(3, 580),
        align="left",
        background=bg,
        foreground=fg,
        transparency=alpha,
    )
    realnub = convert_tosticker(file_name)
    await cozyneko.edit("__**Transfered Successfully, Uploading Receipt...**__")
    await asyncio.sleep(1.2)
    await event.client.send_file(
        event.chat_id, realnub, reply_to=czyneko, force_document=False
    )
    await event.delete()
    for files in (temp_name, file_name):
        if files and os.path.exists(files):
            os.remove(files)


@lionub.lion_cmd(
    pattern=r"write(?:\s|$)([\s\S]*)",
    command=("write", plugin_category),
    info={
        "header": "To write given text or replied message on paper.",
        "usage": "{tr}write <message/reply>",
        "examples": "{tr}write Hello World",
    },
)
async def writer(e):
    if e.reply_to:
        reply = await e.get_reply_message()
        text = reply.message
    elif e.pattern_match.group(1):
        text = e.text.split(maxsplit=1)[1]
    else:
        return await edit_delete(e, "`Give Some Text`")
    template = "downloads/template.png"
    if os.path.exists("downloads/template.png"):
        os.remove(template)
    urllib.request.urlretrieve(
        "https://raw.githubusercontent.com/TeamLionX/Files/main/template/template.jpg",
        template,
    )
    Image.open(template)
    await edit_delete(e, "`Writing...`")
    fonts = "downloads/assfont.ttf"
    if os.path.exists("downloads/assfont.ttf"):
        os.remove(fonts)
    urllib.request.urlretrieve(
        "https://github.com/TeamLionX/Files/blob/main/fonts/assfont.ttf?raw=true", fonts
    )
    Image.open(template)
    img = Image.open(template)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(fonts, 30)
    x, y = 150, 140
    (text)
    line_height = font.getsize("hg")[1]
    draw.text((x, y), text, fill=(1, 22, 55), font=font)
    y = y + line_height - 5
    file = "pic.jpg"
    img.save(file)
    await e.reply(file=file)
    os.remove(file)


@lionub.lion_cmd(
    pattern=r"twrite(?:\s|$)([\s\S]*)",
    command=("twrite", plugin_category),
    info={
        "header": "To write given text or replied message on paper.",
        "usage": "{tr}twrite <message/reply>",
        "examples": "{tr}twrite Hello World",
    },
)
async def writer(e):
    if e.reply_to:
        reply = await e.get_reply_message()
        text = reply.message
    elif e.pattern_match.group(1):
        text = e.text.split(maxsplit=1)[1]
    else:
        return await edit_delete(e, "`Give Some Text`")
    template = "downloads/template.png"
    if os.path.exists("downloads/template.png"):
        os.remove(template)
    urllib.request.urlretrieve(
        "https://raw.githubusercontent.com/TeamLionX/Files/main/template/template.jpg",
        template,
    )
    Image.open(template)
    await edit_delete(e, "`Writing...`")
    fonts = "downloads/Homemade_Apple.zip"
    if os.path.exists("downloads/Homemade_Apple.zip"):
        os.remove(fonts)
    urllib.request.urlretrieve(
        "https://github.com/TeamLionX/Files/blob/main/fonts/Homemade_Apple.zip?raw=true",
        fonts,
    )
    Image.open(template)
    img = Image.open(template)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(fonts, 30)
    x, y = 150, 140
    (text)
    line_height = font.getsize("hg")[1]
    draw.text((x, y), text, fill=(1, 22, 55), font=font)
    y = y + line_height - 5
    file = "pic.jpg"
    img.save(file)
    await e.reply(file=file)
    os.remove(file)
