from aiogram import F,Router
from aiogram.types import Message,CallbackQuery,PhotoSize
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import ReplyKeyboardRemove
from functions import *
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


class FSMAdmins(StatesGroup):
    ban = State()
    mailing_step1 = State()
    mailing_step2 = State()
@router.message(Command(commands='cancel'))
async def process_cancel_command_state(message: Message, state: FSMContext):
    await message.answer(
        text='Вы вышли из машины состояний\n\n'
             'Чтобы снова перейти к заполнению  - '
             'отправьте команду /admin'
    )
    # Сбрасываем состояние и очищаем данные, полученные внутри состояний
    await state.clear()
@router.callback_query(F.data == 'mailing')
async def mailing(call: CallbackQuery,state: FSMContext):
    instructions = "Введите текст сообщения:"
    await call.message.answer(instructions)
    await call.answer()
    await state.set_state(FSMAdmins.mailing_step1)

@router.message(StateFilter(FSMAdmins.mailing_step1),F.text.isalpha())
async def mailing1(message, state):
    await state.update_data(text=message.text)
    instructions = "Прикрепите фотографию к сообщению:"
    await message.answer(text=instructions)
    await state.set_state(FSMAdmins.mailing_step2)

@router.message(StateFilter(FSMAdmins.mailing_step1))
async def warning_not_text(message: Message):
    await message.answer(
        text='Пожалуйста, введите текст\n\n'
             'Если вы хотите прервать заполнение - '
             'отправьте команду /cancel'
    )


@router.message(StateFilter(FSMAdmins.mailing_step2),F.photo)
async def process_photo_sent(message: Message,
                             state: FSMContext):
    from main import bot
    await message.bot.download(file=message.photo[-1].file_id, destination='files/photo.jpg')
    data = await state.get_data()
    subscribers = database.get_id()
    c = 0
    for user_id in subscribers[:][0]:
        try:
            await bot.send_photo(user_id, img_answer('files/photo.jpg'), caption=str(data['text']))
            c += 1
        except Exception as e:
            print(e)

    await message.answer(f'Рассылка успешно завершена: {c} / {database.count()}', reply_markup=admin_kb)
    await state.clear()
@router.message(StateFilter(FSMAdmins.mailing_step2))
async def warning_not_photo(message: Message):
    await message.answer(
        text='Пожалуйста, на этом шаге отправьте '
             'фото\n\nЕсли вы хотите прервать '
             'заполнение анкеты - отправьте команду /cancel'
    )

@router.callback_query(F.data == 'block')
async def block(call: CallbackQuery,state: FSMContext):
    await call.message.answer(texts.admin.ban_from_admin_start, parse_mode="HTML",
                              reply_markup=ReplyKeyboardRemove())
    await call.answer()
    await state.set_state(FSMAdmins.ban)

@router.message(StateFilter(FSMAdmins.ban))
async def ban1(message, state):
    from main import bot
    text = message.text
    if text == '/cancel':
        await message.answer(texts.admin.ban_from_admin_cancel, reply_markup=admin_kb)
        await state.finish()
        return
    if text.isdigit():
        id = int(text)
        try:
            await bot.send_message(id, texts.admin.ban)
        except Exception as e:
            print(e)
        database.block(id)
        await message.answer(texts.admin.ban_from_admin_finaly, parse_mode='HTML', reply_markup=admin_kb)
        await state.finish()
    else:
        await message.answer(texts.admin.ban_from_admin_except, parse_mode='HTML')

@router.callback_query(F.data == 'back_to_admin')
async def back_admin(call: CallbackQuery):
    await call.message.edit_text(texts.admin.start_admin, parse_mode="HTML", reply_markup=admin_kb)
    await call.answer()
