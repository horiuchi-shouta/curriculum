while True:
    try:
        print()
        print('1: ValueError例外を発生')
        print('2: IndexError例外を発生')
        print('3: 例外を発生させない')
        print('4: 終了')
        #input関数とは、ユーザーがキーボードに入力したデータを受け付けるための関数
        number = int(input('選択してください。: '))

        # 問①：if文を用いて、以下の画像のように処理されるように記述しましょう。
        if number==1:    
            tmp=int('hoge')
            continue
        if number==2:
            s=[10,20,30]
            print(s[100])
            continue
        if number==3:
            print('↓')
            print('例外を発生させませんでした')
            print('↓')
            print('もう一度選択しましょう')
            continue
         
    except ValueError as e:
        print('↓')
        print('ValueError')
        print(e.args)
        print('↓')
        print('もう一度選択しましょう')
        continue

    except IndexError as e:
        print('↓')
        print('IndexError')
        print(e.args)
        print('↓')
        print('もう一度選択しましょう')
        continue

    # 問②：else節を用いて、以下の画像のように処理されるように記述しましょう。
    else:
        print('↓')
        print('終了します')
        break
                

    
print('↓')
print('無限ループを終了します')