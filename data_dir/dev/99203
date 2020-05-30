#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const int MOD = 1e9+7;
int main(){
    string s;
    int n;
    cin >> s >> n;
    vector<string> arr(n);
    bool ans = 0;
    for(int i = 0; i < n; ++i){
        cin >> arr[i];
        if(arr[i] == s)
            ans = 1;
    }
    for(int i = 0; i < n; ++i)
        for(int j = 0; j < n; ++j){
            string cur = "";
            cur += arr[i][1];
            cur += arr[j][0];
            if(cur == s)
                ans = 1;
        }
    if(ans)
        puts("YES");
    else
        puts("NO");
}
