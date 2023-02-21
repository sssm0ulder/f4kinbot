from typing import Iterable, List

from aiogram.types import (
    ReplyKeyboardMarkup, 
    KeyboardButton, 
)


def split_list(list, sublist_length = 2):
    return [list[i:i+sublist_length] for i in range(0, len(list), sublist_length)]


def make_kb_from_list(items: Iterable, row_len: int = 2) -> ReplyKeyboardMarkup:
    kb = split_list([KeyboardButton(text=item) for item in items], row_len)
    return ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
