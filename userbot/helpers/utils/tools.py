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
        lionevent = await edit_or_reply(
            event, "`Transfiguration Time! Converting to ....`"
        )

    else:
        lionevent = event
    lionmedia = None
    lionfile = os.path.join("./temp/", "meme.png")
    if os.path.exists(lionfile):
        os.remove(lionfile)
    if mediatype == "Photo":
        lionmedia = await reply.download_media(file="./temp")
        im = Image.open(lionmedia)
        im.save(lionfile)
    elif mediatype in ["Audio", "Voice"]:
        await event.client.download_media(reply, lionfile, thumb=-1)
    elif mediatype == "Sticker":
        lionmedia = await reply.download_media(file="./temp")
        if lionmedia.endswith(".tgs"):
            lioncmd = f"lottie_convert.py --frame 0 -if lottie -of png '{lionmedia}' '{lionfile}'"
            stdout, stderr = (await runcmd(lioncmd))[:2]
            if stderr:
                LOGS.info(stdout + stderr)
        elif lionmedia.endswith(".webp"):
            im = Image.open(lionmedia)
            im.save(lionfile)
    elif mediatype in ["Round Video", "Video", "Gif"]:
        await event.client.download_media(reply, lionfile, thumb=-1)
        if not os.path.exists(lionfile):
            lionmedia = await reply.download_media(file="./temp")
            clip = VideoFileClip(media)
            try:
                clip = clip.save_frame(lionfile, 0.1)
            except Exception:
                clip = clip.save_frame(lionfile, 0)
    elif mediatype == "Document":
        mimetype = reply.document.mime_type
        mtype = mimetype.split("/")
        if mtype[0].lower() == "image":
            lionmedia = await reply.download_media(file="./temp")
            im = Image.open(lionmedia)
            im.save(lionfile)
    if lionmedia and os.path.lexists(lionmedia):
        os.remove(lionmedia)
    if os.path.lexists(lionfile):
        return lionevent, lionfile, mediatype
    return lionevent, None


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
