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

#https://www.ecb.europa.eu/home/contacts/working-hours/html/index.en.html
from itertools import chain
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
    corpus_christi,
    ascension_day,
)
from .trading_calendar import (
    TradingCalendar,
    HolidayCalendar
)

# Regular Holidays
# ----------------
NewYearsDay = new_years_day()

EuropeanLabourDay = european_labour_day()

WhitMonday = whit_monday(start_date='2015-01-01')
WhitMonday90s = whit_monday(start_date = '1991-01-01', end_date = '2000-01-01')
CorpusChristi90s = corpus_christi(start_date = '1991-01-01', end_date = '2000-01-01')
Ascension90s = ascension_day(start_date = '1991-01-01', end_date = '2000-01-01')
DayOfGermanUnity90s = Holiday(
    "Day of German Unity",
    month=10,
    day=3,
    start_date='1991-01-01',
    end_date = '2001-01-01'
)

RepentanceDay = [Timestamp('1991-11-20'),
                         Timestamp('1992-11-18'),
                         Timestamp('1993-11-17'),
                         Timestamp('1994-11-16'),]

DayOfGermanUnity = Holiday(
    "Day of German Unity",
    month=10,
    day=3,
    start_date='2014-01-01'
)

Random = [Timestamp('1993-06-11'), Timestamp('1998-06-11')]

# Whit Monday observed in 2007, before it became regularly observed
# starting in 2015.
WhitMonday2007AdHoc = Timestamp('2007-05-28')

# Reformation Day was a German national holiday in 2017.
ReformationDay500thAnniversaryAdHoc = Timestamp('2017-10-31')

ChristmasEve = christmas_eve()

Christmas = christmas()

BoxingDay = boxing_day()

NewYearsEve = new_years_eve()

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

class XFRA_AbstractHolidayCalendar:
    """
    Holiday calendar for the Frankfurt Stock Exchange (XFRA).
    Open Time: 9:00 AM, CET
    Close Time: 5:30 PM, CET
    Regularly-Observed Holidays:
    - New Years Day
    - Good Friday
    - Easter Monday
    - Whit Monday
    - Labour Day
    - Day of German Unity
    - Christmas Eve
    - Christmas Day
    - Boxing Day
    Early Closes:
    - Last working day before Dec. 31
    """

    regular = HolidayCalendar([
            NewYearsDay,
            GoodFriday,
            EasterMonday,
            EuropeanLabourDay,
            WhitMonday,
            DayOfGermanUnity,
            ChristmasEve,
            Christmas,
            BoxingDay,
            NewYearsEve,
            CorpusChristi90s,
            WhitMonday90s,
            CorpusChristi90s,
            Ascension90s,
            DayOfGermanUnity90s,
        ])

    regular_adhoc = [
            WhitMonday2007AdHoc,
            ReformationDay500thAnniversaryAdHoc,
        ] + RepentanceDay + Random

    early = HolidayCalendar([
            LastWorkingDay,
    ])
