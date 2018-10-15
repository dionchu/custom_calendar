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
    EasterMonday,
    GoodFriday,
    Holiday,
    previous_workday
)
from pytz import timezone

from .common_holidays import (
    new_years_day,
    european_labour_day,
    whit_monday,
    christmas_eve,
    christmas,
    boxing_day,
    new_years_eve,

)
from .trading_calendar import (
    TradingCalendar,
    HolidayCalendar
)

# Regular Holidays
# ----------------
NewYearsDay = new_years_day()

EuropeanLabourDay = european_labour_day()

Christmas = christmas()

BoxingDay = boxing_day()

# Early Closes
# ------------
# The last weekday before Dec 31 is an early close starting in 2010.
LastWorkingDay = Holiday(
    "Last Working Day of Year Early Close",
    month=12,
    day=31,
    start_date='2010-01-01',
    observance=previous_workday,
)

class UKBANK_AbstractHolidayCalendar:
    
    regular = HolidayCalendar([
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
 
    adhoc = [
            SpringBank2002,
            GoldenJubilee,
            RoyalWedding,
            SpringBank2012,
            DiamondJubilee,
        ]

    early = HolidayCalendar([])
