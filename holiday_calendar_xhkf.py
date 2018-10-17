#test
import pandas as pd
from trading_calendars.offset_extensions import (
    next_spring_festival,
    next_buddha_birthday,
    next_dragon_boat_festival,
    next_mid_autumn_festival,
    next_double_nine_festival,
    next_spring_equinox,
    next_summer_solstice,
)

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
