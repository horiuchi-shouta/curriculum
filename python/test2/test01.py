#test01.py

import random
answer = random.randint(1, 10)

while True:  # 無限ループ
    try:
        number = int(input('10までの数値を入力してください: '))
        # 問①：ValueError例外を処理するコードを記述してください。
    except ValueError:
        print('数字以外が入力されました。数字のみを入力してください')

        continue
    if answer< number:
        print('もっと小さな数値です')
        # 問②：画像のように表示するように、コードを記述してください。
    elif answer<8:
        print('もっと大きな数字を入力して下さい。')
    else:
        break  # 変数answerの値と変数numberの値が等しければ終了

print('正解！')