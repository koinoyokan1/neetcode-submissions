// "2[abc3[b]]c"
// 2[abc3   b 
class Solution {
public:
    string decodeString(string s) {
        stack<char> st;

        for (int i = 0; i < s.size(); i++) {
            if (s[i] != ']') {
                st.push(s[i]);
            } else {
                string chrs, cnt;

                while (true) {
                    char c = st.top();
                    st.pop();
                    if (c == '[') {
                        break;
                    }
                    chrs = chrs + c;
                }
                reverse(chrs.begin(), chrs.end());

                while (!st.empty()) {
                    char c = st.top();
                    if (!isdigit(c)) {
                        break;
                    }
                    st.pop();
                    cnt = cnt + c;
                }
                reverse(cnt.begin(), cnt.end());
                int cnt_i = stoi(cnt);


                for (int k=0; k < cnt_i; k++) {
                    for (int j=0; j < chrs.size(); j++) {
                        st.push(chrs[j]);
                    }
                }
                
            }           
        }
        string ans;

        while (!st.empty()) {
            ans.push_back(st.top());
            st.pop();
        }

        reverse(ans.begin(), ans.end());
        return ans;
    }
};