# Stockholm OMX Holiday Calendar
# http://www.nasdaqomxnordic.com/vidskiptatimi

#-------------------------------------------------------
# To Do:
# All Saints Day early close was not observed in 2010
# Check whether Day Before Ascension Day was early close
# Nasdaq says no, FESE says yes

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
    epiphany,    
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

NewYearsDay = new_years_day()

EpiphanyDay = epiphany()

EuropeanLabourDay = european_labour_day()

AscensionDay = ascension_day()

SENationalDay = Holiday(
    "National Day of Sweden",
    month=6,
    day=6,
)

SummerSolsticeFriday = summer_solstice_friday()

WhitMonday = whit_monday()

ChristmasEve = christmas_eve()

Christmas = christmas()

BoxingDay = boxing_day()

NewYearsEve = new_years_eve()

def twelfth_night_early_close_observance(datetime_index):
    return datetime_index[~datetime_index.year.isin([2010])]

TwelfthNight = Holiday(
    'Twelfth Night',
    month=1,
    day=5,
    days_of_week=(MONDAY,TUESDAY,WEDNESDAY,THURSDAY,FRIDAY),
    observance=twelfth_night_early_close_observance,
)

MaundyThursday = maundy_thursday()

WalpurgisNight = Holiday(
    'Walpurgis Night',
    month=4,
    day=30,
    days_of_week=(MONDAY,TUESDAY,WEDNESDAY,THURSDAY,FRIDAY),
)

AllSaintsEve = all_saints_day(observance=friday_week_of)


# Nasdaq OMX Holiday Calendar
# -------------------------------------

class XSTO_AbstractHolidayCalendar:
    
        regular = HolidayCalendar([
          NewYearsDay,
          GoodFriday,
          EasterMonday,
          WhitMonday,
          ChristmasEve,
          Christmas,
          BoxingDay,
          NewYearsEve,
        ])
        
        regular_adhoc = list(
          SummerSolsticeFriday
        )

        early = HolidayCalendar([
            TwelfthNight,
            MaundyThursday,
            WalpurgisNight,
            BusinessDayPriorToMemorialDay,
            AllSaintsEve,
        ])
