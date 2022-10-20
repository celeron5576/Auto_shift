import datetime

test = [1, 0, 0, 1, 0, 1, 3, 0, 1, 1, 0, 3, 1, 0, 3, 0, 0, 0, 0, 0, 0, 0]
test2 = [datetime.time(8, 0), 0, 0, datetime.time(8, 0), 0, datetime.time(8, 0), datetime.time(8, 0), 0, datetime.time(8, 0), datetime.time(8, 0), 0, datetime.time(8, 0), datetime.time(8, 0), 0, datetime.time(8, 0), 0, 0, 0, 0, 0, 0, 0]
testtt = 0
testttt = []
test222 = []

for testt in test:
    if testt == 0:
        testttt.append(testtt+2)
    testtt += 1

b = 0
for test22 in test2:
    if test22 == 0:
        test222.append(b+2)
    b += 1


print(testttt)
print(test222)