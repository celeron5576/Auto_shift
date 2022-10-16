import pandas as pd
import sys
import random




#print(pd.__version__)

#excelの読み込み
df = pd.read_excel('test_shift.xlsx' ,sheet_name=0 ,index_col=0)
col = len(df.columns)
print(col)
start_working = []
temp_working = []
end_working = []
shift_start = []
shift_end = []


#出勤可能日の開始時間と終了時間を配列で表す。配列はすべて0で埋めて初期化
#横の列が日ごとの出勤開始時間(終了時間)、縦の列が人(Aさん、Bさん、Cさん、Dさん、、、)
start_working = [[0 for i in range(20)] for j in range(10)]
end_working = [[0 for i in range(20)] for j in range(10)]
shift_start = [[0 for i in range(20)] for j in range(10)]
shift_end = [[0 for i in range(20)] for j in range(10)]


#shift_start = shift_end = end_working = start_working

def main():
    #宣言&初期化
    a = 1
    count = [0,0,0,0,0,0,0,0,0,0]


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
    #start_working end_workingに出勤可能日の開始時間、終了時間を入れるプログラム

    #変数aはa人目のこと
    #最大10人しか考えられてない(簡単に再利用できるように改善予定)
    #もしレベルを入力していなかったらエラーを出すようにした
    ####################################################################################
    #print(df.iloc[0][3])
    #print(df.iloc[1][3])
    a = 1
    for i in range(10):
        #print(df.loc[a][4])
        #print(df.at[a,"レベル(1~4)"])
        #if df.at[a,"レベル(1~4)"] == "nan":
        #    print("レベルを入力してください！")
        #    sys.exit()
        #シフトが入力された部分のみを繰り返す。欠損値じゃなければ出勤可能日カウントを1増やす
        for n in range(col - 4):
            #print(df.iat[a-1,n+3])
            #print(df.iat[a-1,n+3])
            if not (pd.isnull(df.iat[a-1,n+3])):
                #print(df.iloc[a-1,n+3])
                count[i] += 1
                start_working[i][n] = df.iloc[a-1,n+3]
                end_working[i][n] = df.iloc[a,n+3]
        a += 2


    ####################################################################################
    #もし出勤可能日が営業日÷7より小さければマークをつける
    #出勤可能日が営業日より少ないかどうかの配列(less_people)を用意し、0で初期化（例:[0,0,0,0,0,0,0,0,0,0,0,0]
    #countには従業員ごとの出勤可能日数が入っている
    ####################################################################################
    less_people,temp_less = less_people_bool(count)
    print(less_people)
    print(temp_less)

    ####################################################################################
    #出勤可能日が一定値以下の人を取り出すプログラム
    ####################################################################################
    while(1 in less_people):
        for g in range(len(temp_less)):
            temp_number = random.choice(temp_less)
            temp_less.remove(temp_number)
        count = shift_count(start_working)
        less_people,temp_less = less_people_bool(count)
    print(count)
    print(less_people)
    print(temp_less)
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


def shift_count(shift):
    print(shift)
    print(col)
    a = 1
    count = [0,0,0,0,0,0,0,0,0,0]
    for i in range(10):
        for n in range(col - 5):
            #print(df.iat[a-1,n+3])
            #print(df.iat[a-1,n+3])
            print(shift[i][n])
            if not (pd.isnull(shift[i][n])):
                #print(df.iloc[a-1,n+3])
                count[i] += 1
        a += 2

def less_people_bool(less):
    less_people = [0,0,0,0,0,0,0,0,0,0]
    temp_less = []
    b = 0
    for cou in less:
        if cou <= int((col-4)/7):
            less_people[b] = 1
            temp_less.append(b)
        b += 1
    return less_people,temp_less


if __name__ == "__main__":
    main()