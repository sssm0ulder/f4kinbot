from .utils import make_kb_from_list 
from .lists_of_items import (
    ru_prices,
    en_prices
)

ruPriceMenu = make_kb_from_list(
    ru_prices, 
    row_len=3
)

enPriceMenu = make_kb_from_list(
    en_prices, 
    row_len=3
)
