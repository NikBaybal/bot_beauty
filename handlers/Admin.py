from aiogram import F,Router
from aiogram.types import Message
from aiogram.filters import Command, StateFilter
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state, State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import ReplyKeyboardRemove

from keyboards import *
import texts.admin
import database


from config import Config, load_config
router = Router()
config: Config = load_config()


@router.message(Command(commands='admin'))
async def start(message:Message):
    if message.from_user.id in config.tg_bot.admin_ids:
        await message.answer(texts.admin.start_admin, parse_mode="HTML", reply_markup=admin_kb)

@router.callback_query(F.data=='statistick')
async def stat(callback:CallbackQuery):
    await callback.message.edit_text(texts.admin.statistick(int(database.count())), parse_mode="HTML", reply_markup=back_to_admin_kb)
    await callback.answer()


@router.callback_query(F.data == 'users')
async def users(callback:CallbackQuery):
    from main import bot
    t = '''ID, UserName, Name
    ➖➖➖➖➖➖➖➖➖'''
    num = 0
    flag = False
    await callback.message.delete()
    await callback.answer()
    for id in database.get_all()[:][0]:
        user = await bot.get_chat(id)
        un = user.username
        if not un:
            database.delete(id)
            continue
        fn = user.first_name
        num += 1
        if len(t) > 3900:
            if not flag:
                await callback.message.edit_text(t, parse_mode="HTML")
                flag = True
            else:
                await callback.message.answer(t, parse_mode="HTML")
            t = ''
        t += f'\n{num}. <code>{id}</code> @{un} <b>{fn}</b>'
    await callback.message.answer(t, parse_mode="HTML", reply_markup=back_to_admin_kb)
@router.callback_query(F.data == 'back_to_admin')
async def back_admin(call: CallbackQuery):
    await call.message.edit_text(texts.admin.start_admin, parse_mode="HTML", reply_markup=admin_kb)
    await call.answer()

class FSMAdmins(StatesGroup):
    ban = State()
    mailing_step1 = State()
    mailing_step2 = State()

@router.callback_query(F.data == 'mailing')
async def mailing(call: CallbackQuery):
    instructions = "Введите текст сообщения:"
    await call.message.answer(instructions)
    await call.answer()
    await FSMAdmins.mailing_step1.set_state()