from datetime import time
from itertools import chain
import pandas as pd
from pytz import timezone

from .holiday_calendar_xmod import (
    XMOD_IRD_AbstractHolidayCalendar,
    XMOD_EQD_AbstractHolidayCalendar,
)

from .trading_calendar import (
    TradingCalendar,
    HolidayCalendar,
    MONDAY,
    TUESDAY,
    WEDNESDAY,
    THURSDAY,
    FRIDAY,
)

class XMODExchangeCalendar(TradingCalendar):
    """
    Exchange calendar for the Montreal Exchange (XMOD).
    Open Time: 9:30 AM, EST
    Close Time: 4:30 PM, EST
    Regularly-Observed Holidays:
    - New Years Day (observed on first business day on/after)
    - Family Day (Third Monday in February, starting in 2008)
    - Good Friday
    - Victoria Day (Monday before May 25th)
    - Canada Day (July 1st, observed first business day after)
    - Civic Holiday (First Monday in August)
    - Labor Day (First Monday in September)
    - Thanksgiving (Second Monday in October)
    - Christmas Day
        - Dec. 26th if Chrismas is on a Sunday
        - Dec. 27th if Christmas is on a weekend
    - Boxing Day
        - Dec. 27th if Christmas is on a Sunday
        - Dec. 28th if Boxing Day is on a weekend
    Early closes:
    - IRD observe early close at 13:30 before every holiday
    - EQD does not observe early close
    """
    product_group = 'EQD' # EQD or IRD
    eqd_regular_open = time(9, 31)
    eqd_regular_close = time(16, 30)
    ird_regular_early_close = time(13, 30)
    ird_regular_open = time(2, 1)
    ird_regular_close = time(16, 30)
        
    @property
    def name(self):
        return "XMOD"

    @property
    def tz(self):
        return timezone('Canada/Atlantic')

    @property
    def open_time(self):
        if self.product_group == 'EQD':
            return self.eqd_regular_open
        elif self.product_group == 'IRD':
            return self.ird_regular_open

    @property
    def close_time(self):
        if self.product_group == 'EQD':
            return self.eqd_regular_close
        elif self.product_group == 'IRD':
            return self.ird_regular_close

    @property
    def regular_holidays(self):
        return XMOD_EQD_AbstractHolidayCalendar.regular if self.product_group == 'EQD' else XMOD_IRD_AbstractHolidayCalendar.regular

    @property
    def adhoc_holidays(self):
        # NOTE: change the name of this property
        return XMOD_EQD_AbstractHolidayCalendar.adhoc if self.product_group == 'EQD' else XMOD_IRD_AbstractHolidayCalendar.adhoc

    @property
    def special_closes(self):
        return [(self.ird_regular_early_close, XMOD_IRD_AbstractHolidayCalendar.early)] if self.product_group == 'IRD' else []
