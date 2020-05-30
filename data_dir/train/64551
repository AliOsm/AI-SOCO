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
    int n;
    cin >> n;
    vector<ll>v;
    ll ans = 0;
    v.pb(0);
    f1(n){
        ll add;
        cin >> add;
        v.pb(add);
    }
    if(v.back()==-1){
        cout << 0 << endl;
        exit(0);
    }
    multiset<ll>st;
    int last = n - 1;
    ans = v.back();
    for(int i = n/2 ; i ; i >>= 1){
        int f = 0;
        for(int j = last ; j >= i ; j --){
            if(v[j] == -1){
                f = 1;
                break;
            }
            st.insert(v[j]);
        }
        //cout << i - 1 <<' '<<last <<' '<<endl;
        if(f)break;
        else{
            ans += *st.begin();
            st.erase(st.begin());
            last = i - 1;
        }
    }
    cout << ans << endl;
}
