#include <iostream>
using namespace std;

long long int factorial(long long int n) {
    if (n == 0) return 1;
    return n * factorial(n-1);
}

int main() {
    long long int number;
    cin >> number;
    cout << factorial(number) << endl;
    return 0;
}