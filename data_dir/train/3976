#include<bits/stdc++.h>

using namespace std;

#define ll long long
#define X first
#define Y second
#define all(x) x.begin(), x.end()

const int MX = (int)1e5 + 10;
// const int mod = (int)1e9 + 7;

int main(int argc, char* argv[]){

    cin.tie(0); cout.tie(0);
    ios_base::sync_with_stdio(0);

   
    int n;
    cin >> n;

    int a[n];
    for(int i = 0; i < n; ++i){
        cin >> a[i];
    }

    int q;
    cin >> q;

    int mx = 0;

    int best[q] = {0};
    int lst[n];
    memset(lst, 0xff, sizeof lst);

    for(int i = 0; i < q; ++i){
        int t;
        cin >> t;

        if(t == 1){
            int x, p;
            cin >> p >> x;
            a[p - 1] = x;
            lst[p - 1] = i;
        }
        else
        {
            int x;
            cin >> x;
            best[i] = x;
        }
    }

    for(int i = q - 2; i >= 0; --i) best[i] = max(best[i + 1], best[i]);

    for(int i = 0; i < n; ++i){
        cout << max(a[i], lst[i] != -1 ? best[lst[i]] : best[0]) << " \n"[i == n - 1];
    }

    return 0;
}