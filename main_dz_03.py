import asyncio
import keyboard_dz_03 as kb  
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from config import TOKEN


bot = Bot(token=TOKEN)
dp = Dispatcher()


# Хэндлер для команды /dynamic — отправка сообщения с начальной клавиатурой
@dp.message(Command("dynamic"))
async def dynamic(message: Message):
    # Отправляем сообщение с начальной клавиатурой
    await message.answer("Нажмите, чтобы увидеть опции:", reply_markup=await kb.dynamic_initial_keyboard())

# Хэндлер для обработки нажатия на "Показать больше"
@dp.callback_query(F.data == "show_more")
async def show_more_callback(callback: CallbackQuery):
    # Заменяем клавиатуру на расширенную с двумя опциями
    await callback.message.edit_reply_markup(reply_markup=await kb.dynamic_extended_keyboard())
    await callback.answer()  # Закрываем уведомление

# Хэндлер для обработки нажатия на "Опция 1"
@dp.callback_query(F.data == "option_1")
async def option_1_callback(callback: CallbackQuery):
    # Отправляем сообщение с текстом выбранной опции
    await callback.message.edit_text("Вы выбрали: Опция 1")
    await callback.answer()  # Закрываем уведомление

# Хэндлер для обработки нажатия на "Опция 2"
@dp.callback_query(F.data == "option_2")
async def option_2_callback(callback: CallbackQuery):
    # Отправляем сообщение с текстом выбранной опции
    await callback.message.edit_text("Вы выбрали: Опция 2")
    await callback.answer()  # Закрываем уведомление



async def main():
    await dp.start_polling(bot)  # Запускаем polling для получения обновлений

if __name__ == "__main__":
    asyncio.run(main())  # Запускаем основную функцию в асинхронном режиме
