from aiogram.types import InlineKeyboardButton, InlineKeyboardBuilder

# Асинхронная функция для создания Inline-клавиатуры с кнопками "Привет" и "Пока"
async def start_keyboard():
    # Инициализируем билдер для создания Inline-клавиатуры
    keyboard = InlineKeyboardBuilder()
    # Добавляем кнопку "Привет" с уникальным callback_data
    keyboard.add(InlineKeyboardButton(text="Привет", callback_data="say_hello"))
    # Добавляем кнопку "Пока" с уникальным callback_data
    keyboard.add(InlineKeyboardButton(text="Пока", callback_data="say_goodbye"))
    # Возвращаем клавиатуру с одной кнопкой в ряд
    return keyboard.as_markup()