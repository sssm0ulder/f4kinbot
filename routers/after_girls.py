from .main_state import OrderBitchRu, OrderBitchEn
from .lists_of_items import ru_prices, en_prices
from .kbs import (
    ruServiceMenu,
    enServiceMenu,

    ruAfterGirlsMenu,
    enAfterGirlsMenu
)

from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext


r = Router()

@r.message(OrderBitchRu.price, F.text == 'Назад')
@r.message(OrderBitchRu.girl, F.text == 'Назад')
@r.message(OrderBitchRu.after_girls, F.text == 'Назад')
async def after_girls_back_ru(message: Message, state: FSMContext):
    await message.answer(
        text='Выберите услугу',
        reply_markup=ruServiceMenu
    )
    await state.set_state(OrderBitchRu.service)


@r.message(OrderBitchEn.girl, F.text == 'Back')
@r.message(OrderBitchEn.price, F.text == 'Back')
@r.message(OrderBitchEn.after_girls, F.text == 'Back')
async def after_girls_back_en(message: Message, state: FSMContext):
    await message.answer(
        text='Select a service',
        reply_markup=enServiceMenu
    )
    await state.set_state(OrderBitchEn.service)


@r.message(OrderBitchRu.after_girls)
async def after_girls_menu_error_en(message: Message, state: FSMContext):
    await message.answer(
        text='Ошибка. Выберите кнопку на клавиатуре ниже',
        reply_markup=ruAfterGirlsMenu
    )


@r.message(OrderBitchEn.after_girls)
async def after_girls_menu_error_en(message: Message, state: FSMContext):
    await message.answer(
        'Error. Select a button on the keypad below',
        reply_markup=enAfterGirlsMenu
    )
