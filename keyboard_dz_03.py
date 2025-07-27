from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

# Асинхронная функция для создания начальной Inline-клавиатуры с кнопкой "Показать больше"
async def dynamic_initial_keyboard():
    # Инициализируем билдер для создания Inline-клавиатуры
    keyboard = InlineKeyboardBuilder()
    # Добавляем кнопку "Показать больше" с уникальным callback_data
    keyboard.add(InlineKeyboardButton(text="Показать больше", callback_data="show_more"))
    # Возвращаем клавиатуру с одной кнопкой
    return keyboard.as_markup()

# Асинхронная функция для создания расширенной Inline-клавиатуры с "Опция 1" и "Опция 2"
async def dynamic_extended_keyboard():
    # Инициализируем билдер для создания Inline-клавиатуры
    keyboard = InlineKeyboardBuilder()
    # Добавляем кнопку "Опция 1" с уникальным callback_data
    keyboard.add(InlineKeyboardButton(text="Опция 1", callback_data="option_1"))
    # Добавляем кнопку "Опция 2" с уникальным callback_data
    keyboard.add(InlineKeyboardButton(text="Опция 2", callback_data="option_2"))
    # Возвращаем клавиатуру с двумя кнопками в ряд
    return keyboard.adjust(2).as_markup()

