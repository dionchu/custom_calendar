import pandas as pd
from datetime import time
from pandas import (
    Timestamp,
    DateOffset,
)
from pytz import timezone
from pandas.tseries.holiday import (
    Holiday,
    DateOffset,
    MO,
    TU,
    WE,
    TH,
    FR,
    SA,
    SU,
    nearest_workday,
    weekend_to_monday,
    sunday_to_monday,
    previous_friday,
    previous_workday,
    GoodFriday,
    Easter,
    EasterMonday
)
from trading_calendar import (
    MONDAY,
    TUESDAY,
    WEDNESDAY,
    THURSDAY,
    FRIDAY,
    SATURDAY,
    SUNDAY,
    HolidayCalendar
)
from .offset_extensions import (
    next_spring_festival,
    next_buddha_birthday,
    next_dragon_boat_festival,
    next_mid_autumn_festival,
    next_double_nine_festival,
    next_spring_equinox,
    next_summer_solstice,
)

from .holiday_extensions import sunday_to_tuesday

# BEGIN LUNAR HOLIDAYS
SummerSolsticeFriday = HolidayWithFilter(
    'Sweden Summer Solstice Friday',
    month=1,
    day=1,
    offset=[next_summer_solstice(observance=friday_week_of)],
    year_filter = [2010]
)

SpringFestival = HolidayWithFilter(
    'Spring Festival',
    month=1,
    day=1,
    offset=[next_spring_festival(observance=sunday_to_wednesday)],
    year_filter = [2010]
)

SpringFestival2 = Holiday(
    'Spring Festival Second Day',
    month=1,
    day=1,
    offset=[next_spring_festival(offset=1,observance=sunday_to_tuesday)]
)

SpringFestival3 = Holiday(
    'Spring Festival Third Day',
    month=1,
    day=1,
    offset=[next_spring_festival(offset=1,observance=sunday_to_wednesday)]
)

QingMingFestival = HolidayWithFilter(
    'Qing Ming Festival',
    month=1,
    day=1,
    offset=[next_spring_equinox(offset=15,observance=sunday_to_monday)],
    year_filter = [2010],
)

BuddhasBirthday = Holiday(
    'Buddhas Birthday',
    month=1,
    day=1,
    offset=[next_buddha_birthday(observance=sunday_to_monday)]
)

DragonBoatFestival = Holiday(
    'Dragon Boat Festival',
    month=1,
    day=1,
    offset=[next_dragon_boat_festival(observance=sunday_to_monday)]
)

DayAfterMidAutumnFestival = Holiday(
    'Day After Mid Autumn Festival',
    month=1,
    day=1,
    offset=[next_mid_autumn_festival(offset=1, observance=sunday_to_monday)]
)

DoubleNineFestival = Holiday(
    'Double Nine Festival',
    month=1,
    day=1,
    offset=[next_double_nine_festival(observance=sunday_to_monday)]
)
# END LUNAR HOLIDAYS
# BEGIN NON-LUNAR HOLIDAYS

# New Year's Day: Jan 1, sunday_to_monday
NewYearsDay = new_years_day(observance=sunday_to_monday)

# Good Friday, Easter, and Easter Monday imported from pandas.

# Labor Day: May 1, sunday_to_monday
LaborDay = european_labour_day(observance=sunday_to_monday)

# US Memorial Day imported above.

# HK SAR Day: July 1, sunday_to_monday
HKSARDay = Holiday(
        'HK SAR Establishment Day',
        month=7,
        day=1,
        start_date='1997-07-01',
        observance=sunday_to_monday,
    )

# National Day: Oct. 1, sunday_to_monday
PRCNationalDay = Holiday(
        'PRC National Day',
        month=10,
        day=1,
        start_date='1997-07-01',
        observance=sunday_to_monday,
)

# Christmas Eve
ChristmasEve = christmas_eve(days_of_week=(MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY))

# Christmas Day
Christmas = christmas(observance=sunday_to_tuesday)

# Boxing Day
BoxingDay = boxing_day(observance=sunday_to_monday)

# New Year's Eve
NewYearsEve = new_years_eve(days_of_week=(MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY))

# END NON-LUNAR HOLIDAYS
# BEGIN AD HOC HOLIDAYS

# 9/3/2015: 70th anniversary of Japanese loss
HKJapaneseLoss20150903 = [
    Timestamp('2015-09-03', tz='UTC'), # Should this be UTC?
]

# 8/23/2017: Typhoon (https://www.hkex.com.hk/news/news-release/2017/1708232news?sc_lang=en)
Typhoon20170823 = [
    Timestamp('2017-08-23', tz='UTC'), # Should this be UTC?
]

# 7/2/1997 Day after HK SAR Day--appears to be one-off statutory holiday for 1997
HKSAR19970702 = [
    Timestamp('1997-07-02', tz='UTC'), # Should this be UTC?
]
