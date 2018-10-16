#-------------------------------------------------------
# To Do:
# Check how Japan determines Vernal Equinox holiday

from datetime import time
from pandas.tseries.holiday import Holiday, Easter
from pandas.tseries.offsets import Day
from pytz import timezone

from .trading_calendar import MONDAY, TUESDAY

# Set up code to calculate equinox dates
import datetime
import ephem
import pandas as pd

def friday_week_of(dt):
    """
    returns friday of current week
    """
    return dt + timedelta(days=4) + timedelta(days=-dt.weekday())
  
def summer_solstice_friday(start_date=None,
                           end_date=None):
  if start_date == None:
    start_date = '1970-01-01'
  
  if end_date == None:
    end_date = datetime.date(datetime.datetime.now().year+20,1,1).strftime('%Y-%m-%d')

  drange = pd.date_range(start=start_date,end=end_date,freq='YS').strftime('%Y-%m-%d')
  
  next_summer_solstice = lambda x: Timestamp(ephem.next_summer_solstice(x).datetime().replace(hour=0, minute=0, second=0, microsecond=0).strftime('%Y-%m-%d')) 
  range_solstices = [next_summer_solstice(x) for x in drange]

  to_friday = lambda x: x + timedelta(days=4) + timedelta(days=-x.weekday())
  return [to_friday(x) for x in range_solstices]

# It doesn't appear that Japan follows the actual vernal equinox, must be some adjustment for weekends?
#next_vernal_equinox =  lambda x: Timestamp(ephem.next_vernal_equinox(x).datetime().replace(hour=0, minute=0, second=0, microsecond=0).strftime('%Y-%m-%d')) 
#VernalEquinoxes = [next_vernal_equinox(x) for x in drange]

def new_years_day(start_date=None,
                  end_date=None,
                  observance=None,
                  days_of_week=None):
    return Holiday(
        "New Year's Day",
        month=1,
        day=1,
        start_date=start_date,
        end_date=end_date,
        observance=observance,
        days_of_week=days_of_week,
    )


def anzac_day(start_date=None,
              end_date=None,
              observance=None,
              days_of_week=None):
    return Holiday(
        'Anzac Day',
        month=4,
        day=25,
        start_date=start_date,
        end_date=end_date,
        observance=observance,
        days_of_week=days_of_week,
    )


def epiphany(start_date=None,
             end_date=None,
             observance=None,
             days_of_week=None):
    return Holiday(
        'Epiphany',
        month=1,
        day=6,
        start_date=start_date,
        end_date=end_date,
        observance=observance,
        days_of_week=days_of_week,
    )

def wed_before_maundy_thursday(start_date=None, end_date=None):
    return Holiday(
        "Maundy Thursday",
        month=1,
        day=1,
        offset=[Easter(), Day(-4)],
        start_date=start_date,
        end_date=end_date,
    )
  
def maundy_thursday(start_date=None, end_date=None):
    return Holiday(
        "Maundy Thursday",
        month=1,
        day=1,
        offset=[Easter(), Day(-3)],
        start_date=start_date,
        end_date=end_date,
    )
  
def european_labour_day(start_date=None,
                        end_date=None,
                        observance=None,
                        days_of_week=None):
    return Holiday(
        "Labour Day",
        month=5,
        day=1,
        start_date=start_date,
        end_date=end_date,
        observance=observance,
        days_of_week=days_of_week,
    )


# Ascension Day, Whit Monday, and Corpus Christi do not take observance as a
# parameter because they depend on a particular offset, and offset and
# observance cannot both be passed to a Holiday.
def ascension_day(start_date=None, end_date=None):
    return Holiday(
        "Ascension Day",
        month=1,
        day=1,
        offset=[Easter(), Day(39)],
        start_date=start_date,
        end_date=end_date,
    )


def whit_monday(start_date=None, end_date=None):
    return Holiday(
        "Whit Monday",
        month=1,
        day=1,
        offset=[Easter(), Day(50)],
        start_date=start_date,
        end_date=end_date,
    )


def corpus_christi(start_date=None, end_date=None):
    return Holiday(
        'Corpus Christi',
        month=1,
        day=1,
        offset=[Easter(), Day(60)],
        start_date=start_date,
        end_date=end_date,
    )


def assumption_day(start_date=None,
                   end_date=None,
                   observance=None,
                   days_of_week=None):
    return Holiday(
        'Assumption Day',
        month=8,
        day=15,
        start_date=start_date,
        end_date=end_date,
        observance=observance,
        days_of_week=days_of_week,
    )


def all_saints_day(start_date=None,
                   end_date=None,
                   observance=None,
                   days_of_week=None):
    return Holiday(
        'All Saints Day',
        month=11,
        day=1,
        start_date=start_date,
        end_date=end_date,
        observance=observance,
        days_of_week=days_of_week,
    )


def immaculate_conception(start_date=None,
                          end_date=None,
                          observance=None,
                          days_of_week=None):
    return Holiday(
        'Immaculate Conception',
        month=12,
        day=8,
        start_date=start_date,
        end_date=end_date,
        observance=observance,
        days_of_week=days_of_week,
    )


def christmas_eve(start_date=None,
                  end_date=None,
                  observance=None,
                  days_of_week=None):
    return Holiday(
        'Christmas Eve',
        month=12,
        day=24,
        start_date=start_date,
        end_date=end_date,
        observance=observance,
        days_of_week=days_of_week,
    )


def christmas(start_date=None,
              end_date=None,
              observance=None,
              days_of_week=None):
    return Holiday(
        "Christmas",
        month=12,
        day=25,
        start_date=start_date,
        end_date=end_date,
        observance=observance,
        days_of_week=days_of_week,
    )


def weekend_christmas(start_date=None, end_date=None, observance=None):
    """
    If christmas day is Saturday Monday 27th is a holiday
    If christmas day is sunday the Tuesday 27th is a holiday
    """
    return Holiday(
        "Weekend Christmas",
        month=12,
        day=27,
        days_of_week=(MONDAY, TUESDAY),
        start_date=start_date,
        end_date=end_date,
        observance=observance,
    )


def boxing_day(start_date=None,
               end_date=None,
               observance=None,
               days_of_week=None):
    return Holiday(
        "Boxing Day",
        month=12,
        day=26,
        start_date=start_date,
        end_date=end_date,
        observance=observance,
        days_of_week=days_of_week,
    )


def weekend_boxing_day(start_date=None, end_date=None, observance=None):
    """
    If boxing day is saturday then Monday 28th is a holiday
    If boxing day is sunday then Tuesday 28th is a holiday
    """
    return Holiday(
        "Weekend Boxing Day",
        month=12,
        day=28,
        days_of_week=(MONDAY, TUESDAY),
        start_date=start_date,
        end_date=end_date,
        observance=observance,
    )


def new_years_eve(start_date=None,
                  end_date=None,
                  observance=None,
                  days_of_week=None):
    return Holiday(
        "New Year's Eve",
        month=12,
        day=31,
        start_date=start_date,
        end_date=end_date,
        observance=observance,
        days_of_week=days_of_week,
    )
