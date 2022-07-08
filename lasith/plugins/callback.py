import requests
from stdlogo import stdlogo
from pyrogram import filters, idle
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from stdlogo.utils import STARTTEXT, STARTBTNS, HELPTEXT, HELPBTNS, ABOUTTEXT, ABOUTBTNS, LOGOTEXT, LOGOBTNS, BOTTEXT, BOTBTNS

@stdlogo.on_callback_query(filters.regex("startmenu"))
async def startmenu(_, query: CallbackQuery):
    await query.edit_message_text(STARTTEXT,
        reply_markup=STARTBTNS,
     disable_web_page_preview=True
    )

@stdlogo.on_callback_query(filters.regex("helpmenu"))
async def helpmenu(_, query: CallbackQuery):
    await query.edit_message_text(HELPTEXT,
        reply_markup=HELPBTNS,
     disable_web_page_preview=True
    )

@stdlogo.on_callback_query(filters.regex("aboutmenu"))
async def about(_, query: CallbackQuery):
    await query.edit_message_text(ABOUTTEXT,
        reply_markup=ABOUTBTNS,
     disable_web_page_preview=True
    )

@stdlogo.on_callback_query(filters.regex("logomenu"))
async def about(_, query: CallbackQuery):
    await query.edit_message_text(LOGOTEXT,
        reply_markup=LOGOBTNS,
     disable_web_page_preview=True
    )

@stdlogo.on_callback_query(filters.regex("botmenu"))
async def about(_, query: CallbackQuery):
    await query.edit_message_text(BOTTEXT,
        reply_markup=BOTBTNS,
     disable_web_page_preview=True
    )







""" MIT License

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
SOFTWARE. """
