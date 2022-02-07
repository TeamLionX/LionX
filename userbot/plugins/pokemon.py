import os
from asyncio import sleep

import requests
from bs4 import BeautifulSoup

from userbot.sql_helper.poke_sql import add_grp, get_all_grp, is_pokemon, rm_grp

from . import *

plugin_category = "utils"

qt = "Pokemon appeared!"
qt_bots = ["5020806573"]


def progress(current, total):
    logger.info(
        "Downloaded {} of {}\nCompleted {}".format(
            current, total, (current / total) * 100
        )
    )


@lionub.lion_cmd(
    pattern="ct$",
    command=("ct", plugin_category),
    info={
        "header": "To catch Pokemon",
        "options": "This will help you to catch Pokemon",
        "usage": [
            "{tr}ct",
        ],
    },
)
async def _(event):
    lionevent = await edit_or_reply(event, "pika..")
    BASE_URL = "http://images.google.com"
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        previous_message_text = previous_message.message
        if previous_message.media:
            downloaded_file_name = await event.client.download_media(
                previous_message, Config.TMP_DOWNLOAD_DIRECTORY
            )
            SEARCH_URL = "{}/searchbyimage/upload".format(BASE_URL)
            multipart = {
                "encoded_image": (
                    downloaded_file_name,
                    open(downloaded_file_name, "rb"),
                ),
                "image_content": "",
            }
            google_rs_response = requests.post(
                SEARCH_URL, files=multipart, allow_redirects=False
            )
            the_location = google_rs_response.headers.get("Location")
            os.remove(downloaded_file_name)
        else:
            previous_message_text = previous_message.message
            SEARCH_URL = "{}/searchbyimage?image_url={}"
            request_url = SEARCH_URL.format(BASE_URL, previous_message_text)
            google_rs_response = requests.get(request_url, allow_redirects=False)
            the_location = google_rs_response.headers.get("Location")
        headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:58.0) Gecko/20100101 Firefox/58.0"
        }
        response = requests.get(the_location, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")
        prs_div = soup.find_all("div", {"class": "r5a77d"})[0]
        prs_anchor_element = prs_div.find("a")
        prs_url = BASE_URL + prs_anchor_element.get("href")
        prs_text = prs_anchor_element.text
        img_size_div = soup.find(id="jHnbRc")
        img_size = img_size_div.find_all("div")
        OUTPUT_STR = """/catch {prs_text}""".format(**locals())
    await lionevent.edit(OUTPUT_STR, parse_mode="HTML", link_preview=False)


@lionub.lion_cmd()
async def _(event):
    if not event.media:
        return
    if not qt in event.text:
        return
    if str(event.sender_id) not in qt_bots:
        return
    all_grp = get_all_grp()
    if len(all_grp) == 0:
        return
    for grps in all_grp:
        if int(grps.chat_id) == event.chat_id:
            try:
                dl = await event.client.download_media(event.media, "resources/")
                file = {"encoded_image": (dl, open(dl, "rb"))}
                grs = requests.post(
                    "https://www.google.com/searchbyimage/upload",
                    files=file,
                    allow_redirects=False,
                )
                loc = grs.headers.get("Location")
                response = requests.get(
                    loc,
                    headers={
                        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:58.0) Gecko/20100101 Firefox/58.0"
                    },
                )
                qtt = BeautifulSoup(response.text, "html.parser")
                div = qtt.find_all("div", {"class": "r5a77d"})[0]
                alls = div.find("a")
                text = alls.text
                try:
                    if "cg" in text:
                        return
                    if "fictional character" in text:
                        return
                except:
                    pass
                lionevent = await event.client.send_message(
                    event.chat_id, f"/catch {text}"
                )
                await sleep(2)
                await lionevent.delete()
                os.remove(dl)
            except:
                pass
        else:
            pass


@lionub.lion_cmd(
    pattern="addpoke$",
    command=("addpoke", plugin_category),
    info={
        "header": "To catch auto Pokemon",
        "options": "This will Catch All pokemon Automatic",
        "usage": [
            "{tr}addpoke",
        ],
    },
)
async def _(event):
    if not event.is_group:
        await edit_delete(event, "Auto Pokemon works in Groups Only !!")
        return
    if is_pokemon(str(event.chat_id)):
        await edit_delete(event, "This Chat is Already In Auto Pokemon Database !!")
        return
    add_grp(str(event.chat_id))
    await edit_delete(
        event,
        f"**Added Chat** {event.chat.title} **With Id** `{event.chat_id}` **To Auto Pokemon Database.**",
    )


@lionub.lion_cmd(
    pattern="stoppoke$",
    command=("stoppoke", plugin_category),
    info={
        "header": "To Stop Auto Catch",
        "options": "This will help you to stop auto catch",
        "usage": [
            "{tr}stoppoke",
        ],
    },
)
async def _(event):
    if not event.is_group:
        await edit_delete(event, "Auto Pokemon works in groups only !!")
        return
    if not is_pokemon(str(event.chat_id)):
        await edit_delete(event, "Auto Pokemon was already disabled here.")
        return
    rm_grp(str(event.chat_id))
    await edit_delete(
        event,
        f"**Removed Chat** {event.chat.title} **With Id** `{event.chat_id}` **From Auto Pokemon Database.**",
    )


@lionub.lion_cmd(
    pattern="listpoke$",
    command=("listpoke", plugin_category),
    info={
        "header": "To check current chat of auto Pokemon",
        "options": "This will help you to check where auto Pokemon is currently enable",
        "usage": [
            "{tr}listpoke",
        ],
    },
)
async def _(event):
    lionevent = await edit_or_reply(event, "Fetching Auto Pokemon chats...")
    all_grp = get_all_grp()
    x = "**Auto Pokemon enabled chats :** \n\n"
    for i in all_grp:
        ch = i.chat_id
        cht = int(ch)
        x += f"• `{cht}`\n"
    await lionevent.edit(x)
