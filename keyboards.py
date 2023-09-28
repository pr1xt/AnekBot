from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)

main_kb = [
    [KeyboardButton(text='Случайный анекдот')],
    [KeyboardButton(text='Анекдот по номеру'), KeyboardButton(text='Добавить анекдот'),],
    [KeyboardButton(text='Контакты')]
]

admin_kb = [
    [KeyboardButton(text='Последние логи')],
    [KeyboardButton(text='Основная клава')]
]

approve_kb = [
    [KeyboardButton(text='Да, добавить')],
    [KeyboardButton(text='Нет')]
]

main = ReplyKeyboardMarkup(keyboard=main_kb,
                           resize_keyboard=True,
                           input_field_placeholder='Выберите пункт ниже')

admin = ReplyKeyboardMarkup(keyboard=admin_kb,
                           resize_keyboard=True,
                           input_field_placeholder='Выберите пункт ниже')

approve = ReplyKeyboardMarkup(keyboard=approve_kb,
                           resize_keyboard=True,
                           input_field_placeholder='Выберите пункт ниже')