#include <iostream>
#include <vector>

void myFunction() {
    int stackInt = 10; // ローカル変数⇒スタック
    int* heapInt = new int; // ヒープにint型のメモリを動的確保
    *heapInt = 20;

    std::vector<int> myVector(5); // vectorオブジェクトはスタックに、その中身は（配列）はヒープに

    std::cout << "Stack int: " << stackInt << std::endl;
    std::cout << "Heap int: " << *heapInt << std::endl;

    delete heapInt; // ヒープメモリを明示的に開放
} // 関数終了後は、StackInt と myVector（オブジェクト自体）はスタックから解放される。
int main() {
    myFunction();
    return 0;
}