from tkinter.ttk import Button

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import (KeyboardButton, Message, ReplyKeyboardMarkup,
                           ReplyKeyboardRemove)

BOT_TOKEN = '8119757037:AAEL2hYtDFA3HH_cv0L4_TVEHOT1PeNHbFw'

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

button1 = KeyboardButton(text="• Какие игры вы предлагаете?")
button2 = KeyboardButton(text="• Есть ли возможность поиграть против других колледжей?")
button3 = KeyboardButton(text="• Какие есть развлечения помимо игр?")
button4 = KeyboardButton(text="• Какие часы работы клуба? ")
button5 = KeyboardButton(text="• Как часто проходят турниры")
button6 = KeyboardButton(text="• Какие призы получают победители турниров?")
button7 = KeyboardButton(text="• Как связаться с клубом?")
button8 = KeyboardButton(text="• Есть ли у вас команда?")
button9 = KeyboardButton(text="• Как я могу стать частью команды?")


keyboard = ReplyKeyboardMarkup(keyboard=[[button1],
                                         [button2],
                                         [button3],
                                         [button4],
                                         [button5],
                                         [button6],
                                         [button7],
                                         [button8],
                                            [button9]])

@dp.message(CommandStart())
async def precess_start_commond(message: Message):
    await message.answer(
        text = "Привет я помогу тебя решить твой вопрос",
        reply_markup=keyboard
    )

@dp.message(F.text =="• Какие игры вы предлагаете?")
async def commond_button1(message:Message):
    await  message.answer(
        text="Мы предлагаем игры Dota 2, Valorant, CS:GO, FIFA, Fortnite",
        reply_markup=keyboard
    )
@dp.message(F.text =="• Есть ли возможность поиграть против других колледжей?")
async def commond_button2(message:Message):
    await  message.answer(
        text="Да, мы проводим игры против других колледжей, а также участвуем в турнирах",
        reply_markup=keyboard
    )
@dp.message(F.text =="• Какие есть развлечения помимо игр?")
async def commond_button3(message:Message):
    await  message.answer(
        text="""Мы также предлагаем развлекательные мероприятия, такие как игры в VR, настольные игры, кинопросмотры, проводим киберквиз
        
У нас есть возможность участвовать на мероприятиях в VK Play Arena и возможность играть на локальной площадке""",
        reply_markup=keyboard
    )
@dp.message(F.text =="• Какие часы работы клуба?")
async def commond_button4(message:Message):
    await  message.answer(
        text="Клуб работает после окончания пар и до 5 вечера ",
        reply_markup=keyboard
    )
@dp.message(F.text =="• Как часто проходят турниры")
async def commond_button5(message:Message):
    await  message.answer(
        text=" Мы проводим турниры по различным играм на регулярной основе"
             " Следите за анонсами на нашей странице в соцсетях",
        reply_markup=keyboard
    )
@dp.message(F.text =="• Какие призы получают победители турниров?")
async def commond_button6(message:Message):
    await  message.answer(
        text="Призы для победителей турниров зависят от типа турнира",
        reply_markup=keyboard
    )
@dp.message(F.text =="• Как связаться с клубом?")
async def commond_button7(message:Message):
    await  message.answer(
        text="Связывайтесь с клубом через его страницу, мы всегда готовы помочь",
        reply_markup=keyboard
    )
@dp.message(F.text =="• Есть ли у вас команда?")
async def commond_button8(message:Message):
    await  message.answer(
        text="У нас функционируют команды по таким направлениям как Dota 2, Valorant, CS:GO, FIFA, Fortnite",
        reply_markup=keyboard
    )
@dp.message(F.text =="• Как я могу стать частью команды?")
async def commond_button9(message:Message):
    await  message.answer(
        text="Следите за объявлениями на странице клуба и заполняйте анкету которую можно найти на странице клуба",
        reply_markup=keyboard
    )


if __name__ == "__main__":
    dp.run_polling(bot)