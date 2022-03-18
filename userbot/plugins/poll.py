import random

from telethon.errors.rpcbaseerrors import ForbiddenError
from telethon.errors.rpcerrorlist import PollOptionInvalidError
from telethon.tl.types import InputMediaPoll, Poll

from userbot import lionxub

from ..funcs.managers import edit_or_reply
from . import Build_Poll, reply_id

plugin_category = "extra"


@lionxub.lionx_cmd(
    pattern="poll(?:\s|$)([\s\S]*)",
    command=("poll", plugin_category),
    info={
        "header": "To create a poll.",
        "description": "If you doesnt give any input it sends a default poll",
        "usage": ["{tr}poll", "{tr}poll question ; option 1; option2"],
        "examples": "{tr}poll Are you an early bird or a night owl ;Early bird ; Night owl",
    },
)
async def pollcreator(lionxpoll):
    "To create a poll"
    reply_to_id = await reply_id(lionxpoll)
    string = "".join(lionxpoll.text.split(maxsplit=1)[1:])
    if not string:
        options = Build_Poll(["Yah sure 😊✌️", "Nah 😏😕", "Whatever die sur 🥱🙄"])
        try:
            await lionxpoll.client.send_message(
                lionxpoll.chat_id,
                file=InputMediaPoll(
                    poll=Poll(
                        id=random.getrandbits(32),
                        question="👆👆So do you guys agree with this?",
                        answers=options,
                    )
                ),
                reply_to=reply_to_id,
            )
            await lionxpoll.delete()
        except PollOptionInvalidError:
            await edit_or_reply(
                lionxpoll, "`A poll option used invalid data (the data may be too long).`"
            )
        except ForbiddenError:
            await edit_or_reply(lionxpoll, "`This chat has forbidden the polls`")
        except exception as e:
            await edit_or_reply(lionxpoll, str(e))
    else:
        lionxinput = string.split(";")
        if len(lionxinput) > 2 and len(lionxinput) < 12:
            options = Build_Poll(lionxinput[1:])
            try:
                await lionxpoll.client.send_message(
                    lionxpoll.chat_id,
                    file=InputMediaPoll(
                        poll=Poll(
                            id=random.getrandbits(32),
                            question=lionxinput[0],
                            answers=options,
                        )
                    ),
                    reply_to=reply_to_id,
                )
                await lionxpoll.delete()
            except PollOptionInvalidError:
                await edit_or_reply(
                    lionxpoll,
                    "`A poll option used invalid data (the data may be too long).`",
                )
            except ForbiddenError:
                await edit_or_reply(lionxpoll, "`This chat has forbidden the polls`")
            except Exception as e:
                await edit_or_reply(lionxpoll, str(e))
        else:
            await edit_or_reply(
                lionxpoll,
                "Make sure that you used Correct syntax `.poll question ; option1 ; option2`",
            )
