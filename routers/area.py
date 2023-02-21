from .main_state import OrderBitchRu, OrderBitchEn
from .lists_of_items import (
    ru_Almaty_areas, 
    ru_Astana_areas, 
    en_Almaty_areas, 
    en_Astana_areas
)
from .kbs import enServiceMenu, ruServiceMenu

from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext


r = Router()

_all_areas_ru = ru_Almaty_areas + ru_Astana_areas
_all_areas_en = en_Almaty_areas + en_Astana_areas


@r.message(OrderBitchRu.area, F.text.in_(_all_areas_ru))
async def select_area_ru(message: Message, state: FSMContext):
    await message.answer(
        text='Выберите услугу',
        reply_markup=ruServiceMenu
    )
    await state.set_state(OrderBitchRu.service)


@r.message(OrderBitchEn.area, F.text.in_(_all_areas_en))
async def select_area_en(message: Message, state: FSMContext):
    await message.answer(
        text='Select the service',
        reply_markup=enServiceMenu
    )
    await state.set_state(OrderBitchEn.service)


@r.message(OrderBitchRu.area)
async def select_area_error_ru(message: Message, state: FSMContext):
    await message.answer(
        text='Вы ввели неверный район',
        reply_markup=ruServiceMenu
    )


@r.message(OrderBitchEn.area)
async def select_area_error_en(message: Message, state: FSMContext):
    await message.answer(
        text='You entered the wrong area',
        reply_markup=enServiceMenu
    )
    