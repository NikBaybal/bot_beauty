start_admin = 'Вы открыли <b>Панель администратора</b>'

def statistick(count):
    text = f'Количество пользователей бота: <pre>{count}</pre>'
    return text


ban_from_admin_start = '''Укажите ID пользователя, которого хотите заблокировать!

<i>Пример: 1046276866

Если не хотите блокировать пользователя, нажмите /cancel</i>'''

ban_from_admin_except = '''❗️ Ошибка. Указывайте цифрами ❗️
Укажите ID пользователя, которого хотите заблокировать!

<i>Пример: 1046276866

Если не хотите блокировать пользователя, нажмите /cancel</i>'''
unban_from_admin_start = '''Укажите ID пользователя, которого хотите разблокировать!

<i>Пример: 1046276866

Если не хотите разблокировать пользователя, нажмите /cancel</i>'''

unban_from_admin_except = '''❗️ Ошибка. Указывайте цифрами ❗️
Укажите ID пользователя, которого хотите разблокировать!

<i>Пример: 1046276866

Если не хотите разблокировать пользователя, нажмите /cancel</i>'''

unban_from_admin_finaly = '✅ Вы успешно разблокировали пользователя: '

ban_from_admin_finaly = '✅ Вы успешно заблокировали пользователя: '
