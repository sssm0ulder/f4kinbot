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


@r.message(CommandStart())
@r.message(F.text.in_(['Главное меню', 'Main menu']))
async def command_start(message: Message, state: FSMContext):
    await message.answer(
        'Выберите язык | Choose language',
        reply_markup=langMenu
    )
    await state.set_state(ChooseLang.lang)


@r.message(ChooseLang.lang, F.text == 'RU')
async def ru_lang(message: Message, state: FSMContext):
    await message.answer(
            'Выберите город',
            reply_markup=ruCityMenu
        )
    await state.set_state(OrderBitchRu.city)


@r.message(ChooseLang.lang, F.text == 'EN')
async def en_lang(message: Message, state: FSMContext):
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
    