import asyncio
from datetime import datetime

from telethon.errors import BadRequestError
from telethon.tl.functions.channels import EditAdminRequest, EditBannedRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import (
    ChatAdminRights,
    ChatBannedRights,
    MessageEntityMentionName,
)
from telethon.utils import get_display_name

from userbot import lionub

from ..funcs.devs import DEVLIST
from ..funcs.managers import edit_delete, edit_or_reply
from ..helpers.utils import _format
from ..sql_helper import gban_sql_helper as gban_sql
from ..sql_helper.mute_sql import is_muted, mute, unmute
from . import BOTLOG, BOTLOG_CHATID, admin_groups, get_user_from_event

plugin_category = "admin"

BANNED_RIGHTS = ChatBannedRights(
    until_date=None,
    view_messages=True,
    send_messages=True,
    send_media=True,
    send_stickers=True,
    send_gifs=True,
    send_games=True,
    send_inline=True,
    embed_links=True,
)

UNBAN_RIGHTS = ChatBannedRights(
    until_date=None,
    send_messages=None,
    send_media=None,
    send_stickers=None,
    send_gifs=None,
    send_games=None,
    send_inline=None,
    embed_links=None,
)


@lionub.lion_cmd(
    pattern="gban(?:\s|$)([\s\S]*)",
    command=("gban", plugin_category),
    info={
        "header": "To ban user in every group where you are admin.",
        "description": "Will ban the person in every group where you are admin only.",
        "usage": "{tr}gban <username/reply/userid> <reason (optional)>",
    },
)
async def liongban(event):  # sourcery no-metrics
    "To ban user in every group where you are admin."
    lionz = await edit_or_reply(event, "`gbanning.......`")
    start = datetime.now()
    user, reason = await get_user_from_event(event, lionz)
    if not user:
        return
    if user.id == lionub.uid:
        return await edit_delete(lionz, "`why would I ban myself`")
    if str(user.id) in DEVLIST:
        return await edit_delete(lionz, "🥴 **GBan my creator ?¿ Really‽**")

    if gban_sql.is_gbanned(user.id):
        await lionz.edit(
            f"`the `[user](tg://user?id={user.id})` is already in gbanned list any way checking again`"
        )
    else:
        gban_sql.liongban(user.id, reason)
    san = await admin_groups(event.client)
    count = 0
    madboy = len(san)
    if madboy == 0:
        return await edit_delete(lionz, "`you are not admin of atleast one group` ")
    await lionz.edit(
        f"`initiating gban of the `[user](tg://user?id={user.id}) `in {len(san)} groups`"
    )
    for i in range(madboy):
        try:
            await event.client(EditBannedRequest(san[i], user.id, BANNED_RIGHTS))
            await asyncio.sleep(0.5)
            count += 1
        except BadRequestError:
            achat = await event.client.get_entity(san[i])
            await event.client.send_message(
                BOTLOG_CHATID,
                f"`You don't have required permission in :`\n**Chat :** {get_display_name(achat)}(`{achat.id}`)\n`For banning here`",
            )
    end = datetime.now()
    liontaken = (end - start).seconds
    if reason:
        await lionz.edit(
            f"[{user.first_name}](tg://user?id={user.id}) `was gbanned in {count} groups in {liontaken} seconds`!!\n**Reason :** `{reason}`"
        )
    else:
        await lionz.edit(
            f"[{user.first_name}](tg://user?id={user.id}) `was gbanned in {count} groups in {liontaken} seconds`!!"
        )
    if BOTLOG and count != 0:
        reply = await event.get_reply_message()
        if reason:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"#GBAN\
                \nGlobal Ban\
                \n**User : **[{user.first_name}](tg://user?id={user.id})\
                \n**ID : **`{user.id}`\
                \n**Reason :** `{reason}`\
                \n__Banned in {count} groups__\
                \n**Time taken : **`{liontaken} seconds`",
            )
        else:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"#GBAN\
                \nGlobal Ban\
                \n**User : **[{user.first_name}](tg://user?id={user.id})\
                \n**ID : **`{user.id}`\
                \n__Banned in {count} groups__\
                \n**Time taken : **`{liontaken} seconds`",
            )
        try:
            if reply:
                await reply.forward_to(BOTLOG_CHATID)
                await reply.delete()
        except BadRequestError:
            pass


