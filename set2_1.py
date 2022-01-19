day=int(input('No. of days: '))
year=int(day//365)
rem_day1=day%365
month=int(rem_day1//30)
rem_day2=rem_day1%30
week=rem_day2//7
days=rem_day2%7
print(year,' year(s), ',month,' month(s), ',week,' week(s), ',days,' day(s).')

