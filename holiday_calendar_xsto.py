# Stockholm OMX Holiday Calendar
# http://www.nasdaqomxnordic.com/vidskiptatimi
# Check against Federation of European Securities Exchanges: http://www.fese.eu/statistics-market-research/trading-calendar
# Cross check against NASDAQ http://www.nasdaqtrader.com/content/technicalsupport/dataproducts/GDPcombinedholidays.xls

#-------------------------------------------------------
# Latest verification 2007-2018

#-------------------------------------------------------
# To Do:
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
    all_saints_day,    
    christmas_eve,
    christmas,
    boxing_day,
    new_years_eve,
    summer_solstice_friday,
    maundy_thursday,
)

from .extensions.holiday_extensions import (
    friday_week_of,
    HolidayWithFilter,
)

from .extensions.offset_extensions import (
    next_summer_solstice,
)

NewYearsDay = new_years_day(days_of_week=(MONDAY,TUESDAY,WEDNESDAY,THURSDAY,FRIDAY))

# OMX Stockholm was open for full day in 2010
TwelfthNight = HolidayWithFilter(
    'Twelfth Night',
    month=1,
    day=5,
    days_of_week=(MONDAY,TUESDAY,WEDNESDAY,THURSDAY,FRIDAY),
    year_filter = [2010],
)

EpiphanyDay = epiphany(days_of_week=(MONDAY,TUESDAY,WEDNESDAY,THURSDAY,FRIDAY))

WalpurgisNight = Holiday(
    'Walpurgis Night',
    month=4,
    day=30,
    days_of_week=(MONDAY,TUESDAY,WEDNESDAY,THURSDAY,FRIDAY),
)

MaundyThursday = maundy_thursday()

EuropeanLabourDay = european_labour_day(days_of_week=(MONDAY,TUESDAY,WEDNESDAY,THURSDAY,FRIDAY))

# Nasdaq OMX Stockholm did not observe 2008 Ascension Day
XSTOAscensionDay = HolidayWithFilter(
    'XSTO observed Ascension Day',
    month=1,
    day=1,
    offset=[Easter(), Day(39)],
    year_filter = [2008],
)

SENationalDay = Holiday(
    "National Day of Sweden",
    month=6,
    day=6,
    days_of_week=(MONDAY,TUESDAY,WEDNESDAY,THURSDAY,FRIDAY),
)

SummerSolsticeFriday = Holiday(
    'Sweden Summer Solstice Friday',
    month=1,
    day=1,
    offset=[next_summer_solstice(observance=friday_week_of)],
)

AllSaintsEve = all_saints_day(observance=friday_week_of)

# Nasdaq OMX Stockholm did not observe early close on 2010 All Saints Friday
XSTOAllSaintsFriday = HolidayWithFilter(
    'XSTO observed All Saints Friday',
    month=11,
    day=1,
    observance=friday_week_of,
    year_filter = [2010],
)

ChristmasEve = christmas_eve(days_of_week=(MONDAY,TUESDAY,WEDNESDAY,THURSDAY,FRIDAY))

Christmas = christmas(days_of_week=(MONDAY,TUESDAY,WEDNESDAY,THURSDAY,FRIDAY))

BoxingDay = boxing_day(days_of_week=(MONDAY,TUESDAY,WEDNESDAY,THURSDAY,FRIDAY))

NewYearsEve = new_years_eve(days_of_week=(MONDAY,TUESDAY,WEDNESDAY,THURSDAY,FRIDAY))

# Nasdaq OMX Holiday Calendar
# -------------------------------------

class XSTO_AbstractHolidayCalendar:
    
        regular = HolidayCalendar([
          NewYearsDay,
          GoodFriday,
          EasterMonday,
          EuropeanLabourDay,
          XSTOAscensionDay,
          SENationalDay,
          SummerSolsticeFriday,
          ChristmasEve,
          Christmas,
          BoxingDay,
          NewYearsEve,
        ])
        
        regular_adhoc = []

        early = HolidayCalendar([
          TwelfthNight,
          MaundyThursday,
          WalpurgisNight,
          XSTOAllSaintsFriday,
        ])
