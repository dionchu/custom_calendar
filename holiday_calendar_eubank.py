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

class EUBANK_AbstractHolidayCalendar:
    """
    Holiday calendar for the Eurosystem TARGET
    payment and settlement system.

    Regularly-Observed Holidays:
    - New Years Day
    - Good Friday
    - Easter Monday
    - Labour Day
    - Christmas Day
    - Boxing Day

    Ad-Hoc Closes:
    -  Dec. 31, 1999 to smooth transition to Y2K
    """
    
    regular = HolidayCalendar([
            NewYearsDay,
            GoodFriday,
            EasterMonday,
            EuropeanLabourDay,
            Christmas,
            BoxingDay,
        ])
 
    adhoc = [Timestamp('1999-12-31', tz='UTC')]

    early = HolidayCalendar([])
