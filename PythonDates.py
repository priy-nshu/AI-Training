from datetime import date,datetime,time,timedelta

def simple_date():
    t1 = date.today()
    print("Today's date:", t1)
    print("Year:", t1.year)
    print("Month:", t1.month)
    print("Day:", t1.day)

    Now = datetime.now()
    print("Current date and time:", Now)

    my_birthday = date(2004, 2, 11)
    print("My birthday:", my_birthday," Type:", type(my_birthday))

    dt1 =datetime(2024, 6, 1, 12, 30, 45)
    print(f'Date with time: {dt1} Time: {dt1.time()}')

def time_functions():
    t1 = time(14, 30, 45)
    print("Time:", t1)
    print("Hour:", t1.hour)
    print("Minute:", t1.minute)
    print("Second:", t1.second)
    print("Microsecond:", t1.microsecond)
    Time =time(12,24,36,1212)

    Str =Time.isoformat()
    print("Time in ISO format:", Str)
    print(type(Str))

def Timedelta():
    now = datetime.now()
    print("Current date and time:", now)

    after_2_years = now + timedelta(days=365*2)
    print("Date after 2 years:", after_2_years)

    future_date = now + timedelta(days=10)
    future_days= (future_date - now).days
    print("Future date after 10 days:", future_date)
    print("Number of days until future date:", future_days)



#simple_date()
#time_functions()
Timedelta()