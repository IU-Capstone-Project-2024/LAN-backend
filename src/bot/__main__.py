from asyncio import run
from logging import basicConfig, INFO

from aiogram import Dispatcher, Bot
from aiogram.types import MenuButtonWebApp, WebAppInfo
from dotenv import load_dotenv

from src.bot.app.handlers import router
from src.config import bot_token


async def menu(bot: Bot):
    await bot.set_chat_menu_button(
        menu_button=MenuButtonWebApp(text='Web App', web_app=WebAppInfo(url='https://innolan.ru')))


async def on_startup() -> None:
    load_dotenv()
    basicConfig(level=INFO)
    bot = Bot(bot_token)
    dp = Dispatcher()
    dp.startup.register(menu)
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        run(on_startup())
    except KeyboardInterrupt:
        print('Bot ended')
