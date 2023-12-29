import texts
from keyboards import *
from functions import *
from aiogram import F,Router
from aiogram.filters import CommandStart
from aiogram.types import CallbackQuery
from aiogram.types import Message

router = Router()

@router.message(CommandStart())
async def start(message: Message):
    await message.answer(f'✅ Добро пожаловать, @{message.from_user.username}!\n\n' + texts.start, reply_markup = start_kb)

@router.message(F.text =='ℹ️ О нас')
async def about(message: Message):
    await message.answer_photo(img_answer('files/about.jpg'), texts.about_us, parse_mode = 'HTML', reply_markup = start_kb)

@router.message(F.text =='📝 Прейскурант')
async def price(message):
    await message.answer_photo(img_answer('files/info.jpg'),'<b>Выберите интересующую вас услугу</b>', parse_mode = 'HTML', reply_markup = catalog_kb)

@router.callback_query(F.data=='Маникюр')
async def manikur(callback:CallbackQuery):
    await callback.message.edit_media(img('files/manikur.jpg',texts.manikur), reply_markup = buy_kb)
    await callback.answer()

@router.callback_query(F.data=='Педикюр')
async def pedikur(callback:CallbackQuery):
    await callback.message.edit_media(img('files/pedikur.jpg',texts.pedikur),parse_mode='HTML',reply_markup=buy_kb)
    await callback.answer()

@router.callback_query(F.data=='Наращивание')
async def pedikur(callback:CallbackQuery):
    await callback.message.edit_media(img('files/narast.png',texts.narast),parse_mode='HTML',reply_markup=buy_kb)
    await callback.answer()

@router.callback_query(F.data=='Другое')
async def pedikur(callback:CallbackQuery):
    await callback.message.edit_media(img('files/other.png',texts.other),parse_mode='HTML',reply_markup=buy_kb)
    await callback.answer()

@router.callback_query(F.data=='back_to_preiskurant')
async def back(callback:CallbackQuery):
    await callback.message.edit_media(img('files/info.jpg','<b>Выберите интересующую вас услугу</b>'), reply_markup = catalog_kb)
    await callback.answer()