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

from pytz import timezone

# Useful resources for making changes to this file:
# https://www.sifma.org/resources/general/holiday-schedule/

SIFMAUSNewYearsEve= Holiday(
    'New Years Day',
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

BusinessDayPriorToUSMartinLutherKingJrBefore2010 = Holiday(
    'Dr. Martin Luther King Jr. Day',
    month=1,
    day=1,
    # MLK day signed into law in 1983, not observed until 1986.
    start_date=Timestamp('1986-01-01'),
    end_date=Timestamp('2010-01-01'),
    offset=[DateOffset(weekday=MO(3)),pd.DateOffset(-3)],
)

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

# If July 4th is on a weekday or Sunday, prior workday is an early close
# If July 4th is a Saturday Thursday 2nd is an early close
# If July 4th is a Sunday Friday 2nd is an early close

def july_4th_early_close_observance(datetime_index):
    return datetime_index[~datetime_index.year.isin([2009,2010,2011,2012,2013])]

EarlyCloseIndependenceDayExcept2009to2013 = Holiday(
    'July 4th Early Close',
    month=7,
    day=3,
    days_of_week=(MONDAY, TUESDAY, WEDNESDAY, THURSDAY),
    observance = july_4th_early_close_observance
)
EarlyCloseWeekendIndependenceDayExcept2009to2013 = Holiday(
    'Weekend July 4th Early Close',
    month=7,
    day=2,
    days_of_week=(THURSDAY,FRIDAY),  
    observance = july_4th_early_close_observance
)

FridayBeforeLaborDayBefore2009 = Holiday(
    'Early Close Friday Before Labor Day'
    month=9,
    day=1,
    offset=[pd.DateOffset(weekday=MO(1)),pd.DateOffset(-3)],
    end_date=Timestamp('2009-01-01'),
)

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
    end_date=Timestamp('1993-01-01'),
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

# SIFMA will occasionally trade half days on Good Friday,
# because the holidays function cannot handle both offsers
# and observance rules, we list them out here individually,
# omitting those that markets were open for half days

SIFMAGoodFriday = [
  Timestamp('1971-04-09'),
  Timestamp('1972-03-31'),
  Timestamp('1973-04-20'),
  Timestamp('1974-04-12'),
  Timestamp('1975-03-28'),
  Timestamp('1976-04-16'),
  Timestamp('1977-04-08'),
  Timestamp('1978-03-24'),
  Timestamp('1979-04-13'),
  Timestamp('1980-04-04'),
  Timestamp('1981-04-17'),
  Timestamp('1982-04-09'),
  Timestamp('1983-04-01'),
  Timestamp('1984-04-20'),
  Timestamp('1985-04-05'),
  Timestamp('1986-03-28'),
  Timestamp('1987-04-17'),
  Timestamp('1988-04-01'),
  Timestamp('1989-03-24'),
  Timestamp('1990-04-13'),
  Timestamp('1991-03-29'),
  Timestamp('1992-04-17'),
  Timestamp('1993-04-09'),
  Timestamp('1994-04-01'),
  Timestamp('1995-04-14'),
  Timestamp('1996-04-05'),
  Timestamp('1997-03-28'),
  Timestamp('1998-04-10'),
#  Timestamp('1999-04-02'),
  Timestamp('2000-04-21'),
  Timestamp('2001-04-13'),
  Timestamp('2002-03-29'),
  Timestamp('2003-04-18'),
  Timestamp('2004-04-09'),
  Timestamp('2005-03-25'),
  Timestamp('2006-04-14'),
 # Timestamp('2007-04-06'),
  Timestamp('2008-03-21'),
  Timestamp('2009-04-10'),
 # Timestamp('2010-04-02'),
  Timestamp('2011-04-22'),
 # Timestamp('2012-04-06'),
  Timestamp('2013-03-29'),
  Timestamp('2014-04-18'),
#  Timestamp('2015-04-03'),
  Timestamp('2016-03-25'),
  Timestamp('2017-04-14'),
  Timestamp('2018-03-30'),
  Timestamp('2019-04-19'),
  Timestamp('2020-04-10'),
  Timestamp('2021-04-02'),
  Timestamp('2022-04-15'),
  Timestamp('2023-04-07'),
  Timestamp('2024-03-29'),
  Timestamp('2025-04-18'),
  Timestamp('2026-04-03'),
  Timestamp('2027-03-26'),
  Timestamp('2028-04-14'),
  Timestamp('2029-03-30'),
  Timestamp('2030-04-19'),
]

SIFMAGoodFridayEarlyClose = [
    Timestamp('1971-04-08'),
    Timestamp('1972-03-30'),
    Timestamp('1973-04-19'),
    Timestamp('1974-04-11'),
    Timestamp('1975-03-27'),
    Timestamp('1976-04-15'),
    Timestamp('1977-04-07'),
    Timestamp('1978-03-23'),
    Timestamp('1979-04-12'),
    Timestamp('1980-04-03'),
    Timestamp('1981-04-16'),
    Timestamp('1982-04-08'),
    Timestamp('1983-03-31'),
    Timestamp('1984-04-19'),
    Timestamp('1985-04-04'),
    Timestamp('1986-03-27'),
    Timestamp('1987-04-16'),
    Timestamp('1988-03-31'),
    Timestamp('1989-03-23'),
    Timestamp('1990-04-12'),
    Timestamp('1991-03-28'),
    Timestamp('1992-04-16'),
    Timestamp('1993-04-08'),
    Timestamp('1994-03-31'),
    Timestamp('1995-04-13'),
#    Timestamp('1996-04-04'),
    Timestamp('1997-03-27'),
    Timestamp('1998-04-09'),
    Timestamp('1999-04-01'),
    Timestamp('2000-04-20'),
    Timestamp('2001-04-12'),
    Timestamp('2002-03-28'),
    Timestamp('2003-04-17'),
    Timestamp('2004-04-08'),
    Timestamp('2005-03-24'),
    Timestamp('2006-04-13'),
#    Timestamp('2007-04-05'),
    Timestamp('2008-03-20'),
    Timestamp('2009-04-09'),
#    Timestamp('2010-04-01'),
    Timestamp('2011-04-21'),
#    Timestamp('2012-04-05'),
    Timestamp('2013-03-28'),
    Timestamp('2014-04-17'),
#    Timestamp('2015-04-02'),
    Timestamp('2016-03-24'),
    Timestamp('2017-04-13'),
    Timestamp('2018-03-29'),
    Timestamp('2019-04-18'),
    Timestamp('2020-04-09'),
    Timestamp('2021-04-01'),
    Timestamp('2022-04-14'),
    Timestamp('2023-04-06'),
    Timestamp('2024-03-28'),
    Timestamp('2025-04-17'),
    Timestamp('2026-04-02'),
    Timestamp('2027-03-25'),
    Timestamp('2028-04-13'),
    Timestamp('2029-03-29'),
    Timestamp('2030-04-18'),
]

# SIFMA US Bond Market Holiday Calendar
# -------------------------------------

class SIFMA_US_AbstractHolidayCalendar:

        regular = HolidayCalendar([
          USNewYearsDay,
          USMartinLutherKingJrAfter1986,
          USPresidentsDay,
          USMemorialDay,
          USIndependenceDay,
          USLaborDay,
          USColumbusDay,
          USThanksgivingDay,
          Christmas,
        ])
        
        regular_adhoc = list(chain(
            SIFMAGoodFriday,
            SIFMAHurricaneSandyClose,
            ReaganMourning,
        ))
        
        early = HolidayCalendar([
            SIFMAUSNewYearsEve,
            BusinessDayPriorToUSMartinLutherKingJrBefore2010,
            BusinessDayPriorToUSPresidentsDayBefore2010,
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
            SIFMAGoodFridayEarlyClose,
            SIFMABoxingDay1997,
            SIFMAHurricaneSandyEarlyClose,
        ])
