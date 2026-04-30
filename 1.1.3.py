from datetime import date
date1 = input()
date2 = input()
y1,m1,d1 = map(int,date1.split('-'))
y2,m2,d2 = map(int,date2.split('-'))
d_1 = date(y1,m1,d1)
d_2 = date(y2,m2,d2)
date_diff = d_2 - d_1
print(date_diff.days)