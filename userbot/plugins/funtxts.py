import nekos

from userbot import lionub

from ..funcs.managers import edit_or_reply

plugin_category = "fun"


@lionub.lion_cmd(
    pattern="tlion$",
    command=("tlion", plugin_category),
    info={
        "header": "Some random lion facial text art",
        "usage": "{tr}tlion",
    },
)
async def hmm(lion):
    "Some random lion facial text art"
    reactlion = nekos.textlion()
    await edit_or_reply(lion, reactlion)


@lionub.lion_cmd(
    pattern="why$",
    command=("why", plugin_category),
    info={
        "header": "Sends you some random Funny questions",
        "usage": "{tr}why",
    },
)
async def hmm(lion):
    "Some random Funny questions"
    nekos.why()
    await edit_or_reply(lion, whycat)


@lionub.lion_cmd(
    pattern="fact$",
    command=("fact", plugin_category),
    info={
        "header": "Sends you some random facts",
        "usage": "{tr}fact",
    },
)
async def hmm(lion):
    "Some random facts"
    factlion = nekos.fact()
    await edit_or_reply(lion, factlion)
