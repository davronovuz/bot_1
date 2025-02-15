from aiogram import types
from loader import dp,bot
from utils.quizziz import savollar



joriy_index={}



def send_question(chat_id):
    index=joriy_index.get(chat_id)


@dp.message_handler(commands="test")
async def test_handler(message:types.Message):
    index=joriy_index[message.chat.id]=0

    if index<len(savollar):
        pass
    else:
        await message.answer("savollar tugadi raxmat !!!")









