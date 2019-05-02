from datetime import time
from itertools import chain
from pandas.tseries.offsets import CustomBusinessDay

from pandas import Timestamp
from pytz import timezone

from trading_calendars import TradingCalendar
from trading_calendars.trading_calendar import HolidayCalendar

from .holiday_calendar_usbond import (
    USBOND_AbstractHolidayCalendar,
)

class USBONDExchangeCalendar(TradingCalendar):
    """
    Exchange calendar for USBOND.
    """
    product_group = 'USBOND' # UK, US, EU
    regular_early_close = time(13)

    name = 'USBOND'

    tz = timezone('America/New_York')

    open_times = (
        (None, time(17, 1)),
    )

    close_times = (
        (None, time(17)),
    )


    @property
    def adhoc_holidays(self):
        return USBOND_AbstractHolidayCalendar.regular_adhoc

    @property
    def regular_holidays(self):
        return USBOND_AbstractHolidayCalendar.regular

    @property
    def day(self):
        return CustomBusinessDay(
            holidays=self.adhoc_holidays,
            calendar=self.regular_holidays,
            weekmask=self.weekmask,
        )
