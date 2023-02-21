from .utils import make_kb_from_list 
from .lists_of_items import (
    en_services,
    ru_services
)


ruServiceMenu = make_kb_from_list(
    ru_services,
    row_len=3
)

enServiceMenu = make_kb_from_list(
    en_services,
    row_len=3
)
