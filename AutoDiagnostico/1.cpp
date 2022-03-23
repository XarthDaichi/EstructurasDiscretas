#include <iostream>
using namespace std;

int pregunta1(int n) {
    return n * (n + 1) * ((2 * n) + 4) / 12;
}

int main() {
    int times;
    cout << "Enter the number of numbers in the sequences: ";
    cin >> times;
    cout << "The sum is: " << pregunta1(times) << endl;
    return 0;
}