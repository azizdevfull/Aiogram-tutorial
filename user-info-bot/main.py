from aiogram import Bot, Dispatcher
from asyncio import run
from functions import get_user_info, start_answer, help_answer
from aiogram.types import BotCommand
from aiogram.filters import Command

dp = Dispatcher()

async def startup_answer(bot: Bot):
    await bot.send_message(1184193890, "Bot Ishga tushdi! ✅")

async def shutdown_answer(bot: Bot):
    await bot.send_message(1184193890, "Bot ishdan to'xtadi! ❌")

async def start():

    dp.startup.register(startup_answer)

    dp.message.register(start_answer, Command("start"))
    dp.message.register(help_answer, Command("help"))

    dp.message.register(get_user_info)
    
    dp.shutdown.register(shutdown_answer)
    
    bot = Bot("6803882554:AAH91YHRcmFQQnZmhzy0ZWpRXscZiJBNeV4")
    await bot.set_my_commands([
        BotCommand(command="/start", description="Botni ishga tushurish"),
        BotCommand(command="/help", description="Yordam" )
    ])
    await dp.start_polling(bot)

run(start())
