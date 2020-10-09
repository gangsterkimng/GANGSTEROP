from telethon import events
import random, re
from userbot.utils import admin_cmd
import asyncio 



@borg.on(admin_cmd("gangasta ?(.*)"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("**EVERYONE**")
        await asyncio.sleep(2)
        await event.edit("**is*")
        await asyncio.sleep(2)
        await event.edit("**Gangster**")
        await asyncio.sleep(2)
        await event.edit("**UNTILL**")
        await asyncio.sleep(2)
        await event.edit("**@ALONGANGSTER**")
        await asyncio.sleep(2)
        await event.edit("**ARRIVE**")
        await asyncio.sleep(2)
        await event.edit("**🔥REMEMBER🔥**")
        await asyncio.sleep(2)
        await event.edit("**EVERYBODY IS GANGSTER UNTILL @ALONGANGSTER ARRIVE 🔥🔥🔥")
