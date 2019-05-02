from datetime import time
from itertools import chain

from pandas.tseries.holiday import (
    GoodFriday,
    USPresidentsDay,
    USLaborDay,
    USThanksgivingDay
)
from pandas import Timestamp, date_range
from pytz import timezone
from pandas.tseries.offsets import CustomBusinessDay

from trading_calendars import TradingCalendar
from trading_calendars.trading_calendar import HolidayCalendar
from trading_calendars.us_holidays import (
    USNewYearsDay,
    Christmas,
    USMartinLutherKingJrAfter1998,
    USMemorialDay,
    USIndependenceDay,
    USNationalDaysofMourning)

SOFTSSeptember11Closings = date_range('2001-09-11', '2001-09-14', tz='UTC')

class IFUSExchangeCalendar(TradingCalendar):
    """
    Exchange calendar for ICE US.

    Open Time: 8pm, US/Eastern
    Close Time: 6pm, US/Eastern

    https://www.theice.com/publicdocs/futures_us/ICE_Futures_US_Regular_Trading_Hours.pdf # noqa
    """
    product_group = 'US' # UK, US, EU
    regular_early_close = time(13)
    regular_open = time(20,1)
    regular_close = time(18)

    name = 'IFUS'

    tz = timezone("US/Eastern")

    open_times = (
        (None, time(20, 1)),
    )

    close_times = (
        (None, time(18)),
    )

    @property
    def open_offset(self):
        return -1

    @property
    def adhoc_holidays(self):
        if self.product_group == 'CC':
            return list(chain(
                USNationalDaysofMourning,
                SOFTSSeptember11Closings,
                # ICE was only closed on the first day of the Hurricane Sandy
                # closings (was not closed on 2012-10-30)
                [Timestamp('1999-11-26', tz='UTC'),
                Timestamp('1999-12-31', tz='UTC'),
                Timestamp('2000-07-03', tz='UTC'),
                Timestamp('2000-11-24', tz='UTC'),
                Timestamp('2001-11-23', tz='UTC'),
                Timestamp('2001-12-24', tz='UTC'),
                Timestamp('2001-12-31', tz='UTC'),
                Timestamp('2002-07-05', tz='UTC'),
                Timestamp('2002-11-29', tz='UTC'),
                Timestamp('2002-12-26', tz='UTC'),
                Timestamp('2003-02-18', tz='UTC'),
                Timestamp('2003-11-28', tz='UTC'),
                Timestamp('2003-12-26', tz='UTC'),
                Timestamp('2004-01-02', tz='UTC'),
                Timestamp('2004-11-26', tz='UTC'),
                Timestamp('2004-12-31', tz='UTC'),
                Timestamp('2005-11-25', tz='UTC'),
                Timestamp('2006-11-24', tz='UTC'),
                Timestamp('2007-11-23', tz='UTC'),
                Timestamp('2007-12-24', tz='UTC'),
                Timestamp('2011-01-03', tz='UTC'),]
            ))
        if self.product_group == 'CC1Y':
            return list(chain(
                USNationalDaysofMourning,
                SOFTSSeptember11Closings,
                # ICE was only closed on the first day of the Hurricane Sandy
                # closings (was not closed on 2012-10-30)
                [Timestamp('1999-11-26', tz='UTC'),
                Timestamp('1999-12-31', tz='UTC'),
                Timestamp('2000-07-03', tz='UTC'),
                Timestamp('2000-11-24', tz='UTC'),
                Timestamp('2001-11-23', tz='UTC'),
                Timestamp('2001-12-24', tz='UTC'),
                Timestamp('2001-12-31', tz='UTC'),
                Timestamp('2002-07-05', tz='UTC'),
                Timestamp('2002-11-29', tz='UTC'),
                Timestamp('2002-12-26', tz='UTC'),
                Timestamp('2003-02-18', tz='UTC'),
                Timestamp('2003-11-28', tz='UTC'),
                Timestamp('2003-12-26', tz='UTC'),
                Timestamp('2004-01-02', tz='UTC'),
                Timestamp('2004-11-26', tz='UTC'),
                Timestamp('2004-12-31', tz='UTC'),
                Timestamp('2005-11-25', tz='UTC'),
                Timestamp('2006-11-24', tz='UTC'),
                Timestamp('2007-11-23', tz='UTC'),
                Timestamp('2007-12-24', tz='UTC'),
                Timestamp('2011-01-03', tz='UTC'),
                Timestamp('2011-04-26', tz='UTC'),]
            ))
        elif self.product_group == 'KC':
            return list(chain(
                USNationalDaysofMourning,
                SOFTSSeptember11Closings,
                # ICE was only closed on the first day of the Hurricane Sandy
                # closings (was not closed on 2012-10-30)
                [Timestamp('1999-11-26', tz='UTC'),
                Timestamp('1999-12-31', tz='UTC'),
                Timestamp('2000-07-03', tz='UTC'),
                Timestamp('2000-11-24', tz='UTC'),
                Timestamp('2001-11-23', tz='UTC'),
                Timestamp('2001-12-24', tz='UTC'),
                Timestamp('2001-12-26', tz='UTC'),
                Timestamp('2001-12-31', tz='UTC'),
                Timestamp('2002-07-05', tz='UTC'),
                Timestamp('2002-11-29', tz='UTC'),
                Timestamp('2002-12-26', tz='UTC'),
                Timestamp('2003-02-18', tz='UTC'),
                Timestamp('2003-11-28', tz='UTC'),
                Timestamp('2003-12-26', tz='UTC'),
                Timestamp('2004-01-02', tz='UTC'),
                Timestamp('2004-11-26', tz='UTC'),
                Timestamp('2004-12-31', tz='UTC'),
                Timestamp('2005-11-25', tz='UTC'),
                Timestamp('2006-11-24', tz='UTC'),
                Timestamp('2007-11-23', tz='UTC'),
                Timestamp('2007-12-24', tz='UTC'),
                Timestamp('2011-01-03', tz='UTC'),
                ]
            ))
        elif self.product_group == 'KC1Y':
            return list(chain(
                USNationalDaysofMourning,
                SOFTSSeptember11Closings,
                # ICE was only closed on the first day of the Hurricane Sandy
                # closings (was not closed on 2012-10-30)
                [Timestamp('1999-11-26', tz='UTC'),
                Timestamp('1999-12-31', tz='UTC'),
                Timestamp('2000-07-03', tz='UTC'),
                Timestamp('2000-11-24', tz='UTC'),
                Timestamp('2001-06-04', tz='UTC'),
                Timestamp('2001-11-23', tz='UTC'),
                Timestamp('2001-12-24', tz='UTC'),
                Timestamp('2001-12-26', tz='UTC'),
                Timestamp('2001-12-31', tz='UTC'),
                Timestamp('2002-07-05', tz='UTC'),
                Timestamp('2002-11-29', tz='UTC'),
                Timestamp('2002-12-26', tz='UTC'),
                Timestamp('2003-02-18', tz='UTC'),
                Timestamp('2003-11-28', tz='UTC'),
                Timestamp('2003-12-26', tz='UTC'),
                Timestamp('2004-01-02', tz='UTC'),
                Timestamp('2004-06-29', tz='UTC'),
                Timestamp('2004-11-26', tz='UTC'),
                Timestamp('2004-12-31', tz='UTC'),
                Timestamp('2005-11-25', tz='UTC'),
                Timestamp('2006-11-24', tz='UTC'),
                Timestamp('2007-11-23', tz='UTC'),
                Timestamp('2007-12-24', tz='UTC'),
                Timestamp('2011-01-03', tz='UTC'),
                ]
            ))
        elif self.product_group == 'CT':
            return list(chain(
                USNationalDaysofMourning,
                SOFTSSeptember11Closings,
                # ICE was only closed on the first day of the Hurricane Sandy
                # closings (was not closed on 2012-10-30)
                [Timestamp('1999-11-26', tz='UTC'),
                Timestamp('1999-12-31', tz='UTC'),
                Timestamp('2000-07-03', tz='UTC'),
                Timestamp('2000-11-24', tz='UTC'),
                Timestamp('2001-11-23', tz='UTC'),
                Timestamp('2001-12-24', tz='UTC'),
                Timestamp('2001-12-26', tz='UTC'),
                Timestamp('2001-12-31', tz='UTC'),
                Timestamp('2002-07-05', tz='UTC'),
                Timestamp('2002-11-29', tz='UTC'),
                Timestamp('2002-12-24', tz='UTC'),
                Timestamp('2003-02-18', tz='UTC'),
                Timestamp('2003-11-28', tz='UTC'),
                Timestamp('2003-12-26', tz='UTC'),
                Timestamp('2004-01-02', tz='UTC'),
                Timestamp('2004-11-26', tz='UTC'),
                Timestamp('2004-12-31', tz='UTC'),
                Timestamp('2005-11-25', tz='UTC'),
                Timestamp('2006-11-24', tz='UTC'),
                Timestamp('2007-11-23', tz='UTC'),
                Timestamp('2007-12-24', tz='UTC'),
                Timestamp('2011-01-03', tz='UTC'),
                ]
            ))
        elif self.product_group == 'CT1Y':
            return list(chain(
                USNationalDaysofMourning,
                SOFTSSeptember11Closings,
                # ICE was only closed on the first day of the Hurricane Sandy
                # closings (was not closed on 2012-10-30)
                [Timestamp('1999-11-26', tz='UTC'),
                Timestamp('1999-12-31', tz='UTC'),
                Timestamp('2000-07-03', tz='UTC'),
                Timestamp('2000-11-24', tz='UTC'),
                Timestamp('2001-11-23', tz='UTC'),
                Timestamp('2001-12-24', tz='UTC'),
                Timestamp('2001-12-26', tz='UTC'),
                Timestamp('2001-12-31', tz='UTC'),
                Timestamp('2002-07-05', tz='UTC'),
                Timestamp('2002-11-29', tz='UTC'),
                Timestamp('2002-12-24', tz='UTC'),
                Timestamp('2003-02-18', tz='UTC'),
                Timestamp('2003-08-26', tz='UTC'),
                Timestamp('2003-08-27', tz='UTC'),
                Timestamp('2003-08-28', tz='UTC'),
                Timestamp('2003-11-28', tz='UTC'),
                Timestamp('2003-12-26', tz='UTC'),
                Timestamp('2004-01-02', tz='UTC'),
                Timestamp('2004-11-26', tz='UTC'),
                Timestamp('2004-12-31', tz='UTC'),
                Timestamp('2005-11-25', tz='UTC'),
                Timestamp('2006-11-24', tz='UTC'),
                Timestamp('2007-11-23', tz='UTC'),
                Timestamp('2007-12-24', tz='UTC'),
                Timestamp('2011-01-03', tz='UTC'),
                ]
            ))
        elif self.product_group == 'SB':
            return list(chain(
                USNationalDaysofMourning,
                SOFTSSeptember11Closings,
                # ICE was only closed on the first day of the Hurricane Sandy
                # closings (was not closed on 2012-10-30)
                [Timestamp('1999-11-26', tz='UTC'),
                Timestamp('1999-12-31', tz='UTC'),
                Timestamp('2000-07-03', tz='UTC'),
                Timestamp('2000-11-24', tz='UTC'),
                Timestamp('2001-11-23', tz='UTC'),
                Timestamp('2001-12-24', tz='UTC'),
                Timestamp('2001-12-26', tz='UTC'),
                Timestamp('2001-12-31', tz='UTC'),
                Timestamp('2002-07-05', tz='UTC'),
                Timestamp('2002-11-29', tz='UTC'),
                Timestamp('2002-12-24', tz='UTC'),
                Timestamp('2002-12-26', tz='UTC'),
                Timestamp('2003-02-18', tz='UTC'),
                Timestamp('2003-11-28', tz='UTC'),
                Timestamp('2003-12-26', tz='UTC'),
                Timestamp('2004-01-02', tz='UTC'),
                Timestamp('2004-11-26', tz='UTC'),
                Timestamp('2004-12-31', tz='UTC'),
                Timestamp('2005-11-25', tz='UTC'),
                Timestamp('2006-11-24', tz='UTC'),
                Timestamp('2007-11-23', tz='UTC'),
                Timestamp('2007-12-24', tz='UTC'),
                Timestamp('2011-01-03', tz='UTC'),
                ]
            ))
        elif self.product_group == 'SOFTS':
            return list(chain(
                USNationalDaysofMourning,
                SOFTSSeptember11Closings,
                # ICE was only closed on the first day of the Hurricane Sandy
                # closings (was not closed on 2012-10-30)
                [Timestamp('1999-11-26', tz='UTC'),
                Timestamp('1999-12-31', tz='UTC'),
                Timestamp('2000-07-03', tz='UTC'),
                Timestamp('2000-11-24', tz='UTC'),
                Timestamp('2001-11-23', tz='UTC'),
                Timestamp('2001-12-24', tz='UTC'),
                Timestamp('2001-12-26', tz='UTC'),
                Timestamp('2001-12-31', tz='UTC'),
                Timestamp('2002-07-05', tz='UTC'),
                Timestamp('2002-11-29', tz='UTC'),
                Timestamp('2002-12-24', tz='UTC'),
                Timestamp('2002-12-26', tz='UTC'),
                Timestamp('2003-02-18', tz='UTC'),
                Timestamp('2003-11-28', tz='UTC'),
                Timestamp('2003-12-26', tz='UTC'),
                Timestamp('2004-01-02', tz='UTC'),
                Timestamp('2004-11-26', tz='UTC'),
                Timestamp('2004-12-31', tz='UTC'),
                Timestamp('2005-11-25', tz='UTC'),
                Timestamp('2006-11-24', tz='UTC'),
                Timestamp('2007-11-23', tz='UTC'),
                Timestamp('2007-12-24', tz='UTC'),
                Timestamp('2011-01-03', tz='UTC'),
                ]
            ))
        elif self.product_group == 'SOFTS1Y':
            return list(chain(
                USNationalDaysofMourning,
                SOFTSSeptember11Closings,
                # ICE was only closed on the first day of the Hurricane Sandy
                # closings (was not closed on 2012-10-30)
                [Timestamp('1999-11-26', tz='UTC'),
                Timestamp('1999-12-31', tz='UTC'),
                Timestamp('2000-07-03', tz='UTC'),
                Timestamp('2000-11-24', tz='UTC'),
                Timestamp('2001-06-04', tz='UTC'),
                Timestamp('2001-11-23', tz='UTC'),
                Timestamp('2001-12-24', tz='UTC'),
                Timestamp('2001-12-26', tz='UTC'),
                Timestamp('2001-12-31', tz='UTC'),
                Timestamp('2002-07-05', tz='UTC'),
                Timestamp('2002-11-29', tz='UTC'),
                Timestamp('2002-12-24', tz='UTC'),
                Timestamp('2002-12-26', tz='UTC'),
                Timestamp('2003-02-18', tz='UTC'),
                Timestamp('2003-08-26', tz='UTC'),
                Timestamp('2003-08-27', tz='UTC'),
                Timestamp('2003-08-28', tz='UTC'),
                Timestamp('2003-11-28', tz='UTC'),
                Timestamp('2003-12-26', tz='UTC'),
                Timestamp('2004-01-02', tz='UTC'),
                Timestamp('2004-06-29', tz='UTC'),
                Timestamp('2004-11-26', tz='UTC'),
                Timestamp('2004-12-31', tz='UTC'),
                Timestamp('2005-11-25', tz='UTC'),
                Timestamp('2006-11-24', tz='UTC'),
                Timestamp('2007-11-23', tz='UTC'),
                Timestamp('2007-12-24', tz='UTC'),
                Timestamp('2011-01-03', tz='UTC'),
                Timestamp('2011-04-26', tz='UTC'),
                ]
            ))
        else:
            return list(chain(
                USNationalDaysofMourning,
                # ICE was only closed on the first day of the Hurricane Sandy
                # closings (was not closed on 2012-10-30)
                [Timestamp('2012-10-29', tz='UTC')]
            ))

    @property
    def regular_holidays(self):
        # https://www.theice.com/publicdocs/futures_us/exchange_notices/NewExNot2016Holidays.pdf # noqa
        if self.product_group in ['CC', 'KC', 'CT', 'SB', 'SOFTS', 'CC1Y', 'KC1Y', 'CT1Y', 'SOFTS1Y'] :
            return HolidayCalendar([
                USNewYearsDay,
                USMartinLutherKingJrAfter1998,
                USPresidentsDay,
                GoodFriday,
                USMemorialDay,
                USIndependenceDay,
                USLaborDay,
                USThanksgivingDay,
                Christmas
            ])
        else:
            return HolidayCalendar([
                USNewYearsDay,
                GoodFriday,
                Christmas
            ])

    @property
    def day(self):
        return CustomBusinessDay(
            holidays=self.adhoc_holidays,
            calendar=self.regular_holidays,
            weekmask=self.weekmask,
        )
