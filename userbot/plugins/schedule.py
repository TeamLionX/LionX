from asyncio import sleep

from userbot import lionub

plugin_category = "utils"


@lionub.lion_cmd(
    pattern="schd (\d*) ([\s\S]*)",
    command=("schd", plugin_category),
    info={
        "header": "To schedule a message after given time(in seconds).",
        "usage": "{tr}schd <time_in_seconds>  <message to send>",
        "examples": "{tr}schd 120 hello",
    },
)
async def _(event):
    "To schedule a message after given time"
    lion = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 1)
    message = lion[1]
    ttl = int(lion[0])
    await event.delete()
    await sleep(ttl)
    await event.respond(message)
