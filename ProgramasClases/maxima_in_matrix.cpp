#include <iostream>
#include <vector>
using namespace std;

/*
def maxima_in_matrix(a:'list[list[int]]')->'list[list[int]]':
    max_list = []
    max_num = 0
    for i in range(len(a)):
        for j in range(len(a[i])):
            test = a[i][j]
            if test > max_num:
                max_list = []
                max_num = test
                max_list.append([i,j])
            elif test == max_num:
                max_list.append([i,j])
    return max_list

a_1 = [[5,4,3,2,1], [4,3,2,1,0], [2,1,5,4,3], [3,5,1,2,4], [0,1,2,3,4]]
a_2 = [[1,4,3,2,5], [4,3,2,1,0], [2,1,5,4,3], [3,1,5,2,4], [0,1,2,3,4]]
a_3 = [[1,4,3,2,0], [4,3,2,1,0], [2,1,5,4,3], [3,1,5,2,4], [5,1,2,3,4]]
a_4 = [[1,4,3,2,0], [4,3,2,1,0], [2,1,5,4,3], [3,1,5,2,4], [0,1,2,3,5]]
a_5 = [[1,4,3,2,0], [4,3,2,1,0], [2,1,5,4,3], [3,1,0,2,4], [0,1,2,3,4]]

print(maxima_in_matrix(a_1))
print(maxima_in_matrix(a_2))
print(maxima_in_matrix(a_3))
print(maxima_in_matrix(a_4))
print(maxima_in_matrix(a_5))
*/


vector<vector<int>> maxima_in_matrix(vector<vector<int>> a) {
    vector<vector<int>> max_list;
    int max_num = 0;
    for (int i = 0; i < a.size(); i++) {
        for (int j = 0; j < a[i].size(); j++) {
            int test = a[i][j];
            if (test > max_num) {
                max_list.clear();
                max_num = test;
                max_list.push_back({i, j});
            } else if (test == max_num) {
                max_list.push_back({i, j});
            }
        }
    }
    return max_list;
}

int main() {
    vector<vector<int>> a_1 = {{5,4,3,2,1}, {4,3,2,1,0}, {2,1,5,4,3}, {3,5,1,2,4}, {0,1,2,3,4}};
    vector<vector<int>> a_2 = {{1,4,3,2,5}, {4,3,2,1,0}, {2,1,5,4,3}, {3,1,5,2,4}, {0,1,2,3,4}};
    vector<vector<int>> a_3 = {{1,4,3,2,0}, {4,3,2,1,0}, {2,1,5,4,3}, {3,1,5,2,4}, {5,1,2,3,4}};
    vector<vector<int>> a_4 = {{1,4,3,2,0}, {4,3,2,1,0}, {2,1,5,4,3}, {3,1,5,2,4}, {0,1,2,3,5}};
    vector<vector<int>> a_5 = {{1,4,3,2,0}, {4,3,2,1,0}, {2,1,5,4,3}, {3,1,0,2,4}, {0,1,2,3,4}};

    vector<vector<int>> a_1_result = maxima_in_matrix(a_1);
    vector<vector<int>> a_2_result = maxima_in_matrix(a_2);
    vector<vector<int>> a_3_result = maxima_in_matrix(a_3);
    vector<vector<int>> a_4_result = maxima_in_matrix(a_4);
    vector<vector<int>> a_5_result = maxima_in_matrix(a_5);
    
    for (vector<int> i : a_1_result) {
        for (int j : i) {
            cout << j << '\t';
        }
        cout << '\t';
    }
    cout << endl;
    for (vector<int> i : a_2_result) {
        for (int j : i) {
            cout << j << '\t';
        }
        cout << '\t';
    }
    cout << endl;
    for (vector<int> i : a_3_result) {
        for (int j : i) {
            cout << j << '\t';
        }
        cout << '\t';
    }
    cout << endl;
    for (vector<int> i : a_4_result) {
        for (int j : i) {
            cout << j << '\t';
        }
        cout << '\t';
    }
    cout << endl;
    for (vector<int> i : a_5_result) {
        for (int j : i) {
            cout << j << '\t';
        }
        cout << '\t';
    }
    return 0;
}