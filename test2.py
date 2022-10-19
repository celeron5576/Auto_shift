import datetime

a = datetime.time(9,0)
b = datetime.time(15,30)


temp_time = int(a.strftime('%H')) + (int(b.strftime('%M'))/60)

print(temp_time)