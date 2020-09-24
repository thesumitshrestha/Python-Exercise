import calendar

y = int(raw_input("Enter year: "))
m = int(raw_input("Enter month: "))
calendars = calendar.month(y, m)
print calendars
