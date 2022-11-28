from aiogram import types, Bot, Dispatcher, executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from random import choice

bot = Bot(token='5919818030:AAF4obSo9JLZyyXaRt9pgq-dFI7zQ-XNPrA')
dp = Dispatcher(bot)
click = 0

error_list = ['Я тебя не понимаю😢', 'Такой команды не существует🎑', 'Что ты говоришь⁉']

@dp.message_handler(commands=['start'])
async def start(
    message: types.Message
):
    await message.answer(f'Привет {message.from_user.first_name} в этом боте люди заробатывают клики🎈\n'
        'так как они совместные ты можешь помогать🎫\n'
        'нажать - /click 👆\n'
        'общий баланс - /balance 🎗\n'
        'остальное - /menu 📌')
    
@dp.message_handler(commands=['click'])
async def click_command(
    message: types.Message
):
    global click
    await message.answer('ты заработал 1 клик на общий баланс🎇\nбаланс - /balance 🎉')
    click += 1

@dp.message_handler(commands=['balance'])
async def balance(
    message: types.Message
):
    global click
    await message.answer(f'Баланс общих кликов: {click} 👓')

    
click_button = KeyboardButton('Клик👆')
balance_button = KeyboardButton('Баланс🎗')
menu_button = KeyboardButton('Меню🎭')

reply_button = ReplyKeyboardMarkup()
reply_button.add(click_button)
reply_button.add(balance_button)
reply_button.add(menu_button)

@dp.message_handler(commands=['menu'])
async def menu(
    message: types.Message
):
    await message.answer('меню кнопок ниже🧧', reply_markup=reply_button)

@dp.message_handler()
async def all_battons(
    message: types.Message
):
    global click
    if message.text == 'Клик👆':
        await message.answer('ты заработал 1 клик на общий баланс🎇\nбаланс - /balance 🎉')
        click += 1
    elif message.text == 'Баланс🎗':
        await message.answer(f'Баланс общих кликов: {click}👓')
    elif message.text == 'Меню🎭':
        await message.answer('Ты и так в меню🎃')
    else:
        error = choice(error_list)
        await message.answer(error)


executor.start_polling(dp)