from aiogram.fsm.state import State, StatesGroup

class OrderBitchRu(StatesGroup):
    city = State()
    area = State()
    service = State()
    price = State()
    girl = State()
    after_girls = State()


class OrderBitchEn(StatesGroup):
    city = State()
    area = State()
    service = State()
    price = State()
    girl = State()
    after_girls = State()
    