####################################################################################
#シフト表を自動で作ってくれるプログラム
#
#課題
#10:00~15:30の間で1人しかシフトに入っていないことがあったら入れる処理
#15:00~15:30にlevel5が入っているかの処理
#10:00~15:00に2人以上入っているかの処理
#中途半端だったり、短時間のシフト処理
#14:00~15:30にはlevel4が入っていたら一人で良いという処理
#コードがぐちゃぐちゃだから書き直し
####################################################################################
import pandas as pd
import random
import datetime
import copy
import time
import statistics


####################################################################################
#col : 列数
#df：読み込むシフト表
#level：従業員のレベル
#people_shift_number_temp：従業員が何日目にシフトに入るかを入れる配列
#people_shift_number_temp_temp：同上
#people_shift_number：同上
#user_name：従業員の名前
#count：何日シフトに入るかをカウントする配列
#countt:同上
#shift_start：何時からシフトに入るか
#shift_end：何時までシフトに入るか
#shift_people：誰がシフトに入るか
#start_working：従業員ごとの出勤可能時間のはじめ
#end_working：従業員ごとの出勤可能時間の終わり
#less_people：出勤可能日が一定数以下かを入れる変数 0が以上1が未満
#syukkinn_kanou：
#syukkinn_kanoubi：

####################################################################################


time_sta = time.time()



penalty_temp = 1000000


#print(pd.__version__)

#excelの読み込み
df = pd.read_excel('test_shift.xlsx' ,sheet_name=0 ,index_col=0)
cycle_number = int(df.iloc[24][13])
col = len(df.columns)
week = ["月" ,"火" ,"水" ,"木" ,"金" ,"土" ,"日"]
people_shift_number_temp = [[] ,[] ,[] ,[] ,[] ,[] ,[] ,[] ,[] ,[]]
level = [0,0,0,0,0,0,0,0,0,0]
user_name = []
user_status = list(df.index)
for m in range(10):
    level[m] = df.iloc[(m * 2)][1]
    user_name.append(df.iloc[(m * 2)][0])


########################################################################################################################################################################
########################################################################################################################################################################
########################################################################################################################################################################
########################################################################################################################################################################


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
        if (cou <= int((col-3)/7)) and (cou != 0):
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
        #print(people)
        #print(syukkinn_kanoubi)
        #print(people)
        #print(syukkinn_kanoubi)
        tekito = 0
        temp = random.choice(syukkinn_kanoubi[people])#############################################エラー起きる!!!!!!!!!!!!!!!!
        if shift_start[0][temp] == 0:
            shift_start[0][temp] = start_working[people][temp]
            shift_end[0][temp] = end_working[people][temp]
            shift_people[0][temp] = people + 1
            boo = 1
            tekito = 0
        elif shift_start[1][temp] == 0:
            #people何人目か どこのシフトか どのレベルか
            people,tekito = level_bool(level[people] ,people ,temp)
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
        if tekito == 1:
            tekito = "sono"
    return people ,tekito

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



"""
def level_bool(level1 ,o ,temp):
    if ((level1 + level[o]) >= 5) and (shift_people[1][temp] == 0) and (o != shift_people[0][temp]):
        return o
    else:
        ####################################################################################
        #他のレベルの人を入れる処理
        ####################################################################################
        for n in range(len(start_working)):
            if start_working[n][temp] != 0:
                if (level1 + level[n]) >= 5:
                    if (n != o):
                        return n
        for n in range(len(start_working)):
            if start_working[n][temp] != 0:
                if (n != o):
                    shift_start[n][temp] = start_working[n][temp]
                    shift_end[n][temp] = end_working[n][temp]
                    shift_people[n][temp] = n + 1
                    return n
        return o
"""

def level_bool(level1 ,o ,temp):
    if (level1 + level[o]) >= 5:
        return o,0
    else:
        for n in range(len(start_working)):
            if start_working[n][temp] != 0:
                if (level1 + level[n]) >= 5:
                    return n,1
        return o,0


