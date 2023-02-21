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

#  


r = Router()


@r.message(OrderBitchRu.price, F.text.in_(ru_prices))
async def choose_price_ru(message: Message, state: FSMContext):
    # db = Database.get_instance()
    data = await state.get_data()

    profiles =  [f'*Профиль {i}*' for i in range(5)]  # Тут должна быть автоматическая подгрузка данных из бд
    await state.update_data(profiles=profiles)

    if not profiles:
        await message.answer(
            'К сожалению, анкет с подобными параметрами найти не удалось.'
        )
        await message.answer(
            text='Выберите услугу',
            reply_markup=ruServiceMenu
        )

        await state.set_state(OrderBitchRu.service)
    else:
        current_index = data.get('current_index', 0)
        await state.update_data(current_index=current_index)
        await message.answer(
            text=f"Анкет с такими параметрами: {len(profiles)}",
            reply_markup=ruGirlsNav
        )
        await message.answer(profiles[current_index])
        await state.set_state(OrderBitchRu.girl)
    

@r.message(OrderBitchRu.price)
async def choose_price_error_ru(message: Message):
    await message.answer(
        'Ошибка. Выберите цену на клавиатуре снизу',
        reply_markup=ru_prices
    )


@r.message(OrderBitchEn.price, F.text.in_(en_prices))
async def choose_price_en(message: Message, state: FSMContext):
    # db = Database.get_instance()
    data = await state.get_data()

    profiles = [f'*Profile {i}*' for i in range(5)]  # Тут должна быть автоматическая подгрузка данных из бд
    await state.update_data(profiles=profiles)

    if not profiles:
        await message.answer(
            'Unfortunately, I could not find anyprofiles with similar parameters.'
        )
        await message.answer(
            text='Select a service',
            reply_markup=enServiceMenu
        )

        await state.set_state(OrderBitchEn.service)
    else:
        current_index = data.get('current_index', 0)
        await state.update_data(current_index=current_index)
        await message.answer(
            text=f"Profiles with these parameters: {len(profiles)}",
            reply_markup=enGirlsNav
        )
        await message.answer(profiles[current_index])
        await state.set_state(OrderBitchEn.girl)


@r.message(OrderBitchEn.price)
async def choose_price_error_en(message: Message, state: FSMContext):
    await message.answer(
        'Error. Select a price on the keypad below',
        reply_markup=en_prices
    )
