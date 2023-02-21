from .kbs import langMenu, ruCityMenu, enCityMenu
from .main_state import OrderBitchRu, OrderBitchEn
from .lists_of_items import langs

from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup


r = Router()


class ChooseLang(StatesGroup):
    lang = State()


@r.message(F.text.in_(['Главное меню', 'Main menu']))
@r.message(CommandStart())
async def command_start(message: Message, state: FSMContext):
    await message.answer(
        'Выберите язык | Choose language',
        reply_markup=langMenu
    )
    await state.set_state(ChooseLang.lang)


@r.message(ChooseLang.lang, F.text.in_(langs))
async def select_lang(message: Message, state: FSMContext):
    
    if message.text == 'RU':
        await message.answer(
            'Выберите город',
            reply_markup=ruCityMenu
        )
        await state.set_state(OrderBitchRu.city)

    elif message.text == 'EN':
        await message.answer(
            'Choose city',
            reply_markup=enCityMenu
        )
        await state.set_state(OrderBitchEn.city)



@r.message(ChooseLang.lang)
async def select_lang_error(message: Message, state: FSMContext):
    await message.answer(
        'Неопределённый язык, попробуйте снова | Undefined language, try again.'
    )
    