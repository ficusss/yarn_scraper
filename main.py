from parsers import parse_terrakot18, parse_optwool, parse_2676270, \
    parse_supernitki, parse_rukodelie_online, parse_klubok_store, parse_pryazhaoptom, \
    parse_yarn_ural, parse_nopt, parse_airis_spb, parse_kudel
import pandas as pd

TRACK_CODES = [2, 13, 19, 98, 183, 262, 310, 378, 414, 416, 509, 599, 639, 742]
TRACK_CODES = [13, 310]

items = []
items.extend(parse_terrakot18())
items.extend(parse_optwool())
items.extend(parse_2676270())
items.extend(parse_rukodelie_online())
items.extend(parse_klubok_store())
items.extend(parse_pryazhaoptom())
items.extend(parse_yarn_ural())
items.extend(parse_nopt())
# items.extend(parse_kudel()) # возвращается пустая страница
# items.extend(parse_airis_spb()) # пока не работает (нужна регистрация)


df_yarn = pd.DataFrame(items)
df_yarn = df_yarn.sort_values(by="price")
df_yarn = df_yarn.sort_values(by="code")

df_track_yarn = df_yarn[df_yarn.code.isin(TRACK_CODES)]
print(df_track_yarn)
print(f"Отслеживаемых наименований в продаже: {len(set(df_track_yarn.code))} / {len(TRACK_CODES)}")
print()
print(df_yarn)
