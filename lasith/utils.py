
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
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ForceReply
import config

BOTNAME=config.BOT_NAME
BOTUNAME=config.BOT_USERNAME

STARTTEXT = f""" Hello👋
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

HELPTEXT = """ Hello !
I have some commands.
Try bellow buttons to 
know about them👇. """

HELPBTNS = InlineKeyboardMarkup(
           [
             [
               InlineKeyboardButton("Logo Commands", callback_data="logomenu")
             ],
             [
               InlineKeyboardButton("Bot Commands", callback_data="botmenu")
             ],
             [
               InlineKeyboardButton("🔙Back", callback_data="startmenu")
             ],
           ]
       ) 

ABOUTTEXT = """⚡This logo bot is mainly powered with pyrogram & pillow.
Credits 💳
This bot is made with the help of many peoples,
So credit of this bot should be go to them
•szsupunma
•Single developers API
•Noob|Dev
•ItsMeSithija|Dev """

ABOUTBTNS = InlineKeyboardMarkup(
           [
             [
               InlineKeyboardButton("Source Code📦", url="https://github.com/Gaming-Lasith/TheLogoBot")
             ],
             [
               InlineKeyboardButton("🔙Back", callback_data="helpmenu")
             ],
           ]
       ) 

LOGOTEXT = """෴Logo Commands෴
This is my logo making commands🔥
Try them and Get a fun.
•/logo {text} - random logo make.
•/write {text} - write something.
•/mlogo {text} - mask logo.
More logos update in soon. """

LOGOBTNS = InlineKeyboardMarkup(
           [[
               InlineKeyboardButton("🔙Back", callback_data="helpmenu")
           ]]
         )

BOTTEXT = """ ෴Bot commands෴
•/start - Start bot.
•/help - Get Help.
 """

BOTBTNS = InlineKeyboardMarkup(
           [[
               InlineKeyboardButton("🔙Back", callback_data="helpmenu")
           ]]
         )

LOGOSTD = """
☘️** Logo Created Successfully**✅
〢─────────────〣
🔥 **Created by** :
[{BOTNAME}](http://t.me/{BOTUNAME})
⚡️ **Powered By **  :
[Gaming Lasith](http://t.me/ItsMeLasith)
〣─────────────〢
"""

LOGOSTDBTNS = InlineKeyboardMarkup(
      [
        [
        InlineKeyboardButton(text="Developer", url=f"http://t.me/GamingLasith") 
        ],
        [
         InlineKeyboardButton(text="🤩Share Our Bot🤩", url=f"tg://msg_url?url=I%20found%20a%20super%20logo%20bot%20use%20now%20@AmazingLogosBot%20%F0%9F%A4%A9") 
        ]
      ]      
  )

