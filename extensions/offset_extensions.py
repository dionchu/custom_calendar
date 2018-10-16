# -*- coding: utf-8 -*-
import ephem
from lunardate import LunarDate
###
from pandas import DateOffset
from pandas.errors import PerformanceWarning
from datetime import datetime, timedelta
from pandas.tseries.offsets import apply_wraps
from pandas._libs.tslibs.offsets import (
    _is_normalized,
)

def summer_solstice(year,offset=None,observance=None):
    dt = datetime(year,1,1)
    dt = ephem.next_summer_solstice(dt).datetime().replace(hour=0, minute=0, second=0, microsecond=0)
    if offset != None:
        dt = dt + timedelta(offset)
    return dt if observance == None else observance(dt)

def vernal_equinox(year,offset=None,observance=None):
    dt = datetime(year,1,1)
    dt = ephem.next_vernal_equinox(dt).datetime().replace(hour=0, minute=0, second=0, microsecond=0)
    if offset != None:
        dt = dt + timedelta(offset)
    return dt if observance == None else observance(dt)

def lunar_new_year(year,offset=None,observance=None):
    dt = LunarDate(year, 1, 1).toSolarDate()
    if offset != None:
        dt = dt + timedelta(offset)
    return dt if observance == None else observance(dt)

def buddha_birthday(year,offset=None,observance=None):
    dt = LunarDate(year, 4, 8).toSolarDate()
    if offset != None:
        dt = dt + timedelta(offset)
    return dt if observance == None else observance(dt)

def dragon_boat_festival(year,offset=None,observance=None):
    dt = LunarDate(year, 5, 5).toSolarDate()
    if offset != None:
        dt = dt + timedelta(offset)
    return dt if observance == None else observance(dt)

def mid_autumn_festival(year,offset=None,observance=None):
    dt = LunarDate(year, 8, 15).toSolarDate()
    if offset != None:
        dt = dt + timedelta(offset)
    return dt if observance == None else observance(dt)

def double_nine_festival(year,offset=None,observance=None):
    dt = LunarDate(year, 9, 9).toSolarDate()
    if offset != None:
        dt = dt + timedelta(offset)
    return dt if observance == None else observance(dt)

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


class next_spring_festival(DateOffset):
    """
    DateOffset for the Spring Festival holiday
    using logic defined in lunardate.
    """
    _adjust_dst = True
    _attributes = frozenset(['offset','observance','n', 'normalize'])

    def __init__(self, offset=None, observance=None, n=1, normalize=False):
        self.n = self._validate_n(n)
        self.normalize = normalize
        self.offset = offset
        self.observance = observance

    @apply_wraps
    def apply(self, other):
        current_lunar_new_year = lunar_new_year(other.year,self.offset,self.observance)
        current_lunar_new_year = datetime(current_lunar_new_year.year,
                                  current_lunar_new_year.month, current_lunar_new_year.day)
        current_lunar_new_year = localize_pydatetime(current_lunar_new_year,
                                                    other.tzinfo)

        n = self.n
        if n >= 0 and other < current_lunar_new_year:
            n -= 1
        elif n < 0 and other > current_lunar_new_year:
            n += 1
        # TODO: Why does this handle the 0 case the opposite of others?

        # NOTE: lunar new year returns a datetime.date so we have to convert to type of
        # other
        new = lunar_new_year(other.year + n,self.offset,self.observance)
        new = datetime(new.year, new.month, new.day, other.hour,
                       other.minute, other.second, other.microsecond)
        return new

    def onOffset(self, dt):
        if self.normalize and not _is_normalized(dt):
            return False
        return date(dt.year, dt.month, dt.day) == lunar_new_year(dt.year,self.offset,self.observance)

