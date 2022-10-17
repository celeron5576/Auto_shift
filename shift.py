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
start_working = [[0 for i in range(col - 3)] for j in range(10)]
end_working = [[0 for i in range(col - 3)] for j in range(10)]
syukkinn_kanou = [[0 for i in range(col - 3)] for j in range(10)]
syukkinn_kanoubi = [[],[],[],[],[],[],[],[],[],[]]
a = 1
count = [0,0,0,0,0,0,0,0,0,0]


shift_start = [[0 for i in range(col - 3)] for j in range(2)]
shift_end = [[0 for i in range(col - 3)] for j in range(2)]
shift_people = [[0 for i in range(col - 3)] for j in range(2)]


a = 1
for i in range(10):
    #print(df.loc[a][4])
    #print(df.at[a,"レベル(1~4)"])
    #if df.at[a,"レベル(1~4)"] == "nan":
    #    print("レベルを入力してください！")
    #    sys.exit()
    #シフトが入力された部分のみを繰り返す。欠損値じゃなければ出勤可能日カウントを1増やす
    for n in range(col - 3):
        #print(df.iat[a-1,n+3])
        #print(df.iat[a-1,n+3])
        if not (pd.isnull(df.iat[a-1,n+3])):
            #print(df.iloc[a-1,n+3])
            count[i] += 1
            start_working[i][n] = df.iloc[a-1,n+3]
            end_working[i][n] = df.iloc[a,n+3]
    a += 2

countt = count


for aa in range(10):
    for aaa in range(col - 3):
        if start_working[aa][aaa] != 0:
            syukkinn_kanou[aa][aaa] = 1
            syukkinn_kanoubi[aa].append(aaa)

#shift_start = shift_end = end_working = start_working

def main():
    print(countt)
    """
    #宣言&初期化
    a = 1
    count = [0,0,0,0,0,0,0,0,0,0]


    
    start_working = []
    end_working = []
    temp_working = []

    for d in range(col-4):
        temp_working.append(d)
    for c in range(10):
        start_working.append(temp_working)
        end_working.append(temp_working)
    print(start_working)
    

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
"""

    ####################################################################################
    #もし出勤可能日が営業日÷7より小さければマークをつける
    #出勤可能日が営業日より少ないかどうかの配列(less_people)を用意し、0で初期化（例:[0,0,0,0,0,0,0,0,0,0,0,0]
    #countには従業員ごとの出勤可能日数が入っている
    ####################################################################################
    less_people,temp_less = less_people_bool(countt)
    print("#################################################")
    print(less_people)
    print(temp_less)
    print("#################################################")

    ####################################################################################
    #出勤可能日が一定値以下の人を取り出してシフトに入れるプログラム
    #less_peopleに閾値以下の物がある限り繰り返し続ける(0以外)
    #閾値以下かどうかの配列 countt を使う。[0,1,1,1,0,0,0,0,0,0]
    #less_peopleには閾値以下の人が何番目かを入れておく[1,4,6,7](n番目の人が閾値以下といった感じ)
    #シフトに入れるかどうかを判定し、入れたら入れる。
    #counttとless_peopleの値を減らしていって全部0(もう入れない)になったら配列を終わる
    ####################################################################################
    while(1 in less_people):
        for g in range(len(temp_less)):
            temp_number = random.choice(temp_less)
            temp_less.remove(temp_number)
            shift_in(temp_number)
            print("!")
        count = shift_count(start_working)
        #print("#############################")
        #print(less_people)
        #print(temp_less)
        #print("#############################")
        less_people,temp_less = less_people_bool(count)
    print(count)
    print(less_people)
    print(temp_less)
    print(shift_start)
    print(shift_people)
    #print(start_working)
    #print(end_working)




