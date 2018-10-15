from datetime import time
from itertools import chain
import pandas as pd
from pandas.tseries.holiday import (
    Holiday,
    DateOffset,
    MO,
    weekend_to_monday,
    GoodFriday
)
from pytz import timezone

from .trading_calendar import (
    TradingCalendar,
    HolidayCalendar,
    MONDAY,
    TUESDAY,
    WEDNESDAY,
    THURSDAY,
    FRIDAY,
)

from .common_holidays import (
    new_years_day,
    christmas,
    weekend_christmas,
    boxing_day,
    weekend_boxing_day,
)


# New Year's Day
CANewYearsDay = new_years_day(observance=weekend_to_monday)

# Ontario Family Day
FamilyDay = Holiday(
    "Family Day",
    month=2,
    day=1,
    offset=DateOffset(weekday=MO(3)),
    start_date='2008-01-01',
)
# Victoria Day
VictoriaDay = Holiday(
    'Victoria Day',
    month=5,
    day=24,
    offset=DateOffset(weekday=MO(-1)),
)
# Canada Day
CanadaDay = Holiday(
    'Canada Day',
    month=7,
    day=1,
    observance=weekend_to_monday,
)
# Civic Holiday
CivicHoliday = Holiday(
    'Civic Holiday',
    month=8,
    day=1,
    offset=DateOffset(weekday=MO(1)),
)
# Labor Day
LaborDay = Holiday(
    'Labor Day',
    month=9,
    day=1,
    offset=DateOffset(weekday=MO(1)),
)
# Canadian Thanksgiving
CanadianThanksgiving = Holiday(
    'Canadian Thanksgiving',
    month=10,
    day=1,
    offset=DateOffset(weekday=MO(2)),
)

ChristmasEveEarlyClose2010Onwards = Holiday(
    'Christmas Eve Early Close',
    month=12,
    day=24,
    days_of_week=(MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY),
    start_date=pd.Timestamp("2010-01-01"),
)

Christmas = christmas()

WeekendChristmas = weekend_christmas()

BoxingDay = boxing_day()

WeekendBoxingDay = weekend_boxing_day()

September11ClosingsCanada = pd.date_range('2001-09-11', '2001-09-12', tz='UTC')

# XMOD Equity Derivatives Holiday Calendar
# ----------------------------------------

class XMOD_EQD_AbstractHolidayCalendar:

        regular = HolidayCalendar([
            CANewYearsDay,
            FamilyDay,
            GoodFriday,
            VictoriaDay,
            CanadaDay,
            CivicHoliday,
            LaborDay,
            CanadianThanksgiving,
            Christmas,
            WeekendChristmas,
            BoxingDay,
            WeekendBoxingDay
        ])
        
        adhoc = list(chain(
            September11ClosingsCanada
        ))
        
        early = HolidayCalendar([])

# XMOD Holiday Calendar
# ---------------------

