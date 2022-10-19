while True:
    try:
        print()
        print('1: ValueError例外を発生')
        print('2: IndexError例外を発生')
        print('3: 例外を発生させない')
        print('4: 終了')
        number = int(input('選択してください。: '))
        # 問①：if文を用いて、以下の画像のように処理されるように記述しましょう。
    if number <=1:
        print('ValueError例外を発生')
    except ValueError as IndexError:
        continue
    # 問②：else節を用いて、以下の画像のように処理されるように記述しましょう。
    elif number <=2:
        print('IndexError例外を発生')
    elif number <=3:
        print('例外を発生させませんでした')
    else:
        print('終了します')
        break

#        except ValueError as IndexError:
#        print('ValueError')
#        continue

    ##ここに書く
   
   
#    try:
#        number = int(input('10までの数値を入力してください: '))
#        # 問①：ValueError例外を処理するコードを記述してください。
#        print('数字以外が入力されました。数字のみを入力してください')
#
#        continue
#    if answer< number:   #10<number
#        print('もっと小さな数値です')
#    elif number < answer: # number<10
#        print('もっと大きな数値です')
 #   else:
 #       break
print('↓')
print('無限ループを終了します')