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
from pandas import date_range, Timestamp
from itertools import chain
from pandas.tseries.offsets import CustomBusinessDay
from pandas.tseries.holiday import (
    USPresidentsDay,
    USLaborDay,
    USThanksgivingDay,
    GoodFriday,
    USColumbusDay,
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
    USNationalDaysofMourning,
    USMartinLutherKingJrAfter1995,
    USMemorialDay,
    USIndependenceDay,
    USVeteransDay,
    September11Closings,
)

EQDSeptember11Closings = September11Closings
IRDSeptember11Closings = date_range('2001-09-12', '2001-09-13', tz='UTC')
November12Closing2007 = [Timestamp('2007-11-12', tz='UTC'),
                         Timestamp('1992-04-14', tz='UTC'),
                         Timestamp('2001-11-12', tz='UTC')]

class XCMEExchangeCalendar(TradingCalendar):
    """
    Exchange calendar for the Chicago Mercantile Exchange (CMES).

    Open Time: 5:00 PM, America/Chicago
    Close Time: 5:00 PM, America/Chicago

    Regularly-Observed Holidays:
    - New Years Day
    - Good Friday
    - Christmas
    """
#    def __init__(self):
#        super(XCMEExchangeCalendar,self).__init__(start=Timestamp('1990-01-01', tz='UTC'),end=Timestamp('today', tz='UTC'))

    product_group = 'IRD' # 'EQD' 'METALS' 'SOFTS'
    regular_early_close = time(12)
    regular_open = time(17, 1)
    regular_close = time(17)

    name = 'XCME'

    tz = timezone('America/Chicago')

    open_times = (
        (None, time(17, 1)),
    )

    close_times = (
        (None, time(16)),
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

        # For now, we will treat the CME as having a single calendar, and just
        # go with the most conservative hours - and treat July 4 as an early
        # close at noon.
        if self.product_group == 'IRD':
            return HolidayCalendar([
                USMartinLutherKingJrAfter1995,
                USNewYearsDay,
                USPresidentsDay,
                GoodFriday,
                USMemorialDay,
                USColumbusDay,
                USLaborDay,
                USIndependenceDay,
                USThanksgivingDay,
                Christmas,
                USVeteransDay,
            ])
        if self.product_group == 'EQD':
            return HolidayCalendar([
                USMartinLutherKingJrAfter1995,
                USNewYearsDay,
                USPresidentsDay,
                GoodFriday,
                USMemorialDay,
                USColumbusDay,
                USLaborDay,
                USIndependenceDay,
                USThanksgivingDay,
                Christmas,
                USVeteransDay,
            ])
        if self.product_group == 'ENERGY':
            return HolidayCalendar([
                USNewYearsDay,
                GoodFriday,
                USThanksgivingDay,
                Christmas,
            ])


    @property
    def adhoc_holidays(self):
        if self.product_group == 'EQD':
            return list(chain(USNationalDaysofMourning,
                              EQDSeptember11Closings,
                              November12Closing2007
            ))
        if self.product_group == 'IRD':
            return list(chain(USNationalDaysofMourning,
                              IRDSeptember11Closings,
                              November12Closing2007
            ))
        if self.product_group == 'ENERGY':
            return list(chain(USNationalDaysofMourning,
                              IRDSeptember11Closings,
                              November12Closing2007
            ))

    @property
    def special_closes(self):
        if self.product_group == 'IRD':
            return [(
                self.regular_early_close,
                HolidayCalendar([
    #                USMartinLutherKingJrAfter1998,
    #                USPresidentsDay,
    #                USMemorialDay,
    #                USLaborDay,
    #                USIndependenceDay,
    #                USThanksgivingDay,
                    USBlackFridayInOrAfter1993,
                    ChristmasEveBefore1993,
                    ChristmasEveInOrAfter1993,
                ])
            )]
        if self.product_group == 'EQD':
            return [(
                self.regular_early_close,
                HolidayCalendar([
                    USMartinLutherKingJrAfter1998,
                    USPresidentsDay,
                    USMemorialDay,
                    USLaborDay,
                    USIndependenceDay,
                    USThanksgivingDay,
                    USBlackFridayInOrAfter1993,
                    ChristmasEveBefore1993,
                    ChristmasEveInOrAfter1993,
                ])
            )]
        if self.product_group == 'ENERGY':
            return [(
                self.regular_early_close,
                HolidayCalendar([
                    USMartinLutherKingJrAfter1998,
                    USPresidentsDay,
                    USMemorialDay,
                    USLaborDay,
                    USIndependenceDay,
                    USBlackFridayInOrAfter1993,
                    ChristmasEveBefore1993,
                    ChristmasEveInOrAfter1993,
                ])
            )]

    @property
    def day(self):
        return CustomBusinessDay(
            holidays=self.adhoc_holidays,
            calendar=self.regular_holidays,
            weekmask=self.weekmask,
        )
