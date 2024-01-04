import texts.category
from keyboards import *
from functions import *
from aiogram import F,Router
from aiogram.types import CallbackQuery

router = Router()

@router.message(F.text =='📝 Прейскурант')
async def price(message):
    await message.answer_photo(img_answer('files/info.jpg'), '<b>Выберите интересующую вас услугу</b>', parse_mode ='HTML', reply_markup = catalog_kb)

@router.callback_query(F.data=='Маникюр')
async def manikur(callback:CallbackQuery):
    await callback.message.edit_media(img('files/manikur.jpg', texts.category.manikur), reply_markup = buy_kb)
    await callback.answer()

@router.callback_query(F.data=='Педикюр')
async def pedikur(callback:CallbackQuery):
    await callback.message.edit_media(img('files/pedikur.jpg', texts.category.pedikur), parse_mode='HTML', reply_markup=buy_kb)
    await callback.answer()

@router.callback_query(F.data=='Наращивание')
async def narast(callback:CallbackQuery):
    await callback.message.edit_media(img('files/narast.png', texts.category.narast), parse_mode='HTML', reply_markup=buy_kb)
    await callback.answer()

@router.callback_query(F.data=='Другое')
async def other(callback:CallbackQuery):
    await callback.message.edit_media(img('files/other.png', texts.category.other), parse_mode='HTML', reply_markup=buy_kb)
    await callback.answer()

@router.callback_query(F.data=='back_to_preiskurant')
async def back(callback:CallbackQuery):
    await callback.message.edit_media(img('files/info.jpg', '<b>Выберите интересующую вас услугу</b>'), reply_markup = catalog_kb)
    await callback.answer()