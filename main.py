import asyncio
import logging
from aiogram import Bot, Dispatcher
from config import Config, load_config
from handlers import Start,Admin,Category
from aiogram.fsm.storage.memory import MemoryStorage

# Инициализируем логгер
logger = logging.getLogger(__name__)
# Загружаем конфиг в переменную config
config: Config = load_config()

# Инициализируем бот и диспетчер
bot = Bot(token=config.tg_bot.token,
          parse_mode='HTML')

# Функция конфигурирования и запуска бота
async def main(bot:Bot):
    # Конфигурируем логирование
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s')

    # Выводим в консоль информацию о начале запуска бота
    logger.info('Starting bot')


    dp = Dispatcher(storage=MemoryStorage())

    # Регистриуем роутеры в диспетчере
    dp.include_router(Start.router)
    dp.include_router(Category.router)
    dp.include_router(Admin.router)


    # Пропускаем накопившиеся апдейты и запускаем polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main(bot))
