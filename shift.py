import pandas as pd
import sys

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

for d in range(col-4):
    temp_working.append(0)
for c in range(10):
    start_working.append(temp_working)
    end_working.append(temp_working)

####################################################################################
#何日シフトに入れるかを取得するプログラム
#変数aはa人目のこと
#最大10人しか考えられてない(簡単に再利用できるように改善予定)
#もしレベルを入力していなかったらエラーを出すようにした
####################################################################################
for i in range(10):
    print(df.loc[a])
    #print(df.at[a,"レベル(1~4)"])
    if df.at[a,"レベル(1~4)"] == "nan":
        print("レベルを入力してください！")
        sys.exit()
    #シフトが入力された部分のみを繰り返す。欠損値じゃなければ出勤可能日カウントを1増やす
    for n in range(col - 4):
        #print(df.iat[a-1,n+3])
        if not (pd.isnull(df.iat[a-1,n+3])):
            count[a-1] += 1
            start_working[a-1][n] = df.iat[a-1,n+3]
            print(start_working[a-1][n])
    a += 1

b = 0
print(col)
for counter in count:
    if counter <= int((col-4)/7):
        less_people[b] = 1
    b += 1

print(count)
print(less_people)
print(start_working)