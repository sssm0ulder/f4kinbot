from .main_state import OrderBitchRu, OrderBitchEn
from .lists_of_items import ru_services, en_services
from .kbs import (
    ruPriceMenu,
    enPriceMenu,

    ruServiceMenu,
    enServiceMenu  
)

from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

 

r = Router()



@r.message(OrderBitchRu.service, F.text.in_(ru_services))
async def select_service_ru(message: Message, state: FSMContext):
    if message.text in ['Индивидуалка', 'БДСМ']:
        await message.answer(
            'Выберите ценовой диапазон',
            reply_markup=ruPriceMenu
        )
        await state.set_state(OrderBitchRu.price)
    else:
        await message.answer('Мы отобрали анкеты, которые вам понравятся.')
        await state.set_state(OrderBitchRu.girl)


@r.message(OrderBitchRu.service)
async def select_service_error_ru(message: Message, state: FSMContext):
    await message.answer(
        'Вы ввели неизвестную услугу. Выберите её из клавиатуры снизу',
        reply_markup=ruServiceMenu
    )


@r.message(OrderBitchEn.service, F.text.in_(en_services))
async def select_service_en(message: Message, state: FSMContext):
    if message.text in ['Individual', 'BDSM']:
        await message.answer(
            'Choose your price range',
            reply_markup=enPriceMenu
        )
        await state.set_state(OrderBitchEn.price)
    else:
        await message.answer('We have selectedprofiles that you will like.')
        await state.set_state(OrderBitchRu.girl)


@r.message(OrderBitchEn.service)
async def select_service_error_en(message: Message, state: FSMContext):
    await message.answer(
       'You have entered an unknown service. Select it from the keypad below',
        reply_markup=enServiceMenu
    )
