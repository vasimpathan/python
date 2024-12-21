# -*- coding: utf-8 -*-
"""Day_18.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1qYZhWsB9u_pV0tmInv1Jx0iCSIoDHSAN
"""



"""# **Python Module - Datetime**"""

import datetime

from datetime import datetime, date, time, timedelta

curr_datetime = datetime.now()

curr_datetime

curr_datetime.year

curr_datetime.month

curr_datetime.day

# 1st Jan, 2024
# 01-01-2024
# 2024-01-01
# 1st January 2024

# Y-M-D
date(2024, 1, 1)

# HH:MM:SS
time(14,20,20)

my_time = time(14, 20, 30)

my_time.hour, my_time.minute, my_time.second

# Y-M-D-HH-MM-SS
datetime(2024, 1, 1, 14, 20, 30)

from datetime import timedelta

timedelta(hours=5)

curr_datetime + timedelta(hours =5)

curr_datetime

# short date - 1st jan 2024
# long date - 1st January 2024
# timezones
# difference between dates, time