@lionub.lion_cmd(
    pattern="ungban(?:\s|$)([\s\S]*)",
    command=("ungban", plugin_category),
    info={
        "header": "To unban the person from every group where you are admin.",
        "description": "will unban and also remove from your gbanned list.",
        "usage": "{tr}ungban <username/reply/userid>",
    },
)
async def liongban(event):
    "To unban the person from every group where you are admin."
    lionz = await edit_or_reply(event, "`ungbanning.....`")
    start = datetime.now()
    user, reason = await get_user_from_event(event, lionz)
    if not user:
        return
    if gban_sql.is_gbanned(user.id):
        gban_sql.lionungban(user.id)
    else:
        return await edit_delete(
            lionz, f"the [user](tg://user?id={user.id}) `is not in your gbanned list`"
        )
    san = await admin_groups(event.client)
    count = 0
    madboy = len(san)
    if madboy == 0:
        return await edit_delete(
            lionz, "`you are not even admin of atleast one group `"
        )
    await lionz.edit(
        f"initiating ungban of the [user](tg://user?id={user.id}) in `{len(san)}` groups"
    )
    for i in range(madboy):
        try:
            await event.client(EditBannedRequest(san[i], user.id, UNBAN_RIGHTS))
            await asyncio.sleep(0.5)
            count += 1
        except BadRequestError:
            achat = await event.client.get_entity(san[i])
            await event.client.send_message(
                BOTLOG_CHATID,
                f"`You don't have required permission in :`\n**Chat :** {get_display_name(achat)}(`{achat.id}`)\n`For Unbanning here`",
            )
    end = datetime.now()
    liontaken = (end - start).seconds
    if reason:
        await lionz.edit(
            f"[{user.first_name}](tg://user?id={user.id}`) was ungbanned in {count} groups in {liontaken} seconds`!!\n**Reason :** `{reason}`"
        )
    else:
        await lionz.edit(
            f"[{user.first_name}](tg://user?id={user.id}) `was ungbanned in {count} groups in {liontaken} seconds`!!"
        )

    if BOTLOG and count != 0:
        if reason:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"#UNGBAN\
                \nGlobal Unban\
                \n**User : **[{user.first_name}](tg://user?id={user.id})\
                \n**ID : **`{user.id}`\
                \n**Reason :** `{reason}`\
                \n__Unbanned in {count} groups__\
                \n**Time taken : **`{liontaken} seconds`",
            )
        else:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"#UNGBAN\
                \nGlobal Unban\
                \n**User : **[{user.first_name}](tg://user?id={user.id})\
                \n**ID : **`{user.id}`\
                \n__Unbanned in {count} groups__\
                \n**Time taken : **`{liontaken} seconds`",
            )


@lionub.lion_cmd(
    pattern="listgban$",
    command=("listgban", plugin_category),
    info={
        "header": "Shows you the list of all gbanned users by you.",
        "usage": "{tr}listgban",
    },
)
async def gablist(event):
    "Shows you the list of all gbanned users by you."
    gbanned_users = gban_sql.get_all_gbanned()
    GBANNED_LIST = "Current Gbanned Users\n"
    if len(gbanned_users) > 0:
        for a_user in gbanned_users:
            if a_user.reason:
                GBANNED_LIST += f"👉 [{a_user.chat_id}](tg://user?id={a_user.chat_id}) for {a_user.reason}\n"
            else:
                GBANNED_LIST += (
                    f"👉 [{a_user.chat_id}](tg://user?id={a_user.chat_id}) Reason None\n"
                )
    else:
        GBANNED_LIST = "no Gbanned Users (yet)"
    await edit_or_reply(event, GBANNED_LIST)


