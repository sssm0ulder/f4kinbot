from .utils import make_kb_from_list 

from .lists_of_items import (
    en_Almaty_areas, 
    ru_Almaty_areas, 
    en_Astana_areas, 
    ru_Astana_areas
)


ruAlmatyAreasMenu = make_kb_from_list(ru_Almaty_areas, row_len=2)
enAlmatyAreasMenu = make_kb_from_list(en_Almaty_areas, row_len=2)

ruAstanaAreasMenu = make_kb_from_list(ru_Astana_areas, row_len=2)
enAstanaAreasMenu = make_kb_from_list(en_Astana_areas, row_len=2)
