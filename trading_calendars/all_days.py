from datetime import time
from pytz import timezone

from pandas.tseries.offsets import CustomBusinessDay
from .trading_calendar import HolidayCalendar, TradingCalendar

class AllDaysCalendar(TradingCalendar):
    """
    All business days.
    """
    name = 'ALL'

    tz = timezone('US/Eastern')

    @property
    def open_offset(self):
        return -1

    open_times = (
        (None, time(18, 1)),
    )

    close_times = (
        (None, time(17)),
    )
