# Oslo Bors Holiday Calendar
# https://www.oslobors.no/obnewsletter/download/1e05ee05a9c1a472da4c715435ff1314/file/file/Bortfallskalender%202017-2019.pdf

#-------------------------------------------------------
# To Do:
# 

from datetime import time
from pandas import Timestamp
from pandas.tseries.holiday import (
    EasterMonday,
    GoodFriday,
    Holiday,
    previous_workday,
    MO,
    TU,
    WE,
    TH,
    FR,
    SA,
    SU,
)
from pytz import timezone

from .common_holidays import (
    new_years_day,
    european_labour_day,
    ascension_day,
    whit_monday,
    all_saints_day,    
    christmas_eve,
    christmas,
    boxing_day,
    new_years_eve,
    summer_solstice_friday,
    wed_before_maundy_thursday,
    maundy_thursday,
    friday_week_of,
)

