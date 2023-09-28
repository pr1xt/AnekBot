import keyboards as kb
import pickle
import random as rn
from Token import TOKEN, admin_id
import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from funcs import check_user, is_admin


bot = Bot(TOKEN)
dp = Dispatcher()

last_move = 0
@dp.message(F.text == '/start')
async def cmd_start(message: Message):
    await message.answer('Добро пожаловать! Это бот для хранения и пересылки анекдотов', reply_markup=kb.main)


@dp.message(F.text == "/admin")
async def help_kommand(message: Message):
    if is_admin(message):
        await message.answer("Hello, admin", reply_markup=kb.admin)
    else:
        await message.answer("Отказ в доступе", reply_markup=kb.main)


@dp.message(F.text == "Последние логи")
async def help_kommand(message: Message):
    if is_admin(message):
        f = open("data/logs.txt", "r")
        last_log = [f"{i[0:-1]}" for i in f.read().split("\n")[-1:-7:-1]]
        last_log = str(last_log)[4:-1]
        await message.answer(last_log, reply_markup=kb.admin)


@dp.message(F.text == "Основная клава")
async def help_kommand(message: Message):
    await message.answer("Готово", reply_markup=kb.main)


@dp.message(F.text == '/my_id')
async def cmd_my_id(message: Message):
    await message.answer(f'Ваш ID: {message.from_user.id}')

@dp.message(F.text == "Добавить анекдот")
async def add_joke(message: Message):
    global last_move
    await message.answer("Вышлите ваш анекдот", reply_markup=kb.main)
    last_move = 2


@dp.message(F.text == "Контакты")
async def contact(message: Message):
    await message.answer("@newername", reply_markup=kb.main)


@dp.message(F.text =="Случайный анекдот")
async def random_joke(message: Message):
    with open("C:\Programming\AnekBot\data\jokes_copy1.txt", "rb") as file:
        dct = pickle.load(file)
        rndint = rn.randint(0, len(dct))
        joke = f"{rndint}\n{(dct[rndint])}"

    await message.answer(f"{joke}", reply_markup=kb.main)
    check_user(message)

@dp.message(F.text =="Анекдот по номеру")
async def number_joke(message: Message):
    global last_move
    await message.answer(f"Напишите номер анекдота")
    last_move = 1


@dp.message()
async def echo(message: Message):
    global last_move

    if last_move == 1:
        try:
            with open("C:\Programming\AnekBot\data\jokes_copy1.txt", "rb") as file:
                dct = pickle.load(file)
                joke = f"{int(message.text)}\n{(dct[int(message.text)])}"
            await message.answer(f"{joke}", reply_markup=kb.main)
            check_user(message)
        except:
            await message.answer("Ошибка значенния", reply_markup=kb.main)
            print(last_move)
        last_move = 0
    elif last_move == 2:
        with open("C:\Programming\AnekBot\data\jokes_copy1.txt", "rb") as file:
            dct = pickle.load(file)
        key = int(list(dct.keys())[-1]) + 1
        dct.update({key:message.text})
        await message.answer(f"Вы хотите добавить этот анекдот?\n\n{dct[key]}", reply_markup=kb.approve)
        with open("C:\Programming\AnekBot\data\\buffer.txt", "wb") as buffer:
            pickle.dump(dct, buffer)
            buffer.close()
        last_move = 3
    elif last_move == 3:
        if message.text == "Да, добавить":
            with open("C:\Programming\AnekBot\data\\buffer.txt", "rb") as buffer:
                dct_buffer = pickle.load(buffer)
                buffer.close()
            with open("C:\Programming\AnekBot\data\jokes_copy1.txt", "wb") as file:
                pickle.dump(dct_buffer, file)
            key = int(list(dct_buffer.keys())[-1])
            last_move = 0
            await message.answer(f"Вы добавили анекдот\n Номер анекдота - {key}\n{dct_buffer[key]}", reply_markup=kb.main)
        elif message.text == "Нет":
            last_move = 0
            await message.answer(f"Вы хотите добавить этот анекдот?\n{dct[key]}", reply_markup=kb.main)
    else:
        await message.answer('Ощибка ввода', reply_markup=kb.main)
        print(last_move)
        last_move = 0


async def Main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(Main())
