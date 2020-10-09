import asyncio
from telethon import events
from userbot.utils import admin_cmd
from userbot import ALIVE_NAME
from telethon.tl.types import ChannelParticipantsAdmins
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Hell User"
PM_IMG = "https://telegra.ph/file/4b370450811f0cb8a23ac.jpg"
pm_caption = "🔱 **GANGSTER Is Online** 🔱\n\n"

pm_caption += f"🔸🔹 **MY GOD**           :   {DEFAULTUSER}\n"

pm_caption += "🔹🔸 тєℓєтнσи νєяѕισи   :   1.15.0 \n"

pm_caption += "🔸🔹 σffι¢ιαℓ ¢нαииєℓ   :   [ᴊᴏɪɴ](https://www.pornhub.org/desi)\n"

pm_caption += "🔹🔸 σffι¢ιαℓ gяσυρ     :   [ᴊᴏɪɴ](https://www.pornhub.org/videsi)\n"


pm_caption += "🔹🔸 ¢σρуяιgнт          :   [GANGSTERBOT-OWNER](https://t.me/ALONGANGSTER)\n"

pm_caption += " [...▄███▄███▄\n....█████████\n.......▀█████▀\n............▀█▀\n](https://t.me/ALONGANGSTER)\n"
#@command(outgoing=True, pattern="^.alive$")
@borg.on(admin_cmd(pattern=r"alive"))
async def amireallyalive(alive):
    chat = await alive.get_chat()
    await alive.delete()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)
    await alive.delete() 
