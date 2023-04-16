import asyncio
from pyrogram import Client
from pyrogram.enums import ChatType
import re


api_id = # get this from https://my.telegram.org/apps
api_hash =  # get this from https://my.telegram.org/apps

thanks = r'спасиб[оа]?|пасиб|спс'

app = Client('my_account', api_id, api_hash)

@app.on_message()
async def auto_answer(client, message):
    if message.chat.type is ChatType.PRIVATE and not message.from_user.is_self and re.findall(thanks, message.text.lower()):
        await client.send_reaction(
            chat_id=message.chat.id,
            message_id=message.id,
            emoji='❤'
        )

app.run()