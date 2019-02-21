from datetime import time
from itertools import chain

from pandas.tseries.holiday import (
    GoodFriday,
    USPresidentsDay,
    USLaborDay,
    USThanksgivingDay
)
from pandas import Timestamp
from pytz import timezone

from trading_calendars import TradingCalendar
from trading_calendars.trading_calendar import HolidayCalendar
from trading_calendars.us_holidays import (
    USNewYearsDay,
    Christmas,
    USMartinLutherKingJrAfter1998,
    USMemorialDay,
    USIndependenceDay,
    USNationalDaysofMourning)

from .holiday_calendar_usbond import (
    USBOND_AbstractHolidayCalendar,
)

from .holiday_calendar_ukbank import (
    UKBANK_AbstractHolidayCalendar,
)

from .holiday_calendar_eubank import (
    EUBANK_AbstractHolidayCalendar,
)

class IFEUExchangeCalendar(TradingCalendar):
    """
    Exchange calendar for ICE EU.
    Open Time: 8pm, UK/London
    Close Time: 6pm, UK/London
    https://www.theice.com/publicdocs/futures/Trading_Schedule_Migrated_Liffe_Contracts.pdf # noqa
    """
    product_group = 'UKBANK' # UK, US, EU
    regular_early_close = time(13)

    name = 'IFEU'

    tz = timezone("Europe/London")

    open_times = (
        (None, time(8, 1)),
    )

    close_times = (
        (None, time(18)),
    )

    @property
    def adhoc_holidays(self):
        if self.product_group == 'UKBANK':
            return list(chain(
                USNationalDaysofMourning,
                # ICE was only closed on the first day of the Hurricane Sandy
                # closings (was not closed on 2012-10-30)
                [Timestamp('2012-10-29', tz='UTC'),
                Timestamp('1999-12-31', tz='UTC'),
                Timestamp('2011-12-28', tz='UTC'),
                Timestamp('2016-06-28', tz='UTC'),],
                UKBANK_AbstractHolidayCalendar.regular_adhoc,
            ))
        elif self.product_group == 'US':
            return list(chain(
                USNationalDaysofMourning,
                # ICE was only closed on the first day of the Hurricane Sandy
                # closings (was not closed on 2012-10-30)
                [Timestamp('2012-10-29', tz='UTC')],
                USBOND_AbstractHolidayCalendar.regular_adhoc,
            ))
        elif self.product_group == 'EU':
            return list(chain(
                USNationalDaysofMourning,
                # ICE was only closed on the first day of the Hurricane Sandy
                # closings (was not closed on 2012-10-30)
                [Timestamp('2012-10-29', tz='UTC')],
                EUBANK_AbstractHolidayCalendar.regular_adhoc,
            ))

    @property
    def regular_holidays(self):
        # https://www.theice.com/publicdocs/futures_us/exchange_notices/NewExNot2016Holidays.pdf # noqa
        if self.product_group == 'UKBANK':
            return UKBANK_AbstractHolidayCalendar.regular
        elif self.product_group == 'US':
            return USBOND_AbstractHolidayCalendar.regular
        elif self.product_group == 'EU':
            return EUBANK_AbstractHolidayCalendar.regular
