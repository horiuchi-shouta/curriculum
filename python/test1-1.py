#問題2　問１―１
# int型のリストdataを作成し、値を1,3,5,7で初期化
int=(1,3,5,7)
for i in(1,3,5,7):
    print(i**2)
#問題1　問１―2
for j in range(1,8,2):
    print(j**2)


#問題2　問2-1
all_place = ["札幌","東京","横浜","大阪","名古屋","福岡"]
wait_place = ["札幌","大阪"]
get_place = ["横浜"]

for place in all_place:
    if place in get_place:
        print(place + "のチケットが当選しました！")
    elif place in wait_place:
        print(place + "のチケットは結果待ち")
    else:
        print(place + "のチケットは落選しました")

#問題2　問2-1

s = "{0}と{1}と{2}のチケットが当選しました！".format("札幌","大阪","横浜")
print(s)