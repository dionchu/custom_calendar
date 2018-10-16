# Oslo Bors Holiday Calendar
# https://www.oslobors.no/obnewsletter/download/1e05ee05a9c1a472da4c715435ff1314/file/file/Bortfallskalender%202017-2019.pdf
# Check against Federation of European Securities Exchanges: http://www.fese.eu/statistics-market-research/trading-calendar
#   provides history back to 2007

#-------------------------------------------------------
# To Do:
# 

from datetime import time
from pandas import Timestamp
from pandas.tseries.offsets import Day
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
    Easter,
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

from .holiday_extensions import (
    friday_week_of,
    HolidayWithFilter,
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

# Whit Monday was open for trading on Oslo Bors in 2009
WhitMondayExcept2009 = HolidayWithFilter(
        "Whit Monday",
        month=1,
        day=1,
        offset=[Easter(), Day(50)],
        year_filter = [2009],
    )

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
          WhitMondayExcept2009,
          ChristmasEve,
          Christmas,
          BoxingDay,
          NewYearsEve,
        ])
        
        regular_adhoc = []

        early = HolidayCalendar([
          WednesdayBeforeMaundyThursday,
        ])
