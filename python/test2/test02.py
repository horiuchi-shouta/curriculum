while True:
    try:
        print()
        print('1: ValueError例外を発生')
        print('2: IndexError例外を発生')
        print('3: 例外を発生させない')
        print('4: 終了')
        number = int(input('選択してください。: '))
        #input関数とは、ユーザーがキーボードに入力したデータを受け付けるための関数
        
        
    except ValueError as e:
        print(e.args)
        continue

        # 問①：if文を用いて、以下の画像のように処理されるように記述しましょう。
    if number==4:
        print('終了します')
        break

    elif number==1:
        
        print('↓')
        print('ValueError')
        print(e.args)
        print('↓')
        print('もう一度選択しましょう')

    else:
        print('１以外')
    

    # 問②：else節を用いて、以下の画像のように処理されるように記述しましょう。
    ##ここに書く

print('↓')
print('無限ループを終了します')