import datetime

a = datetime.time(8,0)
b = datetime.time(15,30)


temp_time1 = int(a.strftime('%H')) + (int(a.strftime('%M'))/60)
temp_time2 = int(b.strftime('%H')) + (int(b.strftime('%M'))/60)

temp_time = temp_time2 - temp_time1

print(temp_time)