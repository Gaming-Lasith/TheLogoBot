""" 
MIT License

Copyright (c) 2022 Gaming Lasith

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import os
from pyrogram import filters, idle
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto
from requests import get
import datetime
import pytz
from stdlogo import stdlogo
from stdlogo.plugins import *
from stdlogo import LOGGER
from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
import random
import requests
import shutil
import config
from stdlogo.utils import HELPTEXT, HELPBTNS

BOTNAME = config.BOT_NAME

STARTTEXT = f""" Hello 👋
I am {BOTNAME}
I can create simple logos for you.
Click "About" and "Help And Command" to know more. 
[ԌΛϺェƝԌ ㄥΛکェтℋ](https://t.me/ItsMeLasith) All Right Received©
"""

STARTBTNS = InlineKeyboardMarkup(
            [       
                [
                    InlineKeyboardButton("UPDATES", url="https://t.me/ItsMeLasith"),
                    InlineKeyboardButton("SUPPORT", url="https://t.me/Lasith_SupportChat") 
                ],
                [
                    InlineKeyboardButton("About bot", callback_data="aboutmenu")
                ], 
                [
                    InlineKeyboardButton("☘️Help And Commands☘️", callback_data="helpmenu")
                ],
                [ 
                    InlineKeyboardButton("Developer", url="https://t.me/GamingLasith")           
                ]
            ]
        )

START_IMG = "https://telegra.ph/file/e0a135d44f34933616069.jpg

@lasith.on_message(filters.private & filters.incoming & filters.command(["start"]))
async def startmsg(_, message):
  await message.reply_photo(photo=START_IMG, 
    caption=STARTTEXT,
    reply_markup=STARTBTNS
  )

@lasith.on_message(filters.private & filters.incoming & filters.command(["help"]))
async def startmsg(_, message):
  await message.reply_photo(photo=START_IMG, 
    caption=HELPTEXT,
    reply_markup=HELPBTNS
  )
lasith.start()
LOGGER.info("'Amazing Logo Bot is online!")
idle()