####################################################################################
#
####################################################################################
def time_bool():
    for p in range(col - 3):
        if (shift_start[0][p] != 0) and (shift_start[1][p] != 0):
            if shift_start[0][p] >= shift_start[1][p]:
                shift_start_temp = shift_start[1][p]
            else:
                shift_start_temp = shift_start[0][p]
            if shift_end[0][p] >= shift_end[1][p]:
                shift_end_temp = shift_end[1][p]
            else:
                shift_end_temp = shift_end[0][p]
        #はじめも終わりも欠損あり
        if (shift_start_temp > datetime.time(9,0)) and (shift_end_temp < datetime.time(15,30)):
            #print("a")
            a = 0
            for t in end_working_temp:
                if t[p] != 0:
                    if (t[p] <= datetime.time(9,0)) and (t[p] >= datetime.time(15,30)) and (a != (shift_people[0][p] - 1)) and (a != (shift_people[1][p] - 1)):
                        shift_start[2][p] = start_working[a][p]
                        shift_end[2][p] = end_working[a][p]
                        shift_people[2][p] = a + 1
                a += 1
        #初めのほうのみ欠損あり
        if (shift_start_temp > datetime.time(9,0)) and (shift_end_temp >= datetime.time(15,30)):
            #print("b")
            b = 0
            for r in start_working_temp:
                if r[p] != 0:
                    if r[p] <= datetime.time(9,0) and (b != (shift_people[0][p] - 1)) and (b != (shift_people[1][p] - 1)):
                        shift_start[2][p] = start_working[b][p]
                        shift_end[2][p] = end_working[b][p]
                        shift_people[2][p] = b + 1
                b += 1
        #終わりのほうのみ欠損あり
        if  (shift_start_temp <= datetime.time(9,0)) and (shift_end_temp < datetime.time(15,30)):
            c = 0
            for s in end_working_temp:
                if s[p] != 0:
                    if s[p] >= datetime.time(15,30) and (c != (shift_people[0][p] - 1)) and (c != (shift_people[1][p] - 1)):
                        shift_start[2][p] = start_working[c][p]
                        shift_end[2][p] = end_working[c][p]
                        shift_people[2][p] = c + 1
                c += 1

def hyouzi(people_deci ,start_deci ,end_deci):
    temp_date = copy.deepcopy(date)
    #temp_date.append(" ")
    #temp_date.append("お給料")
    shift = pd.DataFrame(columns = user_name ,index = temp_date)

    for n in range(len(start_deci[0])):
        for m in range(3):
            if (start_deci[m][n] != 0) and (people_deci[m][n] != 0):
                shift.iloc[n ,(people_deci[m][n] - 1)] = (start_deci[m][n].strftime("%H:%M") + "～" + end_deci[m][n].strftime("%H:%M"))

    #("Empty Dataframe ", shift, sep='\n')
    #for r in range(len(total_salary)):
    #    #print("Empty Dataframe ", shift, sep='\n')
    #    shift.iloc[len(shift.index) - 1 ,r] = ("約" + str('{:,}'.format(int(total_salary[r] * 1000))) + "円")
        

    shift.to_excel('Auto_shift.xlsx', sheet_name='shift1')


def eval():
    penalty = 0
    for u in range(3):
        for w in range(col - 3):
            if shift_start[u][w] != 0:
                temp_time_start = int(shift_start[u][w].strftime('%H')) + (int(shift_start[u][w].strftime('%M'))/60)            ###################################
                temp_time_end = int(shift_end[u][w].strftime('%H')) + (int(shift_end[u][w].strftime('%M'))/60)
                #total_salary[shift_people[u][w] - 1] += temp_time_end - temp_time_start + 1
                if temp_time_end - temp_time_start >= 7:
                    total_salary[shift_people[u][w] - 1] += temp_time_end - temp_time_start
                    #print(temp_time_end - temp_time_start + 1)
                else:
                    total_salary[shift_people[u][w] - 1] += temp_time_end - temp_time_start + 1
    
    people_shift_binary = [[0 for i in range(col - 3)] for j in range(10)]
    #(shift_people)
    for y in range(3):
        for z in range(col - 3):
            if shift_people[y][z] != 0:
                people_shift_binary[shift_people[y][z]-1][z] = 1
    people_shift_number = [[] ,[] ,[] ,[] ,[] ,[] ,[] ,[] ,[] ,[]]
    temp_shift_binary = 0
    for cd in range(len(people_shift_binary)):
        for ef in range(len(people_shift_binary[0])):
            if people_shift_binary[cd][ef] == 1:
                people_shift_number[cd].append(temp_shift_binary)
            temp_shift_binary += 1
        temp_shift_binary = 0
    
    #print("何日にシフトに入るか:")
    #print(people_shift_number)
    people_shift_number_temp = copy.deepcopy(people_shift_number)
    #print("合計金額/1000")
    #print(total_salary)                                             #############################ここおかしい
    for tot in total_salary:
        penalty += tot / 2

    salary_temp = 0
    for total_salary_temp in total_salary:
        salary_temp += (total_salary_temp * 1000)
    for i in range(len(total_salary)):

        ####################################################################################
        #salary_pullを平均値にするか中央値にするか問題。上が平均値、したが中央値
        ####################################################################################
        #salary_pull[i] = int(salary_temp / len(total_salary)) - (total_salary[i] * 1000)
        salary_pull[i] = (statistics.median(total_salary)) - (total_salary[i] * 1000)
    for i in range(len(salary_pull)):
        if salary_pull[i] <= 3000 and salary_pull[i] >= -3000:
            salary_pull[i] = 0
        elif salary_pull[i] < 0:
            salary_pull[i] = -salary_pull[i] - 3000
        else:
            salary_pull[i] = salary_pull[i] - 3000

    for l in range(len(salary_pull)):
        if (temp_less_people[l] == "1") or (user_status[l] == "社員"):
            salary_pull[l] = 0



    #print(salary_pull)
    for i in salary_pull:
        penalty += i / 200
    
    #print(penalty)

    for i in range(len(people_shift_number)):
        for j in range(len(people_shift_number[i]) - 1):
            if (people_shift_number[i][j + 1] - people_shift_number[i][j]) < 3:
                penalty += (people_shift_number[i][j + 1] - people_shift_number[i][j]) * 60
    
    #print(penalty)
    return penalty ,people_shift_number_temp


