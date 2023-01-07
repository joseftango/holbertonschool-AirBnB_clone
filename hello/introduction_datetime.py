#!/usr/bin/python3

import datetime

#print(dir(datetime))
my_bir = datetime.date(1997, 5, 26)
print(type(my_bir.isoformat())) # create a date according to your mood

current = datetime.date.today()
print(type(current))

my_age = current - my_bir
print(my_age)

