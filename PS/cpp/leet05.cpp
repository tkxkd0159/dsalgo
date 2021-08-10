#include "algo.h"

using namespace std;

class Solution {
public:
    bool isValid(string s) {
        stack<char> stk;
        for (auto& c : s) {
            switch (c) {
                case '(': stk.push(')'); break;
                case '[': stk.push(']'); break;
                case '{': stk.push('}'); break;
                default:
                    if (stk.empty() || c != stk.top()) {
                        return false;
                    }
                    else {
                        stk.pop();
                    }
            }
        }
        return stk.empty();
    }
};

int main() {
    Solution test;
    string mystr, mystr2;
    mystr = "()";
    mystr2 = "[(]";
    cout << test.isValid(mystr) << endl;
    cout << test.isValid(mystr2) << endl;
    return 0;
}
