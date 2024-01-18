from aiogram_dialog import (
    Dialog, Window, LaunchMode,DialogManager,
)

from aiogram_dialog.widgets.kbd import (
    Start, Button)
from aiogram_dialog.widgets.text import Const
from . import states



main_dialog = Dialog(
    Window(
        Const("Выберите нужное:"),
        Start(
            text=Const('📝 Прейскурант'),
            id="price",
            state=states.Price.MAIN,
        ),
        Start(
            text=Const('ℹ️ О нас'),
            id="about",
            state=states.About.MAIN,
        ),
        Start(
            text=Const('Запись'),
            id="record",
            state=states.Record.MAIN,
        ),
        state=states.Main.MAIN,
    ),
    launch_mode=LaunchMode.ROOT,
)
