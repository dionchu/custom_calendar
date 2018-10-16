# US Bond Markets follow SIFMA US trading calendar
# https://www.sifma.org/resources/general/holiday-schedule/#US

#-------------------------------------------------------
# Latest verification 1996-2018

#-------------------------------------------------------
# To Do:
# Check MLK Day first observed in Federal Payment System

from datetime import time

from pandas import (
    Timestamp,
    DateOffset,
)

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
    USPresidentsDay,
    USLaborDay,
    USColumbusDay,
    USThanksgivingDay,
    GoodFriday
)

from .us_holidays import (
    USNewYearsDay,
    Christmas,
    ChristmasEveBefore1993,
    ChristmasEveInOrAfter1993,
    USBlackFridayInOrAfter1993,
    USNationalDaysofMourning,
    USMartinLutherKingJrAfter1998,
    USMemorialDay,
    USIndependenceDay,
    September11Closings,
    HurricaneSandyClosings,    
)

from .trading_calendar import (
    TradingCalendar,
    MONDAY,
    TUESDAY,
    WEDNESDAY,
    THURSDAY,
    FRIDAY,
    SATURDAY,
    SUNDAY,
    HolidayCalendar
)

from .extensions.holiday_extensions import (
    friday_week_of,
    HolidayWithFilter,
)

from pytz import timezone

# Useful resources for making changes to this file:
# https://www.sifma.org/resources/general/holiday-schedule/

SIFMAUSNewYearsEve= Holiday(
    'SIFMA New Years Eve',
    month=12,
    day=31,
    observance=previous_friday,
)

USMartinLutherKingJr = Holiday(
    'Dr. Martin Luther King Jr. Day',
    month=1,
    day=1,
    # MLK day signed into law in 1983, not observed until 1986.
    start_date=Timestamp('1986-01-01'),
    offset=DateOffset(weekday=MO(3)),
)

# SIFMA stopped observing early close for MLK after 2009
BusinessDayPriorToUSMartinLutherKingJrBefore2010 = Holiday(
    'Business Day prior to Dr. Martin Luther King Jr. Day',
    month=1,
    day=1,
    # MLK day signed into law in 1983, not observed until 1986.
    start_date=Timestamp('1986-01-01'),
    end_date=Timestamp('2010-01-01'),
    offset=[DateOffset(weekday=MO(3)),pd.DateOffset(-3)],
)

# SIFMA stopped observing early close for President's Day after 2009
BusinessDayPriorToUSPresidentsDayBefore2010 = Holiday(
    'Business Day prior to President's Day',
    month=2,
    day=1,
    offset=[DateOffset(weekday=MO(3)),pd.DateOffset(-3)],
    end_date=Timestamp('2010-01-01'),
)

BusinessDayPriorToMemorialDay = Holiday(
    'Business Day prior to Memorial Day', 
    month=5,
    day=25,
    offset=[DateOffset(weekday=MO(1)),pd.DateOffset(-3)],
)

# SIFMA occasionally does not recommend Good Friday full close
# instead it will stay open for a half day, in most cases
# the Thursday before will not be a half day
SIFMAGoodFriday = HolidayWithFilter(
    'SIFMA Good Friday', 
    month=1, 
    day=1, 
    offset=[Easter(), Day(-2)]),
    year_filter = [1999,2007,2010,2012,2015],
)

# SIFMA generally recommends early close day before Good Friday
# if Good Friday is closed
SIFMAMaundyThursday = HolidayWithFilter(
    'SIFMA Maundy Thursday early close', 
    month=1, 
    day=1, 
    offset=[Easter(), Day(-3)]),
    year_filter = [2007,2010,2012,2015],
)

# Where SIFMA does not recommend a full close on Good Friday,
# it is an early close
SIFMAGoodFridayEarlyClose = HolidayWithFilter(
    'SIFMA Good Friday', 
    month=1, 
    day=1, 
    offset=[Easter(), Day(-2)]),
    year_mask = [1999,2007,2010,2012,2015],
)

# If July 4th is on a weekday or Sunday, prior workday is an early close
# If July 4th is a Saturday Thursday 2nd is an early close
# If July 4th is a Sunday Friday 2nd is an early close

