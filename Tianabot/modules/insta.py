from datetime import datetime

from telethon.errors.rpcerrorlist import YouBlockedUserError

from MerissaRobot import telethn as tbot
from MerissaRobot import ubot
from MerissaRobot.events import register


@register(pattern="^/insta ?(.*)")
async def insta(event):
    chat = "@instasavegrambot"
    link = event.pattern_match.group(1)
    xx = await event.reply("`Finding Video...`")
    if event.fwd_from:
        return
    if "instagram.com" not in link:
        await xx.edit("` I need a Instagram link to download it's Video...`(*_*)")
    else:
        start = datetime.now()
        catevent = await xx.edit("```Downloading Video...```")
    async with ubot.conversation(chat) as conv:
        try:
            msg_start = await conv.send_message("/start")
            r_start = await conv.get_response()
            msg = await conv.send_message(link)
            response = await conv.get_response()
            video = await conv.get_response()
            details = await conv.get_response()
            await ubot.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await catevent.edit(
                "**Error:** Contact @MerissaxSupport For InstaGram Download.`"
            )
            return
        await catevent.delete()
        cat = await tbot.send_file(
            event.chat.id,
            caption="Powered by @MerissaRobot",
            file=video,
        )
        end = datetime.now()
        ms = (end - start).seconds
        await cat.edit(
            f"<b><i>➥ Video uploaded in {ms} seconds.</i></b>\n<b><i>➥ Uploaded by :- {hmention}</i></b>",
            parse_mode="html",
        )
    await ubot.delete_messages(
        conv.chat_id,
        [msg_start.id, r_start.id, msg.id, response.id, video.id, details.id],
    )
