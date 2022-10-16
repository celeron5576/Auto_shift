######################################################
# 20×10　の二次元配列 a b を用意し、0で初期化
# testという配列を用意し、for文でtest配列を回す。
#test配列のn番目の要素が1の時、二次元配列のaの1個めのn要素を1に書き換える
#
#するとなぜかa配列aの1番目以外の要素も書き換えられてしまう。
#そのほかにもb配列の要素も書き換えられる。
######################################################
a = []
b = []
c = []

#20×10の配列を0で初期化
#for d in range(20):
#    c.append(0)
#for e in range(10):
#    a.append(c)
#    b.append(c)

a = [[0 for i in range(20)] for j in range(10)]
b = [[0 for i in range(20)] for j in range(10)]

#書き換え前の配列を出力
print("書き換える前")
print("a:" + str(a))
print("b:" + str(b))
print("")
print("")

a[1][2]=999

#配列を初期化
test = [0,0,1,1,1,0,0,1,1,0,1,1,1,0,0,1]


#配列aの0個めの要素を書き換え
n = 0
for test_temp in test:
    if test_temp == 1:
        a[0][n] = 1
    n += 1


#書き換え後の配列を出力
print("書き換え後")
print("a:" + str(a))
print("b:" + str(b))

print(a[0][3])
print(a[1][3])
