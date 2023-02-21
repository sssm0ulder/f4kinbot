from .lang import langMenu
from .city import ruCityMenu, enCityMenu
from .area import ruAlmatyAreasMenu, enAlmatyAreasMenu, ruAstanaAreasMenu, enAstanaAreasMenu
from .service import ruServiceMenu, enServiceMenu
from .price import ruPriceMenu, enPriceMenu
from .girls import ruGirlsNav, enGirlsNav  #, ruGirlsMenu, enGirlsMenu
from .afer_girls import ruAfterGirlsMenu, enAfterGirlsMenu
from .lists_of_items import ru_menu_nav, en_menu_nav


_ru_keyboards = [
    ruCityMenu,
    ruAlmatyAreasMenu,
    ruAstanaAreasMenu,
    ruServiceMenu,
    ruPriceMenu,
    # ruGirlsMenu,
    ruGirlsNav
    
]

_en_keyboards = [
    enCityMenu,
    enAlmatyAreasMenu,
    enAstanaAreasMenu,
    enServiceMenu,
    enPriceMenu,
    # enGirlsMenu,
    enGirlsNav
]

for kb in _ru_keyboards:
    kb.keyboard.append(ru_menu_nav)

for kb in _en_keyboards:
    kb.keyboard.append(en_menu_nav)
