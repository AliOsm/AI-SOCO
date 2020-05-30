#include<bits/stdc++.h>
using namespace std;

#define pb push_back
#define ll long long
#define maxn 300005
#define fr(i,j,k) for(int i=j;i<k;i++)
#define f(n) fr(i,0,n)
#define f1(n) fr(i,1,n+1)
#define ms(i) memset(i,0,sizeof(i));
#define ms1(i) memset(i,-1,sizeof(i));
#define F first
#define S second
const int mod = 1e9 + 7;

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    map<pair<int,int>,int >mp;
    int n;
    cin >> n;
    ll tot[n+5] = {};
    ll cnt[n+5] = {};
    ll ans = 0;
    f1(n){
        cin >> tot[i];
        ans += tot[i];
    }
    int m;
    cin >> m;
    while(m--){
        int add1, add2, add3;
        cin >> add1 >> add2 >> add3;
        if(mp.count({add1,add2})){
            int x = mp[{add1,add2}];
            cnt[x]--;
            if(cnt[x] < tot[x]){
                ans++;
            }
            mp.erase({add1,add2});
        }
        if(add3!=0){
            mp[{add1,add2}] = add3;
            cnt[add3]++;
            if(cnt[add3] <= tot[add3]){
                ans--;
            }
        }
        cout << ans << '\n';
    }

}
