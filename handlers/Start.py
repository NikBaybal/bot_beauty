import texts.admin
import texts.start
from keyboards import *
from functions import *
from aiogram import F,Router
from aiogram.filters import CommandStart, StateFilter
from aiogram.types import Message
import database
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

router = Router()

@router.message(CommandStart())
async def start(message: Message):
    database.add_user(message.from_user.id,message.from_user.username,message.from_user.first_name)
    await message.answer(f'✅ Добро пожаловать, @{message.from_user.username}!\n\n' + texts.start.start, reply_markup = start_kb)

@router.message(F.text =='ℹ️ О нас')
async def about(message: Message):
    await message.answer_photo(img_answer('files/about.jpg'), texts.start.about_us, parse_mode ='HTML', reply_markup = start_kb)
class FSMRecord(StatesGroup):
    day = State()
@router.message(F.text =='Запись')
async def start_record(message: Message,state:FSMContext):
    await message.answer('Введите пожалуйста дату записи в формате: 01.01.2024', parse_mode ='HTML')
    await state.set_state(FSMRecord.day)

@router.message(StateFilter(FSMRecord.day))
async def hours(message, state):
    date = str(message.text)
    await message.answer(text='Выберите пожалуйста часы:',parse_mode ='HTML', reply_markup = free_hours_kb(date))
    await state.finish()
