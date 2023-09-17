import datetime
my_datetime_object = datetime.datetime.now()
print(my_datetime_object)
print(dir(datetime))

my_date = datetime.date(1966,7,30)
print(my_date)


from datetime import datetime, date
my_start = date(year= 2016, month= 7, day= 12)
my_end = date(year= 2019, month= 7, day= 27)
my_term = my_end - my_start
print(my_term)