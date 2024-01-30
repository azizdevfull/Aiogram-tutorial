from aiogram.fsm.state import StatesGroup,State

class sign_up(StatesGroup):
    name = State()
    age = State()
