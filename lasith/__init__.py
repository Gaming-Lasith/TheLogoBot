import aiohttp
import logging
from pyrogram import Client
import config

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

LOGGER = logging.getLogger(__name__)

stdlogo = Client("stdlogobot", bot_token=config.BOT_TOKEN, api_hash=config.API_HASH, api_id=config.API_ID,)
