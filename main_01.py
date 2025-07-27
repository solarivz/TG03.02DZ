import asyncio
import keyboard_01 as kb  # Импорт модуля keyboards под псевдонимом kb
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from config import TOKEN

# Инициализация бота с токеном из файла конфигурации
bot = Bot(token=TOKEN)

# Создание диспетчера для обработки входящих обновлений от Telegram
dp = Dispatcher()

# Хэндлер для команды /start — отправка приветственного сообщения с клавиатурой
@dp.message(CommandStart())
async def start(message: Message):
    # Отправляем приветственное сообщение и прикрепляем клавиатуру
    await message.answer("Выберите действие:", reply_markup=await kb.start_keyboard())

# Хэндлер для обработки нажатия на кнопку "Привет"
@dp.callback_query(F.data == "say_hello")
async def say_hello_callback(callback: CallbackQuery):
    # Отправляем приветствие с именем пользователя
    await callback.message.edit_text(f"Привет, {callback.from_user.first_name}!")
    await callback.answer()  # Закрываем уведомление

# Хэндлер для обработки нажатия на кнопку "Пока"
@dp.callback_query(F.data == "say_goodbye")
async def say_goodbye_callback(callback: CallbackQuery):
    # Отправляем прощание с именем пользователя
    await callback.message.edit_text(f"До свидания, {callback.from_user.first_name}!")
    await callback.answer()  # Закрываем уведомление

# Асинхронная главная функция для запуска бота
async def main():
    await dp.start_polling(bot)  # Запускаем polling для получения обновлений

if __name__ == "__main__":
        asyncio.run(main())  # Запускаем основную функцию в асинхронном режиме
