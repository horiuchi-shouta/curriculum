/**
 *ターミナル上で[javac -encoding UTF-8 main.java]でコンパイル(mainはクラス名)
 *[java main.java]で実行(mainはファイル名)
 * バブルソート
 * チェックテスト-Java３章 */
public class Main{
    public static void main(String[] args){
        /*
        * 問1
        * int型の配列dataを作成し、値を3,1,2,7,5で初期化しなさい
        */
        int[] data = {3,1,2,7,5};

        /*
        * 問2
        * 以下のfor文を完成させなさい
        */
        for(int i = 0; i <= 7; i++){
            System.out.print(data[i] + " ");
        }
        System.out.println();
        //ここまで完成済み。

        for (int i = 0; i < data.length; i++) {     /*i++がないと無限ループに入る。実行ごとに i が一増える。*/
            for (int j =i+1 ; j > i; j--) {  /*j--は実行ごとに i が１減る。*/
                /*
                * 問3
                * 以下、配列の添字を入れてソートを完成させなさい.バブルソートというもの
                */
                if(data[i] > data[j]){
                  //if文で条件に当てはまる値の比較を行い、並び替え
                  int box = data[i];
                  data[i] = data[j];
                  data[j] = box;
                }
            }
        }
        for(int i = 0; i < data.length; i++){   /*lengthは配列dataの中身を一番右まで実行する意味 */
            System.out.print(data[i] + " "); 
        }    
    }
}