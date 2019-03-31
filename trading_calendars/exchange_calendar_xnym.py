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
from itertools import chain
from pandas import date_range, Timestamp
from pandas.tseries.offsets import CustomBusinessDay

from pandas.tseries.holiday import (
    USPresidentsDay,
    USLaborDay,
    USThanksgivingDay,
    GoodFriday
)
from pytz import timezone

# Useful resources for making changes to this file:
# http://www.cmegroup.com/tools-information/holiday-calendar.html

from .trading_calendar import TradingCalendar, HolidayCalendar
from .us_holidays import (
    USNewYearsDay,
    Christmas,
    ChristmasEveBefore1993,
    ChristmasEveInOrAfter1993,
    USBlackFridayInOrAfter1993,
    USBlackFriday1993to2006,
    NYMUSNationalDaysofMourning,
    USMartinLutherKingJrAfter1998,
    USMemorialDay,
    USIndependenceDay
)



September11Closings = date_range('2001-09-11','2001-09-13', tz='UTC')
IndependenceDayClosings = [Timestamp('1995-07-03', tz='UTC'),
                         Timestamp('1996-07-05', tz='UTC'),
                         Timestamp('2000-07-03', tz='UTC'),
                         Timestamp('2002-07-05', tz='UTC'),
                         Timestamp('2006-07-03', tz='UTC')]

RandomClosings = [Timestamp('1993-12-31', tz='UTC'),
                Timestamp('1996-01-08', tz='UTC'),
                Timestamp('1999-12-31', tz='UTC'),
                Timestamp('2000-01-03', tz='UTC'),
                Timestamp('2001-12-24', tz='UTC'),
                Timestamp('2003-12-26', tz='UTC'),
                Timestamp('2004-01-02', tz='UTC'),
                Timestamp('2004-12-31', tz='UTC')]

RandomClosings12Month = [Timestamp('1993-12-31', tz='UTC'),
                Timestamp('1996-01-08', tz='UTC'),
                Timestamp('1999-12-31', tz='UTC'),
                Timestamp('2000-01-03', tz='UTC'),
                Timestamp('2001-12-24', tz='UTC'),
                Timestamp('2002-07-03', tz='UTC'),
                Timestamp('2003-12-26', tz='UTC'),
                Timestamp('2004-01-02', tz='UTC'),
                Timestamp('2004-12-31', tz='UTC'),
                Timestamp('2014-04-08', tz='UTC')]

MetalsSeptember11Closings = date_range('2001-09-11','2001-09-14', tz='UTC')
MetalsRandomClosings = [Timestamp('1999-12-31', tz='UTC'),
                        Timestamp('2000-01-03', tz='UTC'),
                        Timestamp('2000-07-03', tz='UTC'),
                        Timestamp('2001-12-24', tz='UTC'),
                        Timestamp('2002-07-05', tz='UTC'),
                        Timestamp('2003-12-26', tz='UTC'),
                        Timestamp('2004-01-02', tz='UTC'),
                        Timestamp('2004-12-31', tz='UTC')]

MetalsRandomClosings12Month = [Timestamp('1999-12-31', tz='UTC'),
                        Timestamp('2000-01-03', tz='UTC'),
                        Timestamp('2000-07-03', tz='UTC'),
                        Timestamp('2001-12-24', tz='UTC'),
                        Timestamp('2002-07-05', tz='UTC'),
                        Timestamp('2003-12-26', tz='UTC'),
                        Timestamp('2004-01-02', tz='UTC'),
                        Timestamp('2004-12-31', tz='UTC'),
                        Timestamp('2006-07-03', tz='UTC')]

