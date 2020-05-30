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
    int t;
    cin >> t;
    while(t--){
        int n;
        cin >> n;
        int last[n+5] = {};
        int ans = 1e9;
        f1(n){
            int add;
            cin >> add;
            if(last[add]){
                ans = min(i-last[add]+1,ans);
            }
            last[add] = i;
        }
        if(ans == 1e9){
            cout << -1 << '\n';
        }
        else{
            cout << ans << '\n';
        }
    }
}
