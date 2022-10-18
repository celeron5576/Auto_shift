import pandas as pd
import sys
import random
import datetime
import copy

#print(pd.__version__)

#excelの読み込み
df = pd.read_excel('test_shift.xlsx' ,sheet_name=0 ,index_col=0)
col = len(df.columns)
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


shift_start = [[0 for i in range(col - 3)] for j in range(3)]
shift_end = [[0 for i in range(col - 3)] for j in range(3)]
shift_people = [[0 for i in range(col - 3)] for j in range(3)]

week = ["月" ,"火" ,"水" ,"木" ,"金" ,"土" ,"日"]

a = 1
for i in range(10):
    #シフトが入力された部分のみを繰り返す。欠損値じゃなければ出勤可能日カウントを1増やす
    for n in range(col - 3):
        if not (pd.isnull(df.iat[a-1,n+3])):
            count[i] += 1
            start_working[i][n] = df.iloc[a-1,n+3]
            end_working[i][n] = df.iloc[a,n+3]
    a += 2

countt = count

start_working_temp = copy.deepcopy(start_working)
end_working_temp = copy.deepcopy(end_working)

level = [0,0,0,0,0,0,0,0,0,0]
user_name = []
for m in range(10):
    level[m] = df.iloc[(m * 2)][1]
    user_name.append(df.iloc[(m * 2)][0])


date = list(df.columns)
del date[:3]
for t in range(len(date)):
    week_temp = date[t].weekday()
    date[t] = date[t].strftime("%m月%d日" + "(" + week[week_temp] + ")")

for aa in range(10):
    for aaa in range(col - 3):
        if start_working[aa][aaa] != 0:
            syukkinn_kanou[aa][aaa] = 1
            syukkinn_kanoubi[aa].append(aaa)


def main():
    ####################################################################################
    #もし出勤可能日が営業日÷7より小さければマークをつける
    #出勤可能日が営業日より少ないかどうかの配列(less_people)を用意し、0で初期化（例:[0,0,0,0,0,0,0,0,0,0,0,0]
    #countには従業員ごとの出勤可能日数が入っている
    ####################################################################################
    less_people,temp_less = less_people_bool(countt)

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
        count = shift_count(start_working)
        less_people,temp_less = less_people_bool(count)
    #print(count)
    #print(less_people)
    #print(temp_less)
    #print(shift_start)
    #print(shift_people)
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

    #print(more_people)
    #print(temp_more)
    #print(count)


    while(1 in more_people):
        for g in range(len(temp_more)):
            temp_number = random.choice(temp_more)
            temp_more.remove(temp_number)
            #print(temp_number)
            shift_in(temp_number)                                   #エラー起きる！！！！！！！！！！！！！！！！！！！
        count = shift_count(start_working)
        #print("#############################")
        #print(less_people)
        #print(temp_less)
        #print("#############################")
        more_people,temp_more = more_people_bool(count)
    print(count)
    print(more_people)
    print(temp_more)
    print(shift_start)
    print(shift_end)
    print(shift_people)


    hyouzi()

####################################################################################
#出勤可能日をカウントする関数
####################################################################################
def shift_count(shift):
    count = [0,0,0,0,0,0,0,0,0,0]
    for i in range(10):
        for n in range(col - 3):
            if shift[i][n] != 0:
                count[i] += 1
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
        if (cou <= int((col-3)/7)) & (cou != 0):
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
    while(boo == 0):
        print(people)
        print(syukkinn_kanoubi)
        temp = random.choice(syukkinn_kanoubi[people])#############################################エラー起きる!!!!!!!!!!!!!!!!
        if shift_start[0][temp] == 0:
            shift_start[0][temp] = start_working[people][temp]
            shift_end[0][temp] = end_working[people][temp]
            shift_people[0][temp] = people + 1
            boo = 1
        elif shift_start[1][temp] == 0:
            people = level_bool(level[people] ,people ,temp)
            shift_start[1][temp] = start_working[people][temp]
            shift_end[1][temp] = end_working[people][temp]
            shift_people[1][temp] = people + 1
            boo = 1
        syukkinn_kanou[people][temp] = 0
        start_working[people][temp] = 0
        end_working[people][temp] = 0
        syukkinn_kanoubi[people].remove(temp)
        if not (1 in syukkinn_kanou):
            boo = 1