class XNYMExchangeCalendar(TradingCalendar):
    """
    Exchange calendar for the New York Mercantile Exchange (NYMEX).
    Open Time: 5:00 PM, America/New_York
    Close Time: 5:00 PM, America/New_York
    Regularly-Observed Holidays:
    - New Years Day
    - Good Friday
    - Christmas
    """
    product_group = 'ENERGY' # UK, US, EU
    regular_early_close = time(12)

    name = 'XNYM'

    tz = timezone('America/New_York')

    open_times = (
        (None, time(17, 1)),
    )

    close_times = (
        (None, time(17)),
    )

    @property
    def open_offset(self):
        return -1

    @property
    def regular_holidays(self):
        # The CME has different holiday rules depending on the type of
        # instrument. For example, http://www.cmegroup.com/tools-information/holiday-calendar/files/2016-4th-of-july-holiday-schedule.pdf # noqa
        # shows that Equity, Interest Rate, FX, Energy, Metals & DME Products
        # close at 1200 CT on July 4, 2016, while Grain, Oilseed & MGEX
        # Products and Livestock, Dairy & Lumber products are completely
        # closed.

        # For now, we will treat the NYMEX as having a single calendar, and just
        # go with the most conservative hours - and treat July 4 as an early
        # close at noon.
        if self.product_group == 'ENERGY':
            return HolidayCalendar([
                USNewYearsDay,
                USMartinLutherKingJrAfter1998,
                USPresidentsDay,
                GoodFriday,
                USMemorialDay,
                USIndependenceDay,
                USLaborDay,
                USThanksgivingDay,
                USBlackFriday1993to2006,
                ChristmasEveBefore1993,
                Christmas,
            ])

        if self.product_group == 'ENERGY12':
            return HolidayCalendar([
                USNewYearsDay,
                USMartinLutherKingJrAfter1998,
                USPresidentsDay,
                GoodFriday,
                USMemorialDay,
                USIndependenceDay,
                USLaborDay,
                USThanksgivingDay,
                USBlackFriday1993to2006,
                ChristmasEveBefore1993,
                Christmas,
            ])

        if self.product_group == 'METALS':
            return HolidayCalendar([
                USNewYearsDay,
                USMartinLutherKingJrAfter1998,
                USPresidentsDay,
                GoodFriday,
                USMemorialDay,
                USIndependenceDay,
                USLaborDay,
                USThanksgivingDay,
                USBlackFriday1993to2006,
                ChristmasEveBefore1993,
                Christmas,
            ])

        if self.product_group == 'METALS12':
            return HolidayCalendar([
                USNewYearsDay,
                USMartinLutherKingJrAfter1998,
                USPresidentsDay,
                GoodFriday,
                USMemorialDay,
                USIndependenceDay,
                USLaborDay,
                USThanksgivingDay,
                USBlackFriday1993to2006,
                ChristmasEveBefore1993,
                Christmas,
            ])

    @property
    def adhoc_holidays(self):
        if self.product_group == 'ENERGY':
            return list(chain(NYMUSNationalDaysofMourning,
                              September11Closings,
                              IndependenceDayClosings,
                              RandomClosings,
            ))
        if self.product_group == 'ENERGY12':
            return list(chain(NYMUSNationalDaysofMourning,
                              September11Closings,
                              IndependenceDayClosings,
                              RandomClosings12Month,
            ))
        if self.product_group == 'METALS':
            return list(chain(NYMUSNationalDaysofMourning,
                              MetalsSeptember11Closings,
                              MetalsRandomClosings,
            ))
        if self.product_group == 'METALS12':
            return list(chain(NYMUSNationalDaysofMourning,
                              MetalsSeptember11Closings,
                              MetalsRandomClosings12Month,
            ))


#    @property
#    def special_closes(self):
#        return [(
#            self.regular_early_close,
#            HolidayCalendar([
#                USBlackFridayInOrAfter1993,
#                ChristmasEveInOrAfter1993,
#            ])
#        )]

    @property
    def day(self):
        return CustomBusinessDay(
            holidays=self.adhoc_holidays,
            calendar=self.regular_holidays,
            weekmask=self.weekmask,
        )
