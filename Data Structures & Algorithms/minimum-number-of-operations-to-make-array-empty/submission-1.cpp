/*
x%3: 1
x//3 - 1 + 2
1: -1
2: 1
3: 1
4: 2
5: 2
6: 2
7: 3
*/
class Solution {
public:
    int minOperations(vector<int>& nums) {
        unordered_map<int, int> numCnt;
        for (int n: nums) {
            numCnt[n]++;
        }

        int minOps = 0;
        for (auto [key, value]: numCnt) {
            if (value == 1) {
                return -1;
            }
            if (value % 3 == 0) {
                minOps += value/3;
            } else {
                minOps += (value/3 + 1);
            }
        }
        return minOps; 
    }
};