@lionub.lion_cmd(
    pattern="gmute(?:\s|$)([\s\S]*)",
    command=("gmute", plugin_category),
    info={
        "header": "To mute a person in all groups where you are admin.",
        "description": "It doesnt change user permissions but will delete all messages sent by him in the groups where you are admin including in private messages.",
        "usage": "{tr}gmute username/reply> <reason (optional)>",
    },
)
async def startgmute(event):
    "To mute a person in all groups where you are admin."
    if event.is_private:
        await event.edit("`Unexpected issues or ugly errors may occur!`")
        await asyncio.sleep(2)
        userid = event.chat_id
        reason = event.pattern_match.group(1)
    else:
        user, reason = await get_user_from_event(event)
        if not user:
            return
        if user.id == lionub.uid:
            return await edit_or_reply(event, "`Sorry, I can't gmute myself`")
        if str(user.id) in DEVLIST:
            return await edit_delete(event, "**Sorry I'm not going to gmute them..**")

        userid = user.id
    try:
        user = (await event.client(GetFullUserRequest(userid))).user
    except Exception:
        return await edit_or_reply(event, "`Sorry. I am unable to fetch the user`")
    if is_muted(userid, "gmute"):
        return await edit_or_reply(
            event,
            f"{_format.mentionuser(user.first_name ,user.id)} ` is already gmuted`",
        )
    try:
        mute(userid, "gmute")
    except Exception as e:
        await edit_or_reply(event, f"**Error**\n`{e}`")
    else:
        if reason:
            await edit_or_reply(
                event,
                f"{_format.mentionuser(user.first_name ,user.id)} `is Successfully gmuted`\n**Reason :** `{reason}`",
            )
        else:
            await edit_or_reply(
                event,
                f"{_format.mentionuser(user.first_name ,user.id)} `is Successfully gmuted`",
            )
    if BOTLOG:
        reply = await event.get_reply_message()
        if reason:
            await event.client.send_message(
                BOTLOG_CHATID,
                "#GMUTE\n"
                f"**User :** {_format.mentionuser(user.first_name ,user.id)} \n"
                f"**Reason :** `{reason}`",
            )
        else:
            await event.client.send_message(
                BOTLOG_CHATID,
                "#GMUTE\n"
                f"**User :** {_format.mentionuser(user.first_name ,user.id)} \n",
            )
        if reply:
            await reply.forward_to(BOTLOG_CHATID)


@lionub.lion_cmd(
    pattern="ungmute(?:\s|$)([\s\S]*)",
    command=("ungmute", plugin_category),
    info={
        "header": "To unmute the person in all groups where you were admin.",
        "description": "This will work only if you mute that person by your gmute command.",
        "usage": "{tr}ungmute <username/reply>",
    },
)
async def endgmute(event):
    "To remove gmute on that person."
    if event.is_private:
        await event.edit("`Unexpected issues or ugly errors may occur!`")
        await asyncio.sleep(2)
        userid = event.chat_id
        reason = event.pattern_match.group(1)
    else:
        user, reason = await get_user_from_event(event)
        if not user:
            return
        if user.id == lionub.uid:
            return await edit_or_reply(event, "`Sorry, I can't gmute myself`")
        userid = user.id
    try:
        user = (await event.client(GetFullUserRequest(userid))).user
    except Exception:
        return await edit_or_reply(event, "`Sorry. I am unable to fetch the user`")
    if not is_muted(userid, "gmute"):
        return await edit_or_reply(
            event, f"{_format.mentionuser(user.first_name ,user.id)} `is not gmuted`"
        )
    try:
        unmute(userid, "gmute")
    except Exception as e:
        await edit_or_reply(event, f"**Error**\n`{e}`")
    else:
        if reason:
            await edit_or_reply(
                event,
                f"{_format.mentionuser(user.first_name ,user.id)} `is Successfully ungmuted`\n**Reason :** `{reason}`",
            )
        else:
            await edit_or_reply(
                event,
                f"{_format.mentionuser(user.first_name ,user.id)} `is Successfully ungmuted`",
            )
    if BOTLOG:
        if reason:
            await event.client.send_message(
                BOTLOG_CHATID,
                "#UNGMUTE\n"
                f"**User :** {_format.mentionuser(user.first_name ,user.id)} \n"
                f"**Reason :** `{reason}`",
            )
        else:
            await event.client.send_message(
                BOTLOG_CHATID,
                "#UNGMUTE\n"
                f"**User :** {_format.mentionuser(user.first_name ,user.id)} \n",
            )


@lionub.lion_cmd(incoming=True)
async def watcher(event):
    if is_muted(event.sender_id, "gmute"):
        await event.delete()