def shift_in_adjust(people,temp):
    if shift_start[0][temp] == 0:
        shift_start[0][temp] = start_working[people][temp]
        shift_end[0][temp] = end_working[people][temp]
        shift_people[0][temp] = people + 1
    elif shift_start[1][temp] == 0:
        people = level_bool(level[people] ,people ,temp)
        shift_start[1][temp] = start_working[people][temp]
        shift_end[1][temp] = end_working[people][temp]
        shift_people[1][temp] = people + 1

def more_people_bool(more):
    more_people = [0,0,0,0,0,0,0,0,0,0]
    temp_more = []
    b = 0
    for cou in more:
        if (cou >= 1):
            more_people[b] = 1
            temp_more.append(b)
        if cou == 0:
            more_people[b] = 0
        b += 1
    return more_people,temp_more

def level_bool(level1 ,o ,temp):
    if (level1 + level[o]) >= 5:
        return o
    else:
        for n in range(len(start_working)):
            if start_working[n][temp] != 0:
                if (level1 + level[n]) >= 5:
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    o = n
                    return o
        for n in range(len(start_working)):
            if start_working[n][temp] != 0:
                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                shift_start[2][temp] = start_working[n][temp]
                shift_end[2][temp] = end_working[n][temp]
                shift_people[2][temp] = n + 1
                return o
        return o


####################################################################################
#
####################################################################################
def time_bool():
    for p in range(col - 3):
        if (shift_start[0][p] != 0) & (shift_start[1][p] != 0):
            if shift_start[0][p] >= shift_start[1][p]:
                shift_start_temp = shift_start[1][p]
            else:
                shift_start_temp = shift_start[0][p]
            if shift_end[0][p] >= shift_end[1][p]:
                shift_end_temp = shift_end[1][p]
            else:
                shift_end_temp = shift_end[0][p]
        #はじめも終わりも欠損あり
        if (shift_start_temp > datetime.time(9,0)) & (shift_end_temp < datetime.time(15,30)):
            for t in end_working_temp:
                if t[p] != 0:
                    if (t[p] <= datetime.time(9,0)) & (t[p] >= datetime.time(15,30)) & (t != (shift_people[0][p] - 1)) & (t != (shift_people[1][p] - 1)):
                        shift_start[0][p] = start_working[t][p]
                        shift_end[0][p] = end_working[t][p]
        #初めのほうのみ欠損あり
        if (shift_start_temp > datetime.time(9,0)) & (shift_end_temp >= datetime.time(15,30)):
            for r in start_working_temp:
                if r[p] != 0:
                    if r[p] <= datetime.time(9,0) & (t != (shift_people[0][p] - 1)) & (t != (shift_people[1][p] - 1)):
                        shift_start[0][p] = start_working[t][p]
                        shift_end[0][p] = end_working[t][p]
        #終わりのほうのみ欠損あり
        if  (shift_start_temp <= datetime.time(9,0)) & (shift_end_temp < datetime.time(15,30)):
            for s in end_working_temp:
                if s[p] != 0:
                    if s[p] >= datetime.time(15,30) & (t != (shift_people[0][p] - 1)) & (t != (shift_people[1][p] - 1)):
                        shift_start[0][p] = start_working[t][p]
                        shift_end[0][p] = end_working[t][p]

def hyouzi():
    shift = pd.DataFrame(columns=user_name ,index= date)

    print(shift_start)
    print(shift_people)
    for n in range(len(shift_start[0])):
        for m in range(3):
            if (shift_start[m][n] != 0) & (shift_people[m][n] != 0):
                shift.iloc[n ,(shift_people[m][n] - 1)] = (shift_start[m][n].strftime("%H:%M") + "～" + shift_end[m][n].strftime("%H:%M"))

    print("Empty Dataframe ", shift, sep='\n')

    shift.to_excel('Auto_shift.xlsx', sheet_name='shift1')


    
if __name__ == "__main__":
    main()