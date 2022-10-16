import pandas as pd
import sys
import random
import numpy as np


#print(pd.__version__)

df = pd.read_excel('test_shift.xlsx' ,sheet_name=0 ,index_col=0)

#宣言&初期化
a = 1
col = len(df.columns)
count = [0,0,0,0,0,0,0,0,0,0]
less_people = [0,0,0,0,0,0,0,0,0,0]


start_working = []
end_working = []
temp_working = []

for d in range(10):
    for c in range(20):
        temp_working.append(0)
    start_working.append(temp_working)
    end_working.append(temp_working)
    temp_working = []
    
"""
start_working = []
end_working = []
temp_working = []

for d in range(col-4):
    temp_working.append(d)
for c in range(10):
    start_working.append(temp_working)
    end_working.append(temp_working)
print(start_working)
"""

#start_working = np.zeros((10 ,col-4))
#end_working = np.zeros((10 ,col-4))

####################################################################################
#何日シフトに入れるかを取得するプログラム
#変数aはa人目のこと
#最大10人しか考えられてない(簡単に再利用できるように改善予定)
#もしレベルを入力していなかったらエラーを出すようにした
####################################################################################
for i in range(10):
    #print(df.loc[a][4])
    #print(df.at[a,"レベル(1~4)"])
    if df.at[a,"レベル(1~4)"] == "nan":
        print("レベルを入力してください！")
        sys.exit()
    #シフトが入力された部分のみを繰り返す。欠損値じゃなければ出勤可能日カウントを1増やす
    for n in range(col - 4):
        #print(df.iat[a-1,n+3])
        print(df.iat[a-1,n+3])
        if not (pd.isnull(df.iat[a-1,n+3])):
            count[a-1] += 1
            start_working[i][n] = df.iloc[a-1,n+3]
            end_working[i][n] = df.iloc[i+1,n+3]
    a += 1


####################################################################################
#もし出勤可能日が営業日÷7より小さければマークをつける
####################################################################################
b = 0
print(col)
for counter in count:
    if counter <= int((col-4)/7):
        less_people[b] = 1
    b += 1

print(count)
print(less_people)
#print(start_working)
#print(end_working)


array1 = [1,2,3,4,5,6,7,8,9,0]
array2 = []
for i in array1:
    if i != 0:
        array2.append(i)
        print(array2)

arr1 = [1, 2, 3]
arr2 = [4, 5, 6]
arr3 = []

flag_temp = []
for less_temp in less_people:
    if less_temp == 1:
        flag_temp.append[0]

#arr1はa以上出勤可能日があるかのやつ
while(0 in flag_temp):
    for e in arr1:
        for f in int((col-4)/7):
            if e == 1:
                val = random.choice(array2)
                arr3.append(val)
                arr2.remove(val)
                flag_temp[f] = 1
