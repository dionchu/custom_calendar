from datetime import time
from itertools import chain
from pandas.tseries.offsets import CustomBusinessDay

from pandas.tseries.holiday import (
    EasterMonday,
    GoodFriday,
    USPresidentsDay,
    USLaborDay,
    USThanksgivingDay
)
from pandas import Timestamp
from pytz import timezone

from trading_calendars import TradingCalendar
from trading_calendars.trading_calendar import HolidayCalendar

from .common_holidays import (
    new_years_day,
    european_labour_day,
    whit_monday,
    christmas_eve,
    christmas,
    boxing_day,
    new_years_eve,

)

from .holiday_calendar_eubank import (
NewYearsDay,
EuropeanLabourDay,
Christmas,
BoxingDay,
)

ChristmasEve = christmas_eve()
NewYearsEve = new_years_eve()

EUBANKClosings = [Timestamp('1999-05-13', tz='UTC'),
                         Timestamp('1999-05-24', tz='UTC'),
                         Timestamp('1999-06-03', tz='UTC'),
                         Timestamp('2007-05-28', tz='UTC'),
                         Timestamp('2015-05-25', tz='UTC')]

class XEURExchangeCalendar(TradingCalendar):
    """
    Exchange calendar for EUREX.
    """
    product_group = 'EUBANK' # UK, US, EU
    regular_early_close = time(13)

    name = 'XEUR'

    tz = timezone('Europe/Berlin')

    open_times = (
        (None, time(8, 1)),
    )

    close_times = (
        (None, time(17,15)),
    )


    @property
    def adhoc_holidays(self):
        if self.product_group == 'EUBANK':
            return EUBANKClosings

    @property
    def regular_holidays(self):
        if self.product_group == 'EUBANK':
            return HolidayCalendar([
                    NewYearsDay,
                    GoodFriday,
                    EasterMonday,
                    EuropeanLabourDay,
                    ChristmasEve,
                    Christmas,
                    BoxingDay,
                    NewYearsEve,
                ])

    @property
    def day(self):
        return CustomBusinessDay(
            holidays=self.adhoc_holidays,        
            calendar=self.regular_holidays,
            weekmask=self.weekmask,
        )
