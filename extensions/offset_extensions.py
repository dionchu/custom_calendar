# -*- coding: utf-8 -*-
import ephem
###
from pandas import DateOffset, DatetimeIndex, Series, Timestamp
from pandas.errors import PerformanceWarning
from pandas.compat import add_metaclass
from datetime import datetime, timedelta
from dateutil.relativedelta import MO, TU, WE, TH, FR, SA, SU  # noqa
from pandas.tseries.offsets import Easter, Day, apply_wraps
from pandas._libs.tslibs import (
    ccalendar, conversion,
    frequencies as libfrequencies)

from pandas._libs.tslibs.offsets import (
    _is_normalized,
)

def summer_solstice(year):
    dt = datetime(year,1,1)
    return ephem.next_summer_solstice(dt).datetime().replace(hour=0, minute=0, second=0, microsecond=0)

def localize_pydatetime(dt, tz):
    """
    Take a datetime/Timestamp in UTC and localizes to timezone tz.
    Parameters
    ----------
    dt : datetime or Timestamp
    tz : tzinfo, "UTC", or None
    Returns
    -------
    localized : datetime or Timestamp
    """
    if tz is None:
        return dt
    elif not PyDateTime_CheckExact(dt):
        # i.e. is a Timestamp
        return dt.tz_localize(tz)
    elif tz == 'UTC' or tz is UTC:
        return UTC.localize(dt)
    try:
        # datetime.replace with pytz may be incorrect result
        return tz.localize(dt)
    except AttributeError:
        return dt.replace(tzinfo=tz)

class SummerSolstice(DateOffset):
    """
    DateOffset for the Summer Solstice using
    logic defined in ephem.
    """
    _adjust_dst = True
    _attributes = frozenset(['n', 'normalize'])

    def __init__(self, n=1, normalize=False):
        self.n = self._validate_n(n)
        self.normalize = normalize

    @apply_wraps
    def apply(self, other):
        current_summer_solstice = summer_solstice(other.year)
        current_summer_solstice = localize_pydatetime(current_summer_solstice,
                                                            other.tzinfo)

        n = self.n
        if n >= 0 and other < current_summer_solstice:
            n -= 1
        elif n < 0 and other > current_summer_solstice:
            n += 1
        # TODO: Why does this handle the 0 case the opposite of others?

        # NOTE: easter returns a datetime.date so we have to convert to type of
        # other
        new = summer_solstice(other.year + n)
        new = datetime(new.year, new.month, new.day, other.hour,
                       other.minute, other.second, other.microsecond)
        return new

    def onOffset(self, dt):
        if self.normalize and not _is_normalized(dt):
            return False
        return date(dt.year, dt.month, dt.day) == summer_solstice(dt.year)
