import asyncio

from telethon import functions
from telethon.errors.rpcerrorlist import (
    ChatAdminRequiredError,
    ChatWriteForbiddenError,
    PeerFloodError,
)

from userbot import lionub

from ..funcs.managers import edit_delete, edit_or_reply

plugin_category = "tools"


@lionub.lion_cmd(
    pattern="invite ([\s\S]*)",
    command=("invite", plugin_category),
    info={
        "header": "Add the given user/users to the group where u used the command.",
        "description": "Adds only mentioned person or bot not all members",
        "usage": "{tr}invite <username(s)/userid(s)>",
        "examples": "{tr}invite @combot @MissRose_bot",
    },
)
async def _(event):
    "To invite a user to chat."
    to_add_users = event.pattern_match.group(1)
    if not event.is_channel and event.is_group:
        # https://lonamiwebs.github.io/Telethon/methods/messages/add_chat_user.html
        for user_id in to_add_users.split(" "):
            try:
                await event.client(
                    functions.messages.AddChatUserRequest(
                        chat_id=event.chat_id, user_id=user_id, fwd_limit=1000000
                    )
                )
            except Exception as e:
                return await edit_delete(event, f"`{str(e)}`", 5)
    else:
        # https://lonamiwebs.github.io/Telethon/methods/channels/invite_to_channel.html
        for user_id in to_add_users.split(" "):
            try:
                await event.client(
                    functions.channels.InviteToChannelRequest(
                        channel=event.chat_id, users=[user_id]
                    )
                )
            except Exception as e:
                return await edit_delete(event, f"`{e}`", 5)

    await edit_or_reply(event, f"`{to_add_users} is/are Invited Successfully`")


async def delete_in(message, time):
    await asyncio.sleep(time)
    return await message.delete()


# X=============Spent Time Anyway=======================X

Scrapping = {}  # Well this will be needed to stop scrapping at a moment.


@lionub.lion_cmd(
    pattern="inviteall (.*)",
    command=("inviteall", "tools"),
    info={
        "header": "To mass add members.",
        "options": "You can mention limit of members to be added.",
        "usage": [
            "{tr}inviteall <chat> <limit>(optional)",
        ],
    },
)
async def scrapper(event):
    """Will try to kidnap a whole bunch of people from a chat to a chat i.e user pollination."""
    if event.is_private:
        message = await event.edit(
            "Man, do you think I can't differentiate between a channel/group and a personal chat?"
        )
        return await delete_in(message, 5)

    try:
        chat = int((event.pattern_match.group(1)).split(" ")[0])
    except ValueError:
        chat = (event.pattern_match.group(1)).split(" ")[0]

    try:
        max = int((event.pattern_match.group(1)).split(" ")[1])
        if max == 0:
            message = await event.edit(
                "Zero members?! If you aren't in mood of adding members then why even using me?"
            )
            return delete_in(message, 5)
    except IndexError:
        max = None
    except ValueError:
        return await event.edit(max + "is wrong value. An integral value is required.")

    try:
        chat = await event.client.get_entity(chat)
    except ValueError:
        message = await event.edit(
            f"I don't think `{chat}` is a correct chat. Or maybe you are banned from it."
        )
        return await delete_in(message, 8)

    if event.chat_id == chat.id or str(event.chat_id) == ("-100" + f"{chat.id}"):
        message = await event.edit(
            "You just simply tried to add members from the same group. Like WTF? I guess you need to be added in a mental hospital."
        )
        return await delete_in(message, 8)

    try:
        await event.edit("Getting list of members...")
        members = (await event.client.get_participants(chat.id)).total
    except ChatAdminRequiredError:
        message = await event.edit(
            "I am really sorry, you don't have sufficient administrative privilages required to do that."
        )
        return await delete_in(message, 5)

    await event.edit("Starting...")
    Scrapping.update({event.chat_id: True})

    # ====================== Constants =====================================
    warn_surpress = False  # Stops a stupid spam that I have created.
    success = 0  # Counts number of successful attempts to add members.
    failed = 0  # Counts number of failed attempts to add members.
    # =====================================================================

    if event.is_group:
        async for user in event.client.iter_participants(
            chat.id, limit=max, aggressive=True
        ):  # This limit thing isn't blowing anything...!
            if max == 0:
                return
            if event.chat_id not in Scrapping:  # Haha, the spell to stop scrapping.
                return

            try:

                await event.client(
                    functions.messages.AddChatUserRequest(
                        chat_id=event.chat_id, user_id=user.id, fwd_limit=int(members)
                    )
                )
                success += 1
                if max:
                    max -= 1
                await event.edit("Brought " + success + " participant(s)")
                asyncio.sleep(1)

            except ChatWriteForbiddenError:
                await event.delete()
                return await event.respond(
                    "You have insufficient rights to invite members here."
                )
            except PeerFloodError:
                if not warn_surpress:
                    warn_surpress = True
                    await event.respond(
                        "**I am really sorry. You have got Flood-Error from Telegram. Maybe you can't add non-mutual contacts. Please contact** @spambot **for more info.**"
                    )
            except Exception:
                failed += 1

    if event.is_channel:
        async for user in event.client.iter_participants(chat.id):
            if max == 0:
                return
            if event.chat_id not in Scrapping:  # Haha, read comment on line 39.
                return

            try:
                await event.client(
                    functions.channels.InviteToChannelRequest(
                        channel=event.chat_id, users=[user.id]
                    )
                )
                success += 1
                if max:
                    max -= 1
                await event.edit("Brought " + success + " participant(s)")
                asyncio.sleep(1)

            except ChatWriteForbiddenError:
                await event.delete()
                return await event.respond(
                    "You have insufficient rights to invite members here."
                )
            except PeerFloodError:
                if not warn_surpress:
                    warn_surpress = True
                    await event.respond(
                        "**I am really sorry. You have got Flood-Error from Telegram. Maybe you can't add non-mutual contacts. Please contact** @spambot **for more info.**"
                    )
            except Exception:
                failed += 1

    await event.delete()
    await event.respond(
        f"**Phew Done**\n__Stats:__\n**Kidnapped** __{success}__ **members. But couldn't kidnap** __{failed}__ **nerds.**"
    )

    try:
        del Scrapping[event.chat_id]
    except KeyError:
        await event.respond(
            "**Wait!! I just got some error. Please restart the bot quickly or reinstall the plugin!!**"
        )


@lionub.lion_cmd(
    pattern="stopinvite",
    command=("stopinvite", "tools"),
    info={
        "header": "To stop kidnapping in the current chat.",
        "usage": [
            "{tr}stopinvite",
        ],
    },
)
async def kill_scrapper(event):
    """If you wanna stop this stupid User Pollination, use this."""
    if event.chat_id not in Scrapping:
        message = await event.edit("I am not kidnapping in this chat at the moment :D")
        return await delete_in(message, 5)
    else:
        try:
            del Scrapping[event.chat_id]
        except KeyError:
            return await event.edit(
                "Got something wrong. Please reinstall the plugin or restart the bot."
            )
        await event.edit("Ok, I will stop this kidnapping here.")
