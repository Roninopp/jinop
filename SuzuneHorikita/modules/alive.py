import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from SuzuneHorikita.events import register
from SuzuneHorikita import telethn as tbot


PHOTO = "https://telegra.ph/file/6001b9d2ba6d3c183b979.mp4"

@register(pattern=("/alive"))
async def awake(event):
  TEXT = f"**Hi [{event.sender.first_name}](tg://user?id={event.sender.id}), I'm SuzuneHorikita** \n\n"
  TEXT += "βͺ **I'm Working Properly** \n\n"
  TEXT += f"βͺ **My Master : [π©πα΄πsππͺβ’](https://t.me/TheVenomXD)** \n\n"
  TEXT += f"βͺ **Library Version :** `{telever}` \n\n"
  TEXT += f"βͺ **Telethon Version :** `{tlhver}` \n\n"
  TEXT += f"βͺ **Pyrogram Version :** `{pyrover}` \n\n"
  TEXT += "**Thanks For Adding Me HereοΈ**"
  BUTTON = [[Button.url("Help", "https://t.me/Suzune_Superbot?start=help"), Button.url("Support", "https://t.me/Suzune_Support")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=TEXT,  buttons=BUTTON)
