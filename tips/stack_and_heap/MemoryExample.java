public class MemoryExample {
    publuc static void main(String[] args) {
        int stackVar = 10; // スタックに保存されるプリミティブ型変数

        MyObject obj1 = new MyObject(); // obj1 という参照変数はスタックに、MyObjectのインスタンスはヒープに
        obj1.value = 20;

        String str = "Hello"; // strという参照変数はスタックに、"Hello"という文字列オブジェクトはヒープに

        // mainメソッド終了時、stackVarは解放
        // obj1とstrの参照も解放されるが、参照されていたヒープ上のオブジェクトは
        // 参照がなくなった時点でガベージコレクションの対象になる。
    }
}

class MyObject {
    int value;
}