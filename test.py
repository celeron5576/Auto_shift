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

for d in range(20):
    c.append(0)
for e in range(10):
    a.append(c)
    b.append(c)

print("書き換える前")
print("a:" + str(a))
print("b:" + str(b))
print("")
print("")

test = [0,0,1,1,1,0,0,1,1,0,1,1,1,0,0,1]

n = 0
for test_temp in test:
    if test_temp == 1:
        a[0][n] = 1
    n += 1

print("書き換え後")
print("a:" + str(a))
print("b:" + str(b))