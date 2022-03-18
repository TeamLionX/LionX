import os
from typing import Optional

from moviepy.editor import VideoFileClip
from PIL import Image

from ...funcs.logger import logging
from ...funcs.managers import edit_or_reply
from ..tools import media_type
from .utils import runcmd

LOGS = logging.getLogger(__name__)


async def media_to_pic(event, reply, noedits=False):  # sourcery no-metrics
    mediatype = media_type(reply)
    if mediatype not in [
        "Photo",
        "Round Video",
        "Gif",
        "Sticker",
        "Video",
        "Voice",
        "Audio",
        "Document",
    ]:
        return event, None
    if not noedits:
        lionxevent = await edit_or_reply(
            event, "`Transfiguration Time! Converting to ....`"
        )

    else:
        lionxevent = event
    lionxmedia = None
    lionxfile = os.path.join("./temp/", "meme.png")
    if os.path.exists(lionxfile):
        os.remove(lionxfile)
    if mediatype == "Photo":
        lionxmedia = await reply.download_media(file="./temp")
        im = Image.open(lionxmedia)
        im.save(lionxfile)
    elif mediatype in ["Audio", "Voice"]:
        await event.client.download_media(reply, lionxfile, thumb=-1)
    elif mediatype == "Sticker":
        lionxmedia = await reply.download_media(file="./temp")
        if lionxmedia.endswith(".tgs"):
            lionxcmd = f"lottie_convert.py --frame 0 -if lottie -of png '{lionxmedia}' '{lionxfile}'"
            stdout, stderr = (await runcmd(lionxcmd))[:2]
            if stderr:
                LOGS.info(stdout + stderr)
        elif lionxmedia.endswith(".webp"):
            im = Image.open(lionxmedia)
            im.save(lionxfile)
    elif mediatype in ["Round Video", "Video", "Gif"]:
        await event.client.download_media(reply, lionxfile, thumb=-1)
        if not os.path.exists(lionxfile):
            lionxmedia = await reply.download_media(file="./temp")
            clip = VideoFileClip(media)
            try:
                clip = clip.save_frame(lionxfile, 0.1)
            except Exception:
                clip = clip.save_frame(lionxfile, 0)
    elif mediatype == "Document":
        mimetype = reply.document.mime_type
        mtype = mimetype.split("/")
        if mtype[0].lower() == "image":
            lionxmedia = await reply.download_media(file="./temp")
            im = Image.open(lionxmedia)
            im.save(lionxfile)
    if lionxmedia and os.path.lexists(lionxmedia):
        os.remove(lionxmedia)
    if os.path.lexists(lionxfile):
        return lionxevent, lionxfile, mediatype
    return lionxevent, None


async def take_screen_shot(
    video_file: str, duration: int, path: str = ""
) -> Optional[str]:
    thumb_image_path = path or os.path.join(
        "./temp/", f"{os.path.basename(video_file)}.jpg"
    )
    command = f"ffmpeg -ss {duration} -i '{video_file}' -vframes 1 '{thumb_image_path}'"
    err = (await runcmd(command))[1]
    if err:
        LOGS.error(err)
    return thumb_image_path if os.path.exists(thumb_image_path) else None
