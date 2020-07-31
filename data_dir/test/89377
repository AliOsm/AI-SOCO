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

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    ll n;
    cin >> n;
    ll cnt = 0,mi = 1e18;
    for(ll i = 2 ; i * i <= n ; i++){
        if(n%i==0){
            cnt++;
            mi = min(mi,i);
            while(n%i==0){
                n /= i;
            }
        }
    }
    if(n > 1){
        mi = min(mi,n);
        cnt++;
    }
    if(cnt == 1){
        cout << mi << endl;
    }
    else{
        cout << 1 << endl;
    }
}
