from aiogram.fsm.state import State, StatesGroup


class Main(StatesGroup):
    MAIN = State()
class Price(StatesGroup):
    MAIN = State()

class About(StatesGroup):
    MAIN = State()

class Record(StatesGroup):
    MAIN = State()
    Date = State()
    Hour = State()