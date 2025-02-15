from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.inline.menu import menu_courses
from loader import dp

from keyboards.default.menu import menu_start


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer("Assalomu alaykum xush kelibsiz",reply_markup=menu_start)


@dp.message_handler(content_types=types.ContentType.VIDEO)
async def message_vodieo(message:types.Message):
    file_id=message.video.file_id
    await message.answer(file_id)



@dp.message_handler(text="Python darslari")
async def message_python(message:types.Message):
    url="BAACAgIAAxkBAAPXZ633uzjKQLNvBiK1Acu2f7lxXZIAAqclAALA5wFJcZ-ugY1BHNY2BA"
    await message.answer_video(url)


@dp.message_handler(text="Java  darslari")
async def message_python(message:types.Message):
    url="BAACAgIAAxkBAAPeZ634ppIGT-2mbTZJvAi2FtN7DZoAAntjAAIazGBJGDUEgKIv6y42BA"
    await message.answer_video(url)