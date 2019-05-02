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
from itertools import chain
from pandas.tseries.holiday import (
    Holiday,
    GoodFriday,
    Easter,
    EasterMonday,
    DateOffset,
    FR,
)
from pandas.tseries.offsets import Day
from pytz import timezone

from .extensions.holiday_extensions import (
    friday_week_of,
    HolidayWithFilter,
)

from .common_holidays import (
    new_years_day,
    epiphany,
    maundy_thursday,
    ascension_day,
    whit_monday,
    european_labour_day,
    midsummer_eve,
    christmas_eve,
    christmas,
    boxing_day,
    new_years_eve,
)
from .trading_calendar import HolidayCalendar, TradingCalendar, WEEKDAYS

NewYearsDay = new_years_day()

DayBeforeEpiphany = HolidayWithFilter(
    'Day Before Epiphany',
    month=1,
    day=5,
    days_of_week=WEEKDAYS,
    year_filter = [2006],
)

Epiphany = epiphany()

DayBeforeLabourDay = Holiday(
    'Day Before Labour Day',
    month=4,
    day=30,
    days_of_week=WEEKDAYS,
)
LabourDay = european_labour_day()

MaundyThursday = maundy_thursday(days_of_week=WEEKDAYS)
DayBeforeAscensionDay = Holiday(
    'Day Before Ascension Day',
    month=1,
    day=1,
    offset=[Easter(), Day(38)],
)
AscensionDay = ascension_day()
WhitMonday = whit_monday(end_date='2005')

NationalDay = Holiday('Sweden National Day', month=6, day=6, start_date='2004')

MidsummerEve = midsummer_eve()

# This falls on the Friday between October 30th and November 5th.
AllSaintsEve = Holiday(
    "All Saints' Eve",
    month=10,
    day=30,
    offset=DateOffset(weekday=FR(1)),
)

RandomClosings = [Timestamp('2006-01-05', tz='UTC'),
                  Timestamp('2005-02-11', tz='UTC'),
                  Timestamp('2005-02-10', tz='UTC')
                    ]

ChristmasEve = christmas_eve()
Christmas = christmas()
BoxingDay = boxing_day()

NewYearsEve = new_years_eve()

class XSTOExchangeCalendar(TradingCalendar):
    """
    Calendar for the Stockholm Stock Exchange in Sweden.
    Open Time: 9:00 AM, CET (Central European Time)
    Close Time: 5:30 PM, CET (Central European Time)
    Regularly-Observed Holidays:
      - New Year's Day
      - Epiphany
      - Good Friday
      - Easter Monday
      - Labour Day
      - Ascension Day
      - National Day
      - Midsummer Eve
      - Christmas Eve
      - Christmas Day
      - Boxing Day
      - New Year's Eve
    Holidays No Longer Observed:
      - Whit Monday
    Early Closes:
      - Day before Epiphany
      - Maundy Thursday
      - Day before Labour Day
      - Day before Ascension Day
      - All Saints' Eve
    """
    name = 'XSTO'
    tz = timezone('Europe/Stockholm')
    open_times = (
        (None, time(9, 1)),
    )
    close_times = (
        (None, time(17, 30)),
    )
    regular_early_close = time(13)

    @property
    def regular_holidays(self):
        return HolidayCalendar([
            NewYearsDay,
            Epiphany,
            GoodFriday,
            EasterMonday,
            LabourDay,
            AscensionDay,
            WhitMonday,
            NationalDay,
            MidsummerEve,
            ChristmasEve,
            Christmas,
            BoxingDay,
            NewYearsEve,
        ])

    @property
    def adhoc_holidays(self):
            return list(chain(
                              RandomClosings,
            ))

    @property
    def special_closes(self):
        return [
            (
                self.regular_early_close,
                HolidayCalendar([
                    DayBeforeEpiphany,
                    MaundyThursday,
                    DayBeforeLabourDay,
                    DayBeforeAscensionDay,
                    AllSaintsEve,
                ]),
            ),
        ]
