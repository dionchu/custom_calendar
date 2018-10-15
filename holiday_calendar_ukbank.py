#
# Copyright 2018 Quantopian, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from datetime import time
from pandas import Timestamp
from pandas.tseries.holiday import (
    DateOffset,
    EasterMonday,
    GoodFriday,
    Holiday,
    MO,
    previous_friday,
    weekend_to_monday,
)
from pytz import timezone

from .common_holidays import (
    new_years_day,
    christmas,
    weekend_christmas,
    boxing_day,
    weekend_boxing_day,
)
from .trading_calendar import (
    TradingCalendar,
    HolidayCalendar,
)

# Regular Holidays
# ----------------
# New Year's Day
UKNewYearsDay = new_years_day(observance=weekend_to_monday)

# Early May bank holiday
MayBank = Holiday(
    "Early May Bank Holiday",
    month=5,
    offset=DateOffset(weekday=MO(1)),
    day=1,
)
# Spring bank holiday is the last Monday in May except:
# - in 2002, it was moved to June 3
# - in 2012, it was moved to June 4
SpringBankBefore2002 = Holiday(
    "Spring Bank Holiday",
    month=5,
    day=31,
    offset=DateOffset(weekday=MO(-1)),
    end_date="2002-01-01",
)
SpringBank2002To2012 = Holiday(
    "Spring Bank Holiday",
    month=5,
    day=31,
    offset=DateOffset(weekday=MO(-1)),
    start_date="2003-01-01",
    end_date="2012-01-01",
)
SpringBank2013Onwards = Holiday(
    "Spring Bank Holiday",
    month=5,
    day=31,
    offset=DateOffset(weekday=MO(-1)),
    start_date="2013-01-01",
)
# Summer bank holiday
SummerBank = Holiday(
    "Summer Bank Holiday",
    month=8,
    day=31,
    offset=DateOffset(weekday=MO(-1)),
)

Christmas = christmas()

WeekendChristmas = weekend_christmas()

BoxingDay = boxing_day()

WeekendBoxingDay = weekend_boxing_day()

# Ad Hoc Closes
# -------------
SpringBank2002 = Timestamp("2002-06-03", tz="UTC")
GoldenJubilee = Timestamp("2002-06-04", tz="UTC")
RoyalWedding = Timestamp("2011-04-29", tz="UTC")
SpringBank2012 = Timestamp("2012-06-04", tz="UTC")
DiamondJubilee = Timestamp("2012-06-05", tz="UTC")

UKBANK_AbstractHolidayCalendar = HolidayCalendar([
            UKNewYearsDay,
            GoodFriday,
            EasterMonday,
            MayBank,
            SpringBankBefore2002,
            SpringBank2002To2012,
            SpringBank2013Onwards,
            SummerBank,
            Christmas,
            WeekendChristmas,
            BoxingDay,
            WeekendBoxingDay
        ])
 
 UKBANK_AdhocAbstractHolidayCalendar = [
            SpringBank2002,
            GoldenJubilee,
            RoyalWedding,
            SpringBank2012,
            DiamondJubilee,
        ]
