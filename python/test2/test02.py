while True:
    try:
        print()
        print('1: ValueError例外を発生')
        print('2: IndexError例外を発生')
        print('3: 例外を発生させない')
        print('4: 終了')
        number = int(input('選択してください。: '))
       
    # 問①：if文を用いて、以下の画像のように処理されるように記述しましょう。
    except ValueError  as e:
        print(e.args)
        continue
    except IndexError  as e:
        print(e.args)
        continue
    if number <=1 and :
            print('↓')
            print('ValueError例外を発生')
            print('↓')
            print('もう一度選択しましょう')
    
    elif number <=2:
            print('↓')
            print('IndexError例外を発生')
            print('↓')
            print('もう一度選択しましょう')

    elif number <=3:
            print('↓')
            print('例外を発生させない')
            print('↓')
            print('もう一度選択しましょう')
    # 問②：else節を用いて、以下の画像のように処理されるように記述しましょう。

    else:
        print('終了します')
        break

print('↓')
print('無限ループを終了します')