class next_buddha_birthday(DateOffset):
    """
    DateOffset for Buddha's Birthday
    using logic defined in lunardate.
    """
    _adjust_dst = True
    _attributes = frozenset(['offset','observance','n', 'normalize'])

    def __init__(self, offset=None, observance=None, n=1, normalize=False):
        self.n = self._validate_n(n)
        self.normalize = normalize
        self.offset = offset
        self.observance = observance

    @apply_wraps
    def apply(self, other):
        current_buddha_birthday = buddha_birthday(other.year,self.offset,self.observance)
        current_buddha_birthday = datetime(current_buddha_birthday.year,
                                  current_buddha_birthday.month, current_buddha_birthday.day)
        current_buddha_birthday = localize_pydatetime(current_buddha_birthday,
                                                    other.tzinfo)

        n = self.n
        if n >= 0 and other < current_buddha_birthday:
            n -= 1
        elif n < 0 and other > current_buddha_birthday:
            n += 1
        # TODO: Why does this handle the 0 case the opposite of others?

        # NOTE: Buddha birthday returns a datetime.date so we have to convert to type of
        # other
        new = buddha_birthday(other.year + n,self.offset,self.observance)
        new = datetime(new.year, new.month, new.day, other.hour,
                       other.minute, other.second, other.microsecond)
        return new

    def onOffset(self, dt):
        if self.normalize and not _is_normalized(dt):
            return False
        return date(dt.year, dt.month, dt.day) == buddha_birthday(dt.year,self.offset,self.observance)

class next_dragon_boat_festival(DateOffset):
    """
    DateOffset for Dragon Boat Festival
    using logic defined in lunardate.
    """
    _adjust_dst = True
    _attributes = frozenset(['offset','observance','n', 'normalize'])

    def __init__(self, offset=None, observance=None, n=1, normalize=False):
        self.n = self._validate_n(n)
        self.normalize = normalize
        self.offset = offset
        self.observance = observance

    @apply_wraps
    def apply(self, other):
        current_dragon_boat_festival = dragon_boat_festival(other.year,self.offset,self.observance)
        current_dragon_boat_festival = datetime(current_dragon_boat_festival.year,
                                  current_dragon_boat_festival.month, current_dragon_boat_festival.day)
        current_dragon_boat_festival = localize_pydatetime(current_dragon_boat_festival,
                                                    other.tzinfo)

        n = self.n
        if n >= 0 and other < current_dragon_boat_festival:
            n -= 1
        elif n < 0 and other > current_dragon_boat_festival:
            n += 1
        # TODO: Why does this handle the 0 case the opposite of others?

        # NOTE: Dragon Boat Festival returns a datetime.date so we have to convert to type of
        # other
        new = dragon_boat_festival(other.year + n,self.offset,self.observance)
        new = datetime(new.year, new.month, new.day, other.hour,
                       other.minute, other.second, other.microsecond)
        return new

    def onOffset(self, dt):
        if self.normalize and not _is_normalized(dt):
            return False
        return date(dt.year, dt.month, dt.day) == dragon_boat_festival(dt.year,self.offset,self.observance)

class next_mid_autumn_festival(DateOffset):
    """
    DateOffset for Mid Autumn Festival
    using logic defined in lunardate.
    """
    _adjust_dst = True
    _attributes = frozenset(['offset','observance','n', 'normalize'])

    def __init__(self, offset=None, observance=None, n=1, normalize=False):
        self.n = self._validate_n(n)
        self.normalize = normalize
        self.offset = offset
        self.observance = observance

    @apply_wraps
    def apply(self, other):
        current_mid_autumn_festival = mid_autumn_festival(other.year,self.offset,self.observance)
        current_mid_autumn_festival = datetime(current_mid_autumn_festival.year,
                                  current_mid_autumn_festival.month, current_mid_autumn_festival.day)
        current_mid_autumn_festival = localize_pydatetime(current_mid_autumn_festival,
                                                    other.tzinfo)

        n = self.n
        if n >= 0 and other < current_mid_autumn_festival:
            n -= 1
        elif n < 0 and other > current_mid_autumn_festival:
            n += 1
        # TODO: Why does this handle the 0 case the opposite of others?

        # NOTE: Mid-autumn Festival returns a datetime.date so we have to convert to type of
        # other
        new = mid_autumn_festival(other.year + n,self.offset,self.observance)
        new = datetime(new.year, new.month, new.day, other.hour,
                       other.minute, other.second, other.microsecond)
        return new

    def onOffset(self, dt):
        if self.normalize and not _is_normalized(dt):
            return False
        return date(dt.year, dt.month, dt.day) == mid_autumn_festival(dt.year,self.offset,self.observance)

