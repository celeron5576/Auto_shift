import numpy as np
arr = np.zeros((20,15))

print(arr)


col = 20


start_working = []
end_working = []
temp_working = []

for d in range(col-4):
    temp_working.append(d)
for c in range(10):
    start_working.append(temp_working)
    end_working.append(temp_working)


test = [0,0,1,1,1,0,0,0]

n = 0
for test_temp in test:
    if test_temp == 1:
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print(test_temp)
        print(arr[0][n])
        arr[0][n] = 1
    n += 1

print(arr)