####################################################################################
#残りの人をシフトに入れるプログラム
#基本的な仕組みとしては閾値以下の人の処理と同じ
#
####################################################################################
    count = [0,0,0,0,0,0,0,0,0,0]
    more_people = [0,0,0,0,0,0,0,0,0,0]
    for k in range(len(start_working)):
        for l in range(col - 3):
            if start_working[k][l] != 0:
                count[k] += 1


    more_people,temp_more = more_people_bool(count)

    print(more_people)
    print(temp_more)
    print(count)


    while(1 in more_people):
        for g in range(len(temp_more)):
            temp_number = random.choice(temp_more)
            temp_more.remove(temp_number)
            shift_in(temp_number)
            print("#")
        count = shift_count(start_working)
        print("#")
        #print("#############################")
        #print(less_people)
        #print(temp_less)
        #print("#############################")
        more_people,temp_more = more_people_bool(count)
    print(count)
    print(more_people)
    print(temp_more)
    print(shift_start)
    print(shift_people)
"""
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
"""

####################################################################################
#出勤可能日をカウントする関数
####################################################################################
def shift_count(shift):
    #print(shift)
    #print(col)
    #a = 1
    print("0")
    count = [0,0,0,0,0,0,0,0,0,0]
    for i in range(10):
        print("1")
        for n in range(col - 5):
            print("2")
            #print(df.iat[a-1,n+3])
            #print(df.iat[a-1,n+3])
            #print(shift[i][n])
            if shift[i][n] != 0:
                #print(df.iloc[a-1,n+3])
                count[i] += 1
        #a += 2
    return count

def counttt():
    count = [0,0,0,0,0,0,0,0,0,0]
    for k in range(len(start_working)):
        for l in range(col - 3):
            if start_working[k][l] != 0:
                count[k] += 1


####################################################################################
#出勤可能日が閾値以下かどうかを保存する関数
#0が閾値以上、1が以下
#配列の何番目の人が閾値以下なのかも保存する
####################################################################################
def less_people_bool(less):
    #print(less)
    less_people = [0,0,0,0,0,0,0,0,0,0]
    temp_less = []
    b = 0
    for cou in less:
        if (cou <= int((col-4)/7)) & (cou != 0):
            less_people[b] = 1
            temp_less.append(b)
        if cou == 0:
            less_people[b] = 0
        b += 1
    #print(less_people)
    return less_people,temp_less

####################################################################################
#出勤可能日が少ない人をシフトに入れるプログラム
#引数が n番目の人
#ランダムで出勤可能日を一つ選ぶ
#シフトに入れるか確認
#入れたら入れて、入れなかったら !!!また処理をして!!! 出勤可能日から削除
#入れるまで繰り返す
####################################################################################
def shift_in(people):
    boo = 0
    #print("!!!!!!!!!!!!!!!!!!!!!!!!")
    #print(syukkinn_kanoubi)
    #print(people)
    while(boo == 0):
        temp = random.choice(syukkinn_kanoubi[people])
        #print(temp)
        #print(start_working)
        #print(start_working[people][temp])
        if shift_start[0][temp] == 0:
            shift_start[0][temp] = start_working[people][temp]
            shift_end[0][temp] = end_working[people][temp]
            shift_people[0][temp] = people + 1
            boo = 1
        elif shift_start[1][temp] == 0:
            shift_start[1][temp] = start_working[people][temp]
            shift_end[1][temp] = end_working[people][temp]
            shift_people[1][temp] = people + 1
            boo = 1
        syukkinn_kanou[people][temp] = 0
        #print(start_working)
        start_working[people][temp] = 0
        end_working[people][temp] = 0
        syukkinn_kanoubi[people].remove(temp)
        if not (1 in syukkinn_kanou):
            boo = 1
    


def more_people_bool(more):
    #print(less)
    more_people = [0,0,0,0,0,0,0,0,0,0]
    temp_more = []
    b = 0
    for cou in more:
        if (cou >= int((col-4)/7)):
            more_people[b] = 1
            temp_more.append(b)
        if cou == 0:
            more_people[b] = 0
        b += 1
    #print(less_people)
    return more_people,temp_more





if __name__ == "__main__":
    main()