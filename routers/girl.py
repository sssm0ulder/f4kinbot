from .main_state import OrderBitchRu, OrderBitchEn
from .lists_of_items import ru_prices, en_prices
from .kbs import (
    ruServiceMenu,
    enServiceMenu,

    ruGirlsNav,
    enGirlsNav,

    ruAfterGirlsMenu,
    enAfterGirlsMenu
)

from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

#  


r = Router()


@r.message(OrderBitchRu.girl, F.text == 'Следующая')
async def showing_girls_ru(message: Message, state: FSMContext):
    data = await state.get_data()
    profiles = data.get('profiles')
    current_index = data.get('current_index')

    if current_index < len(profiles) - 1:
        current_index += 1
        await message.answer(str(current_index))
        await message.answer(profiles[current_index])
        await state.update_data(current_index=current_index)
    else:
        await message.answer(
            "Анкеты закончились. Выберите кнопку ниже",
            reply_markup=ruAfterGirlsMenu
        )
        await state.set_state(OrderBitchRu.after_girls)



@r.message(OrderBitchRu.girl)
async def showing_girls_ru(message: Message, state: FSMContext):
    await message.answer(
        'Ошибка. Выберите кнопку на клавиатуре ниже',
        reply_markup=ruGirlsNav 
    )
 

@r.message(OrderBitchEn.girl, F.text == 'Next')
async def showing_girls_en(message: Message, state: FSMContext):
    data = await state.get_data()
    profiles = data.get('profiles')
    current_index = data.get('current_index')

    if current_index < len(profiles):
        current_index += 1
        await message.answer(profiles[current_index])
        await state.update_data(current_index=current_index)
    else:
        await message.answer(
            "The list items have run out. Select the button below",
            reply_markup=enAfterGirlsMenu
        )
        await state.set_state(OrderBitchEn.after_girls)



@r.message(OrderBitchEn.girl)
async def showing_girls_en(message: Message, state: FSMContext):
    await message.answer(
        'Error. Select a button on the keypad below',
        reply_markup=enGirlsNav
    )

