import asyncio
from aiogram import Bot, Dispatcher
from handlers import router

bot = Bot(token='7908963405:AAHAjdYjtHyxD0NqEFTLxTvLkRHPwiZNjSs')
dp = Dispatcher()

async def main():
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот выключен')