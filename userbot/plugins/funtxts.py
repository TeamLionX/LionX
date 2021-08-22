import nekos

from userbot import lionub

from ..funcs.managers import edit_or_reply

plugin_category = "fun"


@lionub.lion_cmd(
    pattern="tcat$",
    command=("tcat", plugin_category),
    info={
        "header": "Some random lion facial text art",
        "usage": "{tr}tcat",
    },
)
async def hmm(lion):
    "Some random lion facial text art"
    reactcat = nekos.textcat()
    await edit_or_reply(lion, reactcat)


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
    whycat = nekos.why()
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
    factcat = nekos.fact()
    await edit_or_reply(lion, factcat)
