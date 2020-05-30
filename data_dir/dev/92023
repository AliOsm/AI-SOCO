#include <bits/stdc++.h>
#include <bitset>

#define REP(i,n) for(int i=0;i<(int)n;i++)
#define REP1(i,j,n) for(int i=j;i<(int)n;i++)
#define pb(x) push_back(x)
#define fi first
#define se second
#define all(x) x.begin(),x.end()
#define double long double
#define mp(x,y) make_pair(x,y)

typedef long long ll;

using namespace std;

int n;
const int N=1e5+10;
int arr[N];
pair<int,int>smalL[N],largL[N],smalR[N],largR[N];

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    cin>>n;
    if(n<=2){
        cout<<"0\n";
        return 0;
    }
    REP(i,n)cin>>arr[i];
    smalL[0]=smalL[1]=mp(arr[0],0);
    REP1(i,2,n){
        smalL[i]=min(smalL[i-1],mp(arr[i-1],i-1));
    }
    largR[n-2]=mp(arr[n-1],n-1);
    for(int i=n-3;i>=0;i--){
        largR[i]=max(largR[i+1],mp(arr[i+1],i+1));
    }

    largL[0]=largL[1]=mp(arr[0],0);
    REP1(i,2,n){
        largL[i]=max(largL[i-1],mp(arr[i-1],i-1));
    }
    smalR[n-2]=mp(arr[n-1],n-1);
    for(int i=n-3;i>=0;i--){
        smalR[i]=min(smalR[i+1],mp(arr[i+1],i+1));
    }

    REP1(i,1,n-1){
        if(smalL[i].fi<arr[i]&&arr[i]>smalR[i].fi){
            cout<<3<<"\n";
            cout<<smalL[i].se+1<<" "<<i+1<<" "<<smalR[i].se+1<<"\n";
            return 0;
        }

        if(largL[i].fi>arr[i]&&arr[i]<largR[i].fi){
            cout<<3<<"\n";
            cout<<largL[i].se+1<<" "<<i+1<<" "<<largR[i].se+1<<"\n";
            return 0;
        }
    }
    cout<<"0\n";
}