@lionub.lion_cmd(
    pattern="gkick(?:\s|$)([\s\S]*)",
    command=("gkick", plugin_category),
    info={
        "header": "kicks the person in all groups where you are admin.",
        "usage": "{tr}gkick <username/reply/userid> <reason (optional)>",
    },
)
async def liongkick(event):  # sourcery no-metrics
    "kicks the person in all groups where you are admin"
    lionz = await edit_or_reply(event, "`gkicking.......`")
    start = datetime.now()
    user, reason = await get_user_from_event(event, lionz)
    if not user:
        return
    if user.id == lionub.uid:
        return await edit_delete(lionz, "`why would I kick myself`")
    if str(user.id) in DEVLIST:
        return await edit_delete(lionz, "**😒 I'm not going to gkick my developer!!**")

    san = await admin_groups(event.client)
    count = 0
    madboy = len(san)
    if madboy == 0:
        return await edit_delete(lionz, "`you are not admin of atleast one group` ")
    await lionz.edit(
        f"`initiating gkick of the `[user](tg://user?id={user.id}) `in {len(san)} groups`"
    )
    for i in range(madboy):
        try:
            await event.client.kick_participant(san[i], user.id)
            await asyncio.sleep(0.5)
            count += 1
        except BadRequestError:
            achat = await event.client.get_entity(san[i])
            await event.client.send_message(
                BOTLOG_CHATID,
                f"`You don't have required permission in :`\n**Chat :** {get_display_name(achat)}(`{achat.id}`)\n`For kicking there`",
            )
    end = datetime.now()
    liontaken = (end - start).seconds
    if reason:
        await lionz.edit(
            f"[{user.first_name}](tg://user?id={user.id}) `was gkicked in {count} groups in {liontaken} seconds`!!\n**Reason :** `{reason}`"
        )
    else:
        await lionz.edit(
            f"[{user.first_name}](tg://user?id={user.id}) `was gkicked in {count} groups in {liontaken} seconds`!!"
        )

    if BOTLOG and count != 0:
        reply = await event.get_reply_message()
        if reason:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"#GKICK\
                \nGlobal Kick\
                \n**User : **[{user.first_name}](tg://user?id={user.id})\
                \n**ID : **`{user.id}`\
                \n**Reason :** `{reason}`\
                \n__Kicked in {count} groups__\
                \n**Time taken : **`{liontaken} seconds`",
            )
        else:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"#GKICK\
                \nGlobal Kick\
                \n**User : **[{user.first_name}](tg://user?id={user.id})\
                \n**ID : **`{user.id}`\
                \n__Kicked in {count} groups__\
                \n**Time taken : **`{liontaken} seconds`",
            )
        if reply:
            await reply.forward_to(BOTLOG_CHATID)


