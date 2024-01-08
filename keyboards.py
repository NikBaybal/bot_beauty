from aiogram.types import ReplyKeyboardMarkup,InlineKeyboardMarkup, KeyboardButton,InlineKeyboardButton


start_kb=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='📝 Прейскурант'),
            KeyboardButton(text='ℹ️ О нас')
        ],
    ], resize_keyboard=True
)

catalog_kb=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Маникюр',callback_data='Маникюр')
        ],
        [
            InlineKeyboardButton(text='Педикюр',callback_data='Педикюр')
        ],
        [
            InlineKeyboardButton(text='Наращивание',callback_data='Наращивание')
        ],
        [
            InlineKeyboardButton(text='Другое',callback_data='Другое')
        ]
    ]
)

buy_kb=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🛍 Купить", url = "https://t.me/nikbaybal")
        ],
        [
            InlineKeyboardButton(text="🔙 Назад", callback_data = "back_to_preiskurant"),
        ],
    ]
)

admin_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="👥 Пользователи", callback_data = "users"),
        ],
        [
            InlineKeyboardButton(text="📊 Статистика", callback_data = "statistick"),
        ],
        [
            InlineKeyboardButton(text="✉️ Рассылка", callback_data = "mailing"),
        ],
        [
            InlineKeyboardButton(text="🔒 Блокировка", callback_data = "block"),
        ],
        [
            InlineKeyboardButton(text="🔓 Разблокировка", callback_data = "unblock"),
        ]
    ]
)

back_to_admin_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🔙 Назад", callback_data = "back_to_admin"),
        ],
    ]
)