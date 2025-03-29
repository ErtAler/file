import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, StateFilter
from pyexpat.errors import messages

from keyboards import get_reply_keyboard, get_inline_keyboard
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
from states import Form, FormGame



TOKEN = "8185372539:AAGIqUssQw0WGxgP7oNuZ7sTXJYwiaHwSjw"

bot = Bot(token=TOKEN)
dp = Dispatcher(storage=MemoryStorage())


@dp.message(Command("start"))
async def start(message: Message):
    await message.answer("Выбери кнопку:", reply_markup=get_reply_keyboard())


@dp.message(Command("button"))
async def send_line_button(message: Message):
    await message.answer("Вот твоя кнопка: ", reply_markup=get_inline_keyboard())


@dp.callback_query(F.data == "button_pressed")
async def button_pressed(callback: CallbackQuery):
    await callback.answer("Кнопка нажата")
    await callback.message.answer("Ты большой молодец!")


@dp.message(F.text == "Привет!")
async def reply_hello(message: Message):
    await message.answer("И тебе тоже привет!")


@dp.message(F.text == "Как дела?")
async def reply_how_are_you(message: Message):
    await message.answer("Хорошо, у тебя как?")


@dp.message(F.text == "Пока!")
async def reply_bye(message: Message):
    await message.answer("До встречи!")


@dp.message(Command("form"))
async def start_form(message: Message, state: FSMContext ):
    await state.set_state(Form.name)
    await message.answer("Как тебя зовут?")


@dp.message(StateFilter(Form.name))
async def form_name(message: Message, state : FSMContext):
    await state.update_data(name = message.text)
    await state.set_state(Form.age)
    await message.answer("Сколько тебе лет?")

@dp.message(StateFilter(Form.age))
async def form_age(message : Message, state : FSMContext):
    if not message.text.isdigit():
        await message.answer("Введите возраст только в цифрах")
        return
    await state.update_data(age = int(message.text))
    await state.set_state(Form.city)
    await message.answer("Где ты живешь?")

@dp.message(StateFilter(Form.city))
async def form_city(message : Message, state : FSMContext):
    await state.update_data(city = message.text)
    data = await state.get_data()
    await message.answer(f"Спасибо за ответы! Вот твоя анкета:\n\n"
                         f"👤 Имя: {data['name']}\n"
                         f"🎂 Возраст: {data['age']}\n"
                         f"🏙️ Город: {data['city']}")
    await state.clear()  # Очищаем состояние после завершения

@dp.message(Command("form1"))
async def start_form2(message : Message, state : FSMContext):
    await state.set_state(FormGame.favorite_game)
    await message.answer("Какая ваша любимая игра?")

@dp.message(StateFilter(FormGame.favorite_game))
async def form_fgame(message : Message, state : FSMContext):
    await state.update_data(favorite_game = message.text)
    await state.set_state(FormGame.favorite_character)
    await message.answer("Какой твой любимый персонаж из этой игры?")

@dp.message(StateFilter(FormGame.favorite_character))
async def form_fcharacter(message : Message, state : FSMContext):
    await state.update_data(favorite_character = message.text)
    await state.set_state(FormGame.favorite_brend)
    await message.answer("Какой твой любимый бренд?")

@dp.message(StateFilter(FormGame.favorite_brend))
async def form_fbrend(message : Message, state : FSMContext):
    await state.update_data(favorite_brend = message.text)
    data2 = await state.get_data()
    await message.answer(f"Спасибо за ответы! Вот твоя анкета:\n\n"
                         f"👤 Любимая игра: {data2['favorite_game']}\n"
                         f"🎂 Любимая игра: {data2['favorite_character']}\n"
                         f"🏙️ Любимый бренд: {data2['favorite_brend']}")
    await state.clear()  # Очищаем состояние после завершения



# @dp.message()
# async def message_handler(message: Message):
#     if message.text == "Пока!":
#         await message.answer("")
#     elif:
#
#     else:
#

async def main():
    print("Бот запущен и ждет вашей команды . . .")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())








