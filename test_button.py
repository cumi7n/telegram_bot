from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import  (KeyboardButton, Message, ReplyKeyboardMarkup,
                           ReplyKeyboardRemove)


BOT_TOKEN = ""

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

button1 = KeyboardButton(text="Кто отвечает за компетенции и управляет клубом?")
button2 = KeyboardButton(text="Какое расписание тренировок?")
button3 = KeyboardButton(text="Какие игры доступны в клубе?")


keybord = ReplyKeyboardMarkup(keyboard=[[button1, button2,button3]])

@dp.message(CommandStart())
async def process_start_command(message:Message):
    await message.answer(
        text = "Какие у вас вопросы",
        reply_markup=keybord
    )


@dp.message(F.text == """
Рома — отвечает за 1-2 команду по CS
Рустам — отвечает за 3-4 состав по CS
Соня — отвечает за все команды по Dota
""")

async def message_one(message:Message):
    await message.answer(
        text = "ответ на первыйвопрос",
        reply_markup=ReplyKeyboardRemove()
    )

@dp.message(F.text == "Какое расписание тренировок?")
async def message_two(message:Message):
    await message.answer(
        text="Расписание тренировок можно узнать после распределения в команду у командира или менеджера компетенции",
        reply_markup=ReplyKeyboardRemove()
    )


@dp.message(F.text == "Какие игры доступны в клубе?")
async def message_two(message:Message):
    await message.answer(
        text="CS, Dota, Fifa, Дроны, Валорант",
        reply_markup=ReplyKeyboardRemove()
    )


if __name__ == "__main__":
    dp.run_polling(bot)