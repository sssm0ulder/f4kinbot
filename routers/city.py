from .main_state import OrderBitchRu, OrderBitchEn
from .lists_of_items import ru_cities, en_cities
from .kbs import (
    ruAlmatyAreasMenu, 
    enAlmatyAreasMenu, 
    ruAstanaAreasMenu, 
    enAstanaAreasMenu,

    enServiceMenu,
    ruServiceMenu
)

from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext


r = Router()


@r.message(OrderBitchRu.city, F.text.in_(ru_cities))
async def select_city_ru(message: Message, state: FSMContext):
    if message.text == 'Алматы':
        await message.answer(
            'Выберите район',
            reply_markup=ruAlmatyAreasMenu
        )
        await state.set_state(OrderBitchRu.area)
    elif message.text == 'Астана':
        await message.answer(
            'Выберите район',
            reply_markup=ruAstanaAreasMenu
        )
        await state.set_state(OrderBitchRu.area)
    elif message.text == 'Шымкент':
        await message.answer(
            text='Выберите услугу',
            reply_markup=ruServiceMenu
        )
        await state.set_state(OrderBitchRu.service)


@r.message(OrderBitchEn.city, F.text.in_(en_cities))
async def select_city_en(message: Message, state: FSMContext):
    if message.text == 'Almaty':
        await message.answer(
            'Select area',
            reply_markup=enAlmatyAreasMenu
        )
        await state.set_state(OrderBitchEn.area)
    elif message.text == 'Astana':
        await message.answer(
            'Select area',
            reply_markup=enAstanaAreasMenu
        )
        await state.set_state(OrderBitchEn.area)
    elif message.text == 'Shymkent':
        await message.answer(
            text='Select a service',
            reply_markup=enServiceMenu
        )
        await state.set_state(OrderBitchEn.service)


@r.message(OrderBitchRu.city)
async def select_city_error_ru(message: Message, state: FSMContext):
    await message.answer(
        'Ответ неверный, попробуйте снова.',
        reply_markup=ru_cities
    )


@r.message(OrderBitchEn.city)
async def select_city_error_en(message: Message, state: FSMContext):
    await message.answer(
        'The answer is wrong, try again.',
        reply_markup=en_cities
    )
