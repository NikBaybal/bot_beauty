import texts
from keyboards import *
from functions import *
from aiogram import F,Router
from aiogram.filters import CommandStart
from aiogram.types import Message
import database

router = Router()

@router.message(CommandStart())
async def start(message: Message):
    database.add(message.from_user.id)
    await message.answer(f'✅ Добро пожаловать, @{message.from_user.username}!\n\n' + texts.start, reply_markup = start_kb)

@router.message(F.text =='ℹ️ О нас')
async def about(message: Message):
    await message.answer_photo(img_answer('files/about.jpg'), texts.start.about_us, parse_mode ='HTML', reply_markup = start_kb)

@router.message(F.text =='ℹ️ О нас')
async def ban_message(update):
    await update.answer(texts.admin.ban, parse_mode='HTML')

@router.message(F.text =='ℹ️ О нас')
async def ban_callbackquery(update):
    await update.message.answer(texts.admin.ban, parse_mode='HTML')
    await update.answer()