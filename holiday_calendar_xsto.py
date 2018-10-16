# Stockholm OMX Holiday Calendar
# http://www.nasdaqomxnordic.com/vidskiptatimi

#-------------------------------------------------------
# To Do:
# 

from datetime import time
from pandas import Timestamp
from pandas.tseries.holiday import (
    EasterMonday,
    GoodFriday,
    Holiday,
    previous_workday
)
from pytz import timezone

from .common_holidays import (
    new_years_day,
    european_labour_day,
    whit_monday,
    christmas_eve,
    christmas,
    boxing_day,
    new_years_eve,

)

NewYearsDay = new_years_day()

EuropeanLabourDay = european_labour_day()

WhitMonday = whit_monday(start_date='2015-01-01')

ChristmasEve = christmas_eve()

Christmas = christmas()

BoxingDay = boxing_day()

NewYearsEve = new_years_eve()

New Years Day 
Epiphany Dayx
Good Friday 
Easter Monday
Labour day 
Asension Dayx
National Dayx
Friday of Summer Solstice (Mid summer's day) x
Christmas Eve
Christmas Day
Boxing Day 
New Years Eve
Twelfth Night 
Maundy Thursday 
Walpurgis Night (Day before labour day)  
Day before Ascension Day 
Day before National Day
Thursday before Summer Solstice (Midsummer's Day)
All Saint's Eve 
