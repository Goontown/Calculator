#!/usr/bin/env python3

import datetime
import math
from decimal import *

datetime.MINYEAR=2019
datetime.MAXYEAR=2020

#Today är dagens datum.
today = datetime.datetime.today()

def main ():
    user_input = input( "Day that the subscription started, format should be YYYY-MM-DD : ")
    day = user_input [-2:]
    result = ""
    if int(day) < 15:
        result =  "{}-01".format(user_input[:-3])
        result = datetime.datetime.strptime(result, '%Y-%m-%d')
        print(result)
        diff=today-result
        print("Amount of days for refund:",diff.days)
        price = 2.16438356
        payback = diff.days * price
        print("Customer's refund is:",payback,"SEK")
    else:
        user_input = datetime.datetime.strptime(user_input, '%Y-%m-%d')
        diff = today - user_input
        print("Amount of days for refund:",diff.days)
        price = 2.16438356
        payback = diff.days * price
        print("Customer's refund is:{:.3f}SEK" (format(payback)))


if __name__ == '__main__':
    main()





