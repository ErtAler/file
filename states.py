from aiogram.fsm.state import StatesGroup, State


class Form(StatesGroup):
    name = State()
    age = State()
    city = State()

class FormGame(StatesGroup):
    favorite_game = State()
    favorite_character = State()
    favorite_brend = State()
