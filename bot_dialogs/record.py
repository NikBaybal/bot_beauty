from typing import Any, Dict
from aiogram_dialog import (Dialog, Window, DialogManager)
from aiogram_dialog.widgets.kbd import Next, Row, Back, Checkbox, Radio
from aiogram_dialog.widgets.text import Const, Format, Case
from . import states
from .main import MAIN_MENU_BUTTON
from aiogram_dialog.widgets.input import TextInput, ManagedTextInput
import datetime
from aiogram.types import Message

def date_check(text: str) -> str:
    if datetime.date.fromisoformat(text):
        return text
    raise ValueError("Incorrect data format, should be YYYY-MM-DD")

async def correct_date_handler(
        message: Message,
        widget: ManagedTextInput,
        dialog_manager: DialogManager,
        text:str):
    dialog_manager.dialog_data['user_input'] = text
    await dialog_manager.next()

async def error_date_handler(
        message: Message,
        widget: ManagedTextInput,
        dialog_manager: DialogManager,
        text: str):
    await message.answer(
        text='Вы ввели некорректную дату. Попробуйте еще раз'
    )

main_window = Window(
    Const("Введите желаемую дату в формате YYYY-MM-DD:"),
    MAIN_MENU_BUTTON,
    TextInput(
        id='date_input',
        type_factory=date_check,
        on_success=correct_date_handler,
        on_error=error_date_handler,
    ),
    state=states.Record.MAIN,
)


async def data_getter(**_kwargs):
    return {
         "something": "data from Window1 getter",
    }


hour_window = Window(
    Format("Выбранная дата:  {dialog_data[user_input]}"),
    Back(),
    MAIN_MENU_BUTTON,
    state=states.Record.Hour,
    getter=data_getter,
)

record_dialog = Dialog(
    main_window,
    hour_window,

)