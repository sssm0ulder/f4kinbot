from .main_state import OrderBitchRu, OrderBitchEn
from .lists_of_items import ru_prices, en_prices
from .kbs import (
    ruServiceMenu,
    enServiceMenu,

    ruPriceMenu, 
    enPriceMenu,

    ruGirlsNav,
    enGirlsNav
)

from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext


r = Router()


@r.message(OrderBitchRu.price)
async def show_girls_error_ru(message: Message):
    await message.answer(
        'Ошибка. Выберите цену на клавиатуре снизу',
        reply_markup=ru_prices
    )


@r.message(OrderBitchEn.price)
async def show_girls_error_en(message: Message, state: FSMContext):
    await message.answer(
        'Error. Select a price on the keypad below',
        reply_markup=en_prices
    )
    