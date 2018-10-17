import warnings

from pandas import DateOffset, DatetimeIndex, Series, Timestamp
from pandas.errors import PerformanceWarning
from pandas.compat import add_metaclass
from datetime import datetime, timedelta
import numpy as np

def friday_week_of(dt):
    """
    returns friday of current week
    """
    return dt + timedelta(days=4) + timedelta(days=-dt.weekday())

def sunday_to_tuesday(dt):
    """
    If holiday falls on Sunday, use two days thereafter (Tuesday) instead.
    """
    if dt.weekday() == 6:
        return dt + timedelta(2)
    return dt

def sunday_to_wednesday(dt):
    """
    If holiday falls on Sunday, use three days thereafter (Wednesday) instead.
    """
    if dt.weekday() == 6:
        return dt + timedelta(3)
    return dt

def hong_kong_rules(dt):
    """
    If holiday falls on National Day observance, move to day after National Day
    """
    prc_day = datetime(dt.year,10,1)
    if prc_day.weekday() == 6:
        prc_day = prc_day + timedelta(1)
    if dt.weekday() == 6:
        dt = dt + timedelta(1)
    if dt.month == 10 and dt.day == prc_day.day:
        return dt.replace(day=prc_day.day+1)
    return dt

class HolidayWithFilter(object):
    """
    Class that defines a holiday with start/end dates and rules
    for observance.
    """

    def __init__(self, name, year=None, month=None, day=None, offset=None,
                 observance=None, start_date=None, end_date=None,
                 days_of_week=None, year_filter=None, year_mask=None):
        """
        Parameters
        ----------
        name : str
            Name of the holiday , defaults to class name
        offset : array of pandas.tseries.offsets or
                class from pandas.tseries.offsets
            computes offset from date
        observance: function
            computes when holiday is given a pandas Timestamp
        days_of_week:
            provide a tuple of days e.g  (0,1,2,3,) for Monday Through Thursday
            Monday=0,..,Sunday=6
        """
        if offset is not None and observance is not None:
            raise NotImplementedError("Cannot use both offset and observance.")

        self.name = name
        self.year = year
        self.month = month
        self.day = day
        self.offset = offset
        self.start_date = Timestamp(
            start_date) if start_date is not None else start_date
        self.end_date = Timestamp(
            end_date) if end_date is not None else end_date
        self.observance = observance
        assert (days_of_week is None or type(days_of_week) == tuple)
        self.days_of_week = days_of_week
        self.year_filter = year_filter
        self.year_mask = year_mask

    def __repr__(self):
        info = ''
        if self.year is not None:
            info += 'year={year}, '.format(year=self.year)
        info += 'month={mon}, day={day}, '.format(mon=self.month, day=self.day)

        if self.offset is not None:
            info += 'offset={offset}'.format(offset=self.offset)

        if self.observance is not None:
            info += 'observance={obs}'.format(obs=self.observance)
        
        if self.year_filter is not None:
            info += 'year_filter={yrf}'.format(yrf=self.year_filter)
            
        if self.year_mask is not None:
            info += 'year_mask={yrm}'.format(yrf=self.year_mask)            

        repr = 'Holiday: {name} ({info})'.format(name=self.name, info=info)
        return repr

    def dates(self, start_date, end_date, return_name=False):
        """
        Calculate holidays observed between start date and end date
        Parameters
        ----------
        start_date : starting date, datetime-like, optional
        end_date : ending date, datetime-like, optional
        return_name : bool, optional, default=False
            If True, return a series that has dates and holiday names.
            False will only return dates.
        """
        start_date = Timestamp(start_date)
        end_date = Timestamp(end_date)

        filter_start_date = start_date
        filter_end_date = end_date

        if self.year is not None:
            dt = Timestamp(datetime(self.year, self.month, self.day))
            if return_name:
                return Series(self.name, index=[dt])
            else:
                return [dt]

        dates = self._reference_dates(start_date, end_date)
        holiday_dates = self._apply_rule(dates)
        if self.days_of_week is not None:
            holiday_dates = holiday_dates[np.in1d(holiday_dates.dayofweek,
                                                  self.days_of_week)]

        if self.start_date is not None:
            filter_start_date = max(self.start_date.tz_localize(
                filter_start_date.tz), filter_start_date)
        if self.end_date is not None:
            filter_end_date = min(self.end_date.tz_localize(
                filter_end_date.tz), filter_end_date)
        holiday_dates = holiday_dates[(holiday_dates >= filter_start_date) &
                                      (holiday_dates <= filter_end_date)]
            
        if return_name:
            return Series(self.name, index=holiday_dates)
        return holiday_dates

    def _reference_dates(self, start_date, end_date):
        """
        Get reference dates for the holiday.
        Return reference dates for the holiday also returning the year
        prior to the start_date and year following the end_date.  This ensures
        that any offsets to be applied will yield the holidays within
        the passed in dates.
        """
        if self.start_date is not None:
            start_date = self.start_date.tz_localize(start_date.tz)

        if self.end_date is not None:
            end_date = self.end_date.tz_localize(start_date.tz)

        year_offset = DateOffset(years=1)
        reference_start_date = Timestamp(
            datetime(start_date.year - 1, self.month, self.day))

        reference_end_date = Timestamp(
            datetime(end_date.year + 1, self.month, self.day))
        # Don't process unnecessary holidays
        dates = DatetimeIndex(start=reference_start_date,
                              end=reference_end_date,
                              freq=year_offset, tz=start_date.tz)
        
        if self.year_filter is not None:
            dates = dates[~dates.year.isin(self.year_filter)]
        
        if self.year_mask is not None:
            dates = dates[dates.year.isin(self.year_mask)]
            
        return dates

    def _apply_rule(self, dates):
        """
        Apply the given offset/observance to a DatetimeIndex of dates.
        Parameters
        ----------
        dates : DatetimeIndex
            Dates to apply the given offset/observance rule
        Returns
        -------
        Dates with rules applied
        """
        if self.observance is not None:
            return dates.map(lambda d: self.observance(d))

        if self.offset is not None:
            if not isinstance(self.offset, list):
                offsets = [self.offset]
            else:
                offsets = self.offset
            for offset in offsets:

                # if we are adding a non-vectorized value
                # ignore the PerformanceWarnings:
                with warnings.catch_warnings():
                    warnings.simplefilter("ignore", PerformanceWarning)
                    dates += offset
        return dates
