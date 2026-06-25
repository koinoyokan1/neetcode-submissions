class Solution {
public:
    vector<int> asteroidCollision(vector<int>& asteroids) {
        stack<int> st;

        for (int a:asteroids) {
            if (a > 0) {
                st.push(a);
                continue;
            }
            bool addA = true;
            while (st.size() != 0 && st.top() > 0 && a < 0) {
                int b = st.top();

                if (abs(a) == b) {
                    st.pop();
                    addA = false;
                    break;
                } else if (abs(a) < b) {
                    addA = false;
                    break;
                } else {
                    st.pop();
                    addA = true;
                }
            }
            if (addA) {
                st.push(a);
            }
        }
        vector<int> ans;
        while(!st.empty()) {
            int x = st.top();
            ans.push_back(x);
            st.pop();
        } 
        reverse(ans.begin(), ans.end());
        return ans;
    }
};