from parsers import parse_terrakot18, parse_optwool, parse_2676270, parse_supernitki
from pprint import pprint
import pandas as pd

TRACK_CODES = [2, 13, 19, 98, 183, 262, 310, 378, 414, 416, 509, 599, 639, 742]

items = []
items.extend(parse_terrakot18())
items.extend(parse_optwool())
items.extend(parse_2676270())

df_yarn = pd.DataFrame(items)
df_yarn = df_yarn.sort_values(by="code")

df_track_yarn = df_yarn[df_yarn.code.isin(TRACK_CODES)]
print(df_track_yarn)
print()
print(df_yarn)


# parse_supernitki()