async def get_full_user(event):
    args = event.pattern_match.group(1).split(":", 1)
    extra = None
    if event.reply_to_msg_id and not len(args) == 2:
        previous_message = await event.get_reply_message()
        user_obj = await event.client.get_entity(previous_message.sender_id)
        extra = event.pattern_match.group(1)
    elif len(args[0]) > 0:
        user = args[0]
        if len(args) == 2:
            extra = args[1]
        if user.isnumeric():
            user = int(user)
        if not user:
            await event.edit("`Itz not possible without an user ID`")
            return
        if event.message.entities is not None:
            probable_user_mention_entity = event.message.entities[0]
            if isinstance(probable_user_mention_entity, MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                user_obj = await event.client.get_entity(user_id)
                return user_obj
        try:
            user_obj = await event.client.get_entity(user)
        except Exception as err:
            return await event.edit("Error... Please report at @LionxSupport", str(err))
    return user_obj, extra


global hehe, lala
hehe = "admin"
lala = "owner"


async def get_user_from_id(user, event):
    if isinstance(user, str):
        user = int(user)
    try:
        user_obj = await event.client.get_entity(user)
    except (TypeError, ValueError) as err:
        await event.edit(str(err))
        return None
    return user_obj


@lionub.lion_cmd(
    pattern="gpromote ?(.*)",
    command=("gpromote", plugin_category),
    info={
        "header": "To promote an user in every group where you are admin.",
        "description": "Will promote the person in every group where you are admin only.",
        "usage": "{tr}gpromote <username/reply/userid> <reason (optional)>",
    },
)
async def gben(userbot):
    dc = lion = userbot
    i = 0
    await dc.get_sender()
    me = await userbot.client.get_me()
    await lion.edit("`promoting...`")
    my_mention = "[{}](tg://user?id={})".format(me.first_name, me.id)
    f"@{me.username}" if me.username else my_mention
    await userbot.get_chat()
    if userbot.is_private:
        user = userbot.chat
        rank = userbot.pattern_match.group(1)
    else:
        userbot.chat.title
    try:
        user, rank = await get_full_user(userbot)
    except:
        pass
    if me == user:
        await lion.edit("khud ko gpromote krega😑😑 chutiya spotted..")
        return
    try:
        if not rank:
            rank = "ㅤㅤ"
    except:
        return await lion.edit(f"**kuch to gadbad hai😑😑**")
    if user:
        telchanel = [
            d.entity.id
            for d in await userbot.client.get_dialogs()
            if (d.is_group or d.is_channel)
        ]
        rgt = ChatAdminRights(
            add_admins=False,
            invite_users=True,
            change_info=False,
            ban_users=True,
            delete_messages=True,
            pin_messages=True,
            manage_call=True,
        )
        for x in telchanel:
            try:
                await userbot.client(EditAdminRequest(x, user, rgt, rank))
                i += 1
                await lion.edit(f"**Promoted in Chats **: `{i}`")
            except:
                pass
    else:
        await lion.edit(f"**kisi ko reply kr lavde🙄!!**")
    return await lion.edit(
        f"**Globally promoted [{user.first_name}](tg://user?id={user.id})\n On Chats🙄 : {i} **"
    )


@lionub.lion_cmd(
    pattern="gdemote ?(.*)",
    command=("gdemote", plugin_category),
    info={
        "header": "To demote user in every group where you are admin.",
        "description": "Will demote the person in every group where you are admin only.",
        "usage": "{tr}gdemote <username/reply/userid> <reason (optional)>",
    },
)
async def gben(userbot):
    dc = lion = userbot
    i = 0
    await dc.get_sender()
    me = await userbot.client.get_me()
    await lion.edit("`demoting...`")
    my_mention = "[{}](tg://user?id={})".format(me.first_name, me.id)
    f"@{me.username}" if me.username else my_mention
    await userbot.get_chat()
    if userbot.is_private:
        user = userbot.chat
        rank = userbot.pattern_match.group(1)
    else:
        userbot.chat.title
    try:
        user, rank = await get_full_user(userbot)
    except:
        pass
    if me == user:
        await lion.edit("khud ko gdemote karega😑😑 chumtiya spotted..")
        return
    try:
        if not rank:
            rank = "ㅤㅤ"
    except:
        return await lion.edit(f"**Phir se kuch gadbad kiya😑**")
    if user:
        telchanel = [
            d.entity.id
            for d in await userbot.client.get_dialogs()
            if (d.is_group or d.is_channel)
        ]
        rgt = ChatAdminRights(
            add_admins=None,
            invite_users=None,
            change_info=None,
            ban_users=None,
            delete_messages=None,
            pin_messages=None,
            manage_call=None,
        )
        for x in telchanel:
            try:
                await userbot.client(EditAdminRequest(x, user, rgt, rank))
                i += 1
                await lion.edit(f"**Demoted in Chats **: `{i}`")
            except:
                pass
    else:
        await lion.edit(f"**Reply to a user you dumbo !!**")
    return await lion.edit(
        f"**Globally Demoted this lavda On [{user.first_name}](tg://user?id={user.id})\n Chats😏 : {i} **"
    )


@lionub.lion_cmd(
    pattern="gcast ?(.*)",
    command=("gcast", plugin_category),
    info={
        "header": "global groups cast.",
        "description": "Use this command to global broadcast a message in all groups.",
        "usage": "{tr}gcast",
    },
)
async def gcast(event):
    if not event.out and not is_fullsudo(event.sender_id):
        return await edit_or_reply(event, "`This Command Is Sudo Restricted.`")
    xx = event.pattern_match.group(1)
    if not xx:
        return edit_or_reply(event, "`Give some text to Globally Broadcast`")
    tt = event.text
    msg = tt[6:]
    lion = await edit_or_reply(event, "`Globally Broadcasting Msg...`")
    er = 0
    done = 0
    async for x in bot.iter_dialogs():
        if x.is_group:
            chat = x.id
            try:
                done += 1
                await bot.send_message(chat, msg)
            except BaseException:
                er += 1
    await lion.edit(f"Done in {done} chats, error in {er} chat(s)")


@lionub.lion_cmd(
    pattern="gucast ?(.*)",
    command=("gucast", plugin_category),
    info={
        "header": "global users cast.",
        "description": "Use this command to broadcast global message to all users only.",
        "usage": "{tr}gucast",
    },
)
async def gucast(event):
    if not event.out and not is_fullsudo(event.sender_id):
        return await edit_or_reply(event, "`This Command Is Sudo Restricted.`")
    xx = event.pattern_match.group(1)
    if not xx:
        return edit_or_reply(event, "`Give some text to Globally Broadcast`")
    tt = event.text
    msg = tt[7:]
    lion = await edit_or_reply(event, "`Globally Broadcasting Msg...`")
    er = 0
    done = 0
    async for x in bot.iter_dialogs():
        if x.is_user and not x.entity.bot:
            chat = x.id
            try:
                done += 1
                await bot.send_message(chat, msg)
            except BaseException:
                er += 1
    await lion.edit(f"Done in {done} chats, error in {er} chat(s)")
