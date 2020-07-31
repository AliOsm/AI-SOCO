#include <bits/stdc++.h>

#define ll long long
#define all(x) x.begin(), x.end()
#define f(i, j, k) for (int i = j; i < k; i++)
#define pb(x) push_back(x)
#define F first
#define S second

using namespace std;


int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    string s; cin >> s;
    int sz = (int)s.length();
    int idx = 0;
    f(rows, 1, 5 + 1)
        f(cols, 1, 20 + 1){
            int left = rows * cols - sz;
            if(left < 0)continue;
            vector<int> give(rows);
            f(j, 0, left)give[j % rows]++;
            cout << rows << " " << cols << "\n";
            f(i, 0, rows){
                int done = 0;
                while(give[i]--)done++, cout << "*";
                while(done < cols){
                    cout << s[idx++];
                    done++;
                }
                cout << "\n";
            }
            return 0;
        }
}