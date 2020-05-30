#include<bits/stdc++.h>

using namespace std;

#define ll long long
#define X first
#define Y second
#define all(x) x.begin(), x.end()

const int MX = (int)2e5 + 10;
// const int mod = (int)1e9 + 7;

vector<int> fin[MX];

int main(){

    cin.tie(0); cout.tie(0);
    ios_base::sync_with_stdio(0);

    int n, k;
    cin >> n >> k;


    for(int i = 0; i < n; ++i){
        int x;
        cin >> x;
        int cntr = 0;
        fin[x].push_back(cntr);
        while(x){
            x >>= 1;
            cntr++;
            fin[x].push_back(cntr);
        }
    }

    int res = n * 20;
    for(int i = 0; i < MX; ++i){
        if(fin[i].size() < k) continue;
        sort(all(fin[i]));
        res = min(res, accumulate(fin[i].begin(), fin[i].begin() + k, 0));
    }

    cout << res << endl;

    return 0;
}