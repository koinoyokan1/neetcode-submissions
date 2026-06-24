class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        vector<int> ans;

        for (int e: nums) {
            ans.push_back(e);
        }
        for (int e: nums) {
            ans.push_back(e);
        }
        return ans;
    }
};