from datetime import time
from itertools import chain
import pandas as pd
from pytz import timezone

from .trading_calendar import (
    TradingCalendar,
    HolidayCalendar,
    end_default,
)
from .xjpx_holidays import (
    NewYearsHolidayDec31,
    NewYearsHolidayJan1,
    NewYearsHolidayJan2,
    NewYearsHolidayJan3,
    ComingOfAgeDay,
    NationalFoundationDay,
    VernalEquinoxes,
    GreeneryDayThrough2006,
    ShowaDay,
    ConstitutionMemorialDay,
    GreeneryDay2007Onwards,
    CitizensHolidayGoldenWeek,
    ChildrensDay,
    MarineDayThrough2002,
    MarineDay2003Onwards,
    MountainDay,
    AutumnalEquinoxes,
    CitizensHolidaySilverWeek,
    RespectForTheAgedDayThrough2002,
    RespectForTheAgedDay2003Onwards,
    HealthAndSportsDay,
    CultureDay,
    LaborThanksgivingDay,
    EmperorAkihitoBirthday,
    EmperorNaruhitoBirthday,
)


XJPX_START_DEFAULT = pd.Timestamp('2000-01-01', tz='UTC')


class XJPXExchangeCalendar(TradingCalendar):
    """
    Exchange calendar for the JPX Group
        Tokyo Stock Exchange
        Osaka Securities Exchange

    First session: 9:00am - 11:30am
    Lunch
    Second session: 12:30pm - 3:00pm

    NOTE: we are treating the two sessions per day as one session for now,
    because we will not be handling minutely data in the immediate future.

    Regularly-Observed Holidays (see tse_holidays.py for more info):
    - New Year's Holidays (Dec. 31 - Jan. 3)
    - Coming of Age Day (second Monday of January)
    - National Foundation Day (Feb. 11)
    - Vernal Equinox (usually Mar 20-22)
    - Greenery Day (Apr. 29 2000-2006, May 4 2007-present)
    - Showa Day (Apr. 29 2007-present)
    - Constitution Memorial Day (May 3)
    - Citizen's Holiday (May 4 2000-2006, later replaced by Greenery Day)
    - Children's Day (May 5)
    - Marine Day (July 20 2000-2002, third Monday of July 2003-present)
    - Respect for the Aged Day (Sep. 15 2000-2002, third Monday
      of Sep. 2003-present)
    - Autumnal Equinox (usually Sept. 22-24)
    - Health-Sports Day (second Monday of October)
    - Culture Day (November 3)
    - Labor Thanksgiving Day (Nov. 23)
    - Emperor's Birthday (Dec. 23)
    """
    def __init__(self, start=XJPX_START_DEFAULT, end=end_default):
        # because we are not tracking holiday info farther back than 2000,
        # make the default start date 01-01-2000
        super(XJPXExchangeCalendar, self).__init__(start=start, end=end)

    regular_open = time(9,1)
    regular_close = time(15, 00)
       
    @property
    def name(self):
        return "XJPX"

    @property
    def tz(self):
        return timezone('Asia/Tokyo')

    @property
    def open_time(self):
        return self.regular_open

    @property
    def close_time(self):
        return self.regular_close

    @property
    def regular_holidays(self):
        return HolidayCalendar([
            NewYearsHolidayDec31,
            NewYearsHolidayJan1,
            NewYearsHolidayJan2,
            NewYearsHolidayJan3,
            ComingOfAgeDay,
            NationalFoundationDay,
            GreeneryDayThrough2006,
            ShowaDay,
            ConstitutionMemorialDay,
            GreeneryDay2007Onwards,
            CitizensHolidayGoldenWeek,
            ChildrensDay,
            MarineDayThrough2002,
            MarineDay2003Onwards,
            MountainDay,
            RespectForTheAgedDayThrough2002,
            RespectForTheAgedDay2003Onwards,
            HealthAndSportsDay,
            CultureDay,
            LaborThanksgivingDay,
            EmperorAkihitoBirthday,
            EmperorNaruhitoBirthday,
        ])

    @property
    def adhoc_holidays(self):
        return list(chain(
            VernalEquinoxes,
            AutumnalEquinoxes,
            CitizensHolidaySilverWeek,
        ))