class next_double_nine_festival(DateOffset):
    """
    DateOffset for Double-Nine
    using logic defined in lunardate.
    """
    _adjust_dst = True
    _attributes = frozenset(['offset','observance','n', 'normalize'])

    def __init__(self, offset=None, observance=None, n=1, normalize=False):
        self.n = self._validate_n(n)
        self.normalize = normalize
        self.offset = offset
        self.observance = observance

    @apply_wraps
    def apply(self, other):
        current_double_nine_festival = double_nine_festival(other.year,self.offset,self.observance)
        current_double_nine_festival = datetime(current_double_nine_festival.year,
                                  current_double_nine_festival.month, current_double_nine_festival.day)
        current_double_nine_festival = localize_pydatetime(current_double_nine_festival,
                                                    other.tzinfo)

        n = self.n
        if n >= 0 and other < current_double_nine_festival:
            n -= 1
        elif n < 0 and other > current_double_nine_festival:
            n += 1
        # TODO: Why does this handle the 0 case the opposite of others?

        # NOTE: Double Nine Festival returns a datetime.date so we have to convert to type of
        # other
        new = double_nine_festival(other.year + n,self.offset,self.observance)
        new = datetime(new.year, new.month, new.day, other.hour,
                       other.minute, other.second, other.microsecond)
        return new

    def onOffset(self, dt):
        if self.normalize and not _is_normalized(dt):
            return False
        return date(dt.year, dt.month, dt.day) == double_nine_festival(dt.year,self.offset,self.observance)

class next_spring_equinox(DateOffset):
    """
    DateOffset for Spring Equinox
    using logic defined in lunardate.
    """
    _adjust_dst = True
    _attributes = frozenset(['offset','observance','n', 'normalize'])

    def __init__(self, offset=None, observance=None, n=1, normalize=False):
        self.n = self._validate_n(n)
        self.normalize = normalize
        self.offset = offset
        self.observance = observance

    @apply_wraps
    def apply(self, other):
        current_vernal_equinox = vernal_equinox(other.year,self.offset,self.observance)
        current_vernal_equinox = datetime(current_vernal_equinox.year,
                                  current_vernal_equinox.month, current_vernal_equinox.day)
        current_vernal_equinox = localize_pydatetime(current_vernal_equinox,
                                                    other.tzinfo)

        n = self.n
        if n >= 0 and other < current_vernal_equinox:
            n -= 1
        elif n < 0 and other > current_vernal_equinox:
            n += 1
        # TODO: Why does this handle the 0 case the opposite of others?

        # NOTE: Vernal equinox returns a datetime.date so we have to convert to type of
        # other
        new = vernal_equinox(other.year + n,self.offset,self.observance)
        new = datetime(new.year, new.month, new.day, other.hour,
                       other.minute, other.second, other.microsecond)
        return new

    def onOffset(self, dt):
        if self.normalize and not _is_normalized(dt):
            return False
        return date(dt.year, dt.month, dt.day) == vernal_equinox(dt.year,self.offset,self.observance)

class next_summer_solstice(DateOffset):
    """
    DateOffset for Spring Equinox
    using logic defined in lunardate.
    """
    _adjust_dst = True
    _attributes = frozenset(['offset','observance','n', 'normalize'])

    def __init__(self, offset=None, observance=None, n=1, normalize=False):
        self.n = self._validate_n(n)
        self.normalize = normalize
        self.offset = offset
        self.observance = observance

    @apply_wraps
    def apply(self, other):
        current_summer_solstice = summer_solstice(other.year,self.offset,self.observance)
        current_summer_solstice = datetime(current_summer_solstice.year,
                                  current_summer_solstice.month, current_summer_solstice.day)
        current_summer_solstice = localize_pydatetime(current_summer_solstice,
                                                    other.tzinfo)

        n = self.n
        if n >= 0 and other < current_summer_solstice:
            n -= 1
        elif n < 0 and other > current_summer_solstice:
            n += 1
        # TODO: Why does this handle the 0 case the opposite of others?

        # NOTE: Summer solstice returns a datetime.date so we have to convert to type of
        # other
        new = summer_solstice(other.year + n,self.offset,self.observance)
        new = datetime(new.year, new.month, new.day, other.hour,
                       other.minute, other.second, other.microsecond)
        return new

    def onOffset(self, dt):
        if self.normalize and not _is_normalized(dt):
            return False
        return date(dt.year, dt.month, dt.day) == summer_solstice(dt.year,self.offset,self.observance)