# SIFMA occasionally trades a full day before July 4th
# specifically, in 2009, 2010, 2011, 2012, and 2013
EarlyCloseIndependenceDayExcept2009to2013 = HolidayWithFilter(
    'July 4th Early Close',
    month=7,
    day=3,
    days_of_week=(MONDAY, TUESDAY, WEDNESDAY, THURSDAY),
    year_filter = [2009,2010,2011,2012,2013],
)

EarlyCloseWeekendIndependenceDayExcept2009to2013 = HolidayWithFilter(
    'Weekend July 4th Early Close',
    month=7,
    day=2,
    days_of_week=(THURSDAY,FRIDAY),  
    year_filter = [2009,2010,2011,2012,2013],
)

# SIFMA stopped observing early close for Labor Day after 2009
FridayBeforeLaborDayBefore2009 = Holiday(
    'Early Close Friday Before Labor Day'
    month=9,
    day=1,
    offset=[pd.DateOffset(weekday=MO(1)),pd.DateOffset(-3)],
    end_date=Timestamp('2009-01-01'),
)

# SIFMA stopped observing early close for Columbus Day after 2009
FridayBeforeColumbusDayBefore2009 = Holiday(
    'Early Close Friday Before Columbus Day'
    month=10,
    day=1,
    offset=[pd.DateOffset(weekday=MO(2)),pd.DateOffset(-3)],
    end_date=Timestamp('2009-01-01'),
)

WednesdayBeforeThanksgiving = Holiday(
    'Early Close Wednesday Before Thanksgiving Day'
    month=11,
    day=1,
    offset=[pd.DateOffset(weekday=TH(4)),pd.DateOffset(-1)],
)

# SIFMA stopped observing early close for Black Friday after 2009
BlackFridayBefore2009 = Holiday(
    'Early Close Wednesday Before Thanksgiving Day'
    month=11,
    day=1,
    offset=[pd.DateOffset(weekday=TH(4)),pd.DateOffset(1)],
    end_date=Timestamp('2009-01-01'),
)

ChristmasEve = Holiday(
    'Christmas Eve',
    month=12,
    day=24,
    observance=previous_friday,
)

# SIFMA recommended early market close
# - Random Boxing Day - December 26, 1997
# - Hurricane Sandy - October 29, 2012
# - President Gerald R. Ford - Jan 2, 2007

SIFMABoxingDay1997 = [
    Timestamp('1997-12-26', tz='UTC'),
]

SIFMAHurricaneSandyEarlyClose = [
    Timestamp('2012-10-29', tz='UTC'),
]

FordMourning = [
    Timestamp('2007-01-02', tz='UTC'),
]

# SIFMA recommended market close
# - Hurricane Sandy - October 30, 2012
# - President Ronald W. Reagan - June 11, 2004

SIFMAHurricaneSandyClose = [
    Timestamp('2012-10-30', tz='UTC'),
]

ReaganMourning = [
    Timestamp('2004-06-11', tz='UTC'),
]

# SIFMA US Bond Market Holiday Calendar
# -------------------------------------

class USBOND_AbstractHolidayCalendar:

        regular = HolidayCalendar([
          USNewYearsDay,
          USMartinLutherKingJrAfter1986,
          USPresidentsDay,
          SIFMAGoodFriday,
          USMemorialDay,
          USIndependenceDay,
          USLaborDay,
          USColumbusDay,
          USThanksgivingDay,
          Christmas,
        ])
        
        regular_adhoc = list(chain(
            SIFMAHurricaneSandyClose,
            ReaganMourning,
        ))
        
        early = HolidayCalendar([
            SIFMAUSNewYearsEve,
            BusinessDayPriorToUSMartinLutherKingJrBefore2010,
            BusinessDayPriorToUSPresidentsDayBefore2010,
            SIFMAMaundyThursday,
            SIFMAGoodFridayEarlyClose,
            BusinessDayPriorToMemorialDay,
            EarlyCloseIndependenceDayExcept2009to2013,
            EarlyCloseWeekendIndependenceDayExcept2009to2013,
            FridayBeforeLaborDayBefore2009,
            FridayBeforeColumbusDayBefore2009,
            WednesdayBeforeThanksgiving,
            BlackFridayBefore2009,
            ChristmasEve,
        ])
        
        early_adhoc = HolidayCalendar([
            SIFMABoxingDay1997,
            SIFMAHurricaneSandyEarlyClose,
        ])
