"""Emoji

Available Commands:

.emoji shrug

.emoji apple

.emoji :/

.emoji -_-"""

from telethon import events

import asyncio
from userbot.utils import admin_cmd




@borg.on(admin_cmd(pattern=r"call"))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 3

    animation_ttl = range(0, 18)

   # input_str = event.pattern_match.group(1)

   # if input_str == "call":

    await event.edit("Calling")

    animation_chars = [
        
            "`Connecting To Telegram Headquarterssss...`",
            "`Call Connected.`",
            "`Telegram: Hello This is Telegram HQ. Who is this?`",
            "`Me: Yo this is` [THUG](t.me/GANGSTERSUPPORT) ,`Please Connect me to my master,GANGSTER`",
            "`User Authorised.`",
            "`Calling`  `At +916969696969`",
            "`Private  Call Connected...`",
            "`Me: SIR, Please Ban This Telegram Account.`",    
            "`GANGSTER: May I Know Who Is This?`",
            "`Me: Yo Brah, itz me THUG HERE`  ",
            "`GANGSTER: OH YEAH I remember you ya ...\nI'll Make Sure That Guy Account Will Get Blocked Within 24Hrs.`",
            "`Me: Thanks, See You Later Brah.`",
            "`GANGSTER: NO PROBLEM , Telegram Is Our's. Just Gimme A Call if you need any help ;).`",
            "`Me: Sure Sur \nTC Bye Bye :)`",
            "`Private Call Disconnected`"
        ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 18])