def shiage():
    sabunn = [[0 ,0] ,[0 ,0] ,[0 ,0]]
    sabunn_start = 0
    sabunn_end = 0


    for w in range(col - 3):
        if shift_people[2][w] == 0:

            for u in range(3):
                if shift_start[u][w] != 0:
                    temp_time_start = int(shift_start[u][w].strftime('%H')) + (int(shift_start[u][w].strftime('%M'))/60)
                    temp_time_end = int(shift_end[u][w].strftime('%H')) + (int(shift_end[u][w].strftime('%M'))/60)
                    if temp_time_start > 10.0:
                        sabunn[u][0] =  temp_time_start - 10
                    if temp_time_end < 15.0:
                        sabunn[u][1] =  15 - temp_time_end

            for i in range(3):
                sabunn_start += sabunn[i][0]
                sabunn_end += sabunn[i][1]


            if (sabunn_start != 0):
                for p in range(len(shift_people)):
                    if start_working_temp[p][w] != 0:
                        if (start_working_temp[p][w] <= datetime.time(9 ,0)) and (p != (shift_people[0][w] - 1)) and (p != (shift_people[1][w] - 1)):
                                shift_start[2][w] = start_working[p][w]
                                shift_end[2][w] = end_working[p][w]
                                shift_people[2][w] = p + 1

            if (sabunn_end != 0):
                for p in range(len(shift_people)):
                    if start_working_temp[p][w] != 0:
                        if (end_working_temp[p][w] >= datetime.time(15 ,30)) and (p != (shift_people[0][w] - 1)) and (p != (shift_people[1][w] - 1)):
                                shift_start[2][w] = start_working[p][w]
                                shift_end[2][w] = end_working[p][w]
                                shift_people[2][w] = p + 1


            sabunn_start = 0
            sabunn_end = 0


def level_in():                                                                             ############################################################################
    #print("########################")
    #print(len(start_working))
    for temp in range(col - 3):
        #print(temp)
        if shift_people[2][temp] == 0:
            for n in range(len(start_working)):
                #print("########################")
                #print(shift_people[0][temp])
                #print(level[shift_people[0][temp]] + level[shift_people[1][temp]])
                if (level[shift_people[0][temp] - 1] + level[shift_people[1][temp] - 1]) < 5:
                    if (start_working[n][temp] != 0) and (n != (shift_people[0][temp] - 1)) and (n != (shift_people[1][temp] - 1)):
                        shift_start[2][temp] = start_working[n][temp]
                        shift_end[2][temp] = end_working[n][temp]
                        shift_people[2][temp] = n + 1
########################################################################################################################################################################
########################################################################################################################################################################
########################################################################################################################################################################
########################################################################################################################################################################

shift_start_deci = [[0 for i in range(col - 3)] for j in range(3)]
shift_end_deci = [[0 for i in range(col - 3)] for j in range(3)]
shift_people_deci = [[0 for i in range(col - 3)] for j in range(3)]


