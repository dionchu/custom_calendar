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
    wed_before_maundy_thursday,
    maundy_thursday,
    european_labour_day,
    ascension_day,
    whit_monday,
    christmas_eve,
    christmas,
    boxing_day,
    new_years_eve,
)

NewYearsDay = new_years_day(days_of_week=(MONDAY,TUESDAY,WEDNESDAY,THURSDAY,FRIDAY))

WednesdayBeforeMaundyThursday = wed_before_maundy_thursday()

MaundyThursday = maundy_thursday()

EuropeanLabourDay = european_labour_day(days_of_week=(MONDAY,TUESDAY,WEDNESDAY,THURSDAY,FRIDAY)

AscensionDay = ascension_day()

NOConstitutionDay = Holiday(
    "Norwegian Constitution Day",
    month=5,
    day=17,
    days_of_week=(MONDAY,TUESDAY,WEDNESDAY,THURSDAY,FRIDAY),
)

WhitMonday = whit_monday()

ChristmasEve = christmas_eve(days_of_week=(MONDAY,TUESDAY,WEDNESDAY,THURSDAY,FRIDAY))

Christmas = christmas(days_of_week=(MONDAY,TUESDAY,WEDNESDAY,THURSDAY,FRIDAY))

BoxingDay = boxing_day(days_of_week=(MONDAY,TUESDAY,WEDNESDAY,THURSDAY,FRIDAY))

NewYearsEve = new_years_eve(days_of_week=(MONDAY,TUESDAY,WEDNESDAY,THURSDAY,FRIDAY))

# Oslo Bors Holiday Calendar
# -------------------------------------

class XOSL_AbstractHolidayCalendar:
    
        regular = HolidayCalendar([
          NewYearsDay,
          MaundyThursday,  
          GoodFriday,
          EasterMonday,
          EuropeanLabourDay,
          AscensionDay,
          NOConstitutionDay,
          WhitMonday,
          ChristmasEve,
          Christmas,
          BoxingDay,
          NewYearsEve,
        ])
        
        regular_adhoc = []

        early = HolidayCalendar([
          WednesdayBeforeMaundyThursday,
        ])