for cycle in range(cycle_number):
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


    total_salary = []
    salary_pull = []
    for x in range(10):
        if not (pd.isnull(df.iat[x * 2 ,0])):
            total_salary.append(0)
            salary_pull.append(0)

    shift_start = [[0 for i in range(col - 3)] for j in range(3)]
    shift_end = [[0 for i in range(col - 3)] for j in range(3)]
    shift_people = [[0 for i in range(col - 3)] for j in range(3)]

    #shift_start_deci = [[0 for i in range(col - 3)] for j in range(3)]
    #shift_end_deci = [[0 for i in range(col - 3)] for j in range(3)]
    #shift_people_deci = [[0 for i in range(col - 3)] for j in range(3)]

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




    ####################################################################################
    #もし出勤可能日が営業日÷7より小さければマークをつける
    #出勤可能日が営業日より少ないかどうかの配列(less_people)を用意し、0で初期化（例:[0,0,0,0,0,0,0,0,0,0,0,0]
    #countには従業員ごとの出勤可能日数が入っている
    ####################################################################################
    less_people,temp_less = less_people_bool(countt)
    temp_less_people = copy.deepcopy(less_people)
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



    
    """
    levelone = [0,0,0,0,0,0,0,0,0,0]
    temp_one = 0
    for level1 in range(len(start_working)):
        if level[level1] == 1 and temp_less_people[level1] == 0:
            levelone[level1] = 1
            levelone_number.append(temp_one)
        temp_one += 1

    
    while 1 in bool_one:
        for level1 in levelone:
            temp_one_temp = copy.deepcopy(temp_one)
    """



    ####################################################################################
    #残りの人をシフトに入れるプログラム
    #基本的な仕組みとしては閾値以下の人の処理と同じ
    #
    #########################################
    # ###########################################
    count = [0,0,0,0,0,0,0,0,0,0]
    more_people = [0,0,0,0,0,0,0,0,0,0]
    for k in range(len(start_working)):
        for l in range(col - 3):
            if start_working[k][l] != 0:
                count[k] += 1


    more_people,temp_more = more_people_bool(count)

    syukkinn_kanou_temp = copy.deepcopy(syukkinn_kanou)
    syukkinn_kanoubi_temp = copy.deepcopy(syukkinn_kanoubi)

    while(1 in more_people):
        for g in range(len(temp_more)):
            #print("!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            #print(temp_more)
            temp_number = random.choice(temp_more)
            #print(temp_number)
            #print("############################")
            temp_number_temp ,tekito = shift_in(temp_number)                                   #エラー起きる！！！！！！！！！！！！！！！！！！！
            #print(temp_number_temp)
            #print(temp_more)
            if temp_number_temp in temp_more:
                temp_more.remove(temp_number_temp)
            #if len(temp_more[temp_number_temp]) != 0:
            elif temp_number == temp_number_temp and tekito != "sono":
                temp_more.remove(temp_number_temp)
                #print(temp_number)
        count = shift_count(start_working)
        #print(count)
        more_people,temp_more = more_people_bool(count)
        #print("****************************************")
        #print(more_people)
        #print(temp_more)
        #print("****************************************")
    

    start_working = copy.deepcopy(start_working_temp)
    end_working = copy.deepcopy(end_working_temp)
    syukkinn_kanou = syukkinn_kanou_temp
    syukkinn_kanoubi = syukkinn_kanoubi_temp


    level_in()
    time_bool()
    shiage()

    print("処理中")



    for i in range(3):
        for a in range(len(shift_start[0])):
            if shift_start_deci[i][a] != 0:
                if shift_start_deci[i][a] < datetime.time(8 ,0):
                    shift_start_deci[i][a] = datetime.time(8 ,0)
                if shift_end_deci[i][a] > datetime.time(15 ,30):
                    shift_end_deci[i][a] = datetime.time(15 ,30)


    penalty ,people_shift_number_temp = eval()


    if penalty < penalty_temp:
        shift_people_deci =  copy.deepcopy(shift_people)
        shift_start_deci = copy.deepcopy(shift_start)
        shift_end_deci =  copy.deepcopy(shift_end)
        total_salary_deci = copy.deepcopy(total_salary)
        people_shift_number_temp_temp = copy.deepcopy(people_shift_number_temp)
        #print(people_shift_number_temp_temp)
        penalty_temp = penalty

        aaa = []
        for a in people_shift_number_temp_temp:
            aaa.append(len(a) * 8.5)
        #print(aaa)




    if cycle == cycle_number - 1:
        print(penalty_temp)
        print(total_salary_deci)
        print(shift_people_deci)
        #print(shift_start)
        #print(shift_start_deci)
        hyouzi(shift_people_deci ,shift_start_deci ,shift_end_deci)





time.sleep(1)
time_end = time.time()
# 経過時間（秒）
tim = time_end - time_sta

print(tim)