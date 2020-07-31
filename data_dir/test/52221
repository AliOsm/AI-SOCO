#pragma warning(disable:4786)
#pragma warning(disable:4996)
#include<bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/trie_policy.hpp>
#define pii pair<int,int>
#define pll pair<long long ,long long>
#define pli pair<long long , int>
#define pil pair<int ,long long>
#define pi acos(-1)
#define pb push_back
#define mkp make_pair
#define all(a) a.begin(), a.end()
#define IOS ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);
#define ll long long
#define MAX 300005
#define INF 0x3f3f3f3f
template <class T> inline T bigmod(T p,T e,T M){ll ret = 1LL;for(; e > 0LL; e >>= 1LL){if(e & 1LL) ret = (ret * p) % M;p = (p * p) % M;}return (T)ret;}
template <class T> inline T modinverse(T a,T M){return bigmod(a,M-2,M);}   // M is prime}

using namespace std;
using namespace __gnu_pbds;

typedef trie<string,null_type,trie_string_access_traits<>,pat_trie_tag,trie_prefix_search_node_update>pref_trie;




int main(){
    IOS
    //freopen("output.txt","w",stdout);
    double a,b,c;
    cin>>a>>b>>c;
    double det = b*b - 4*a*c;
    if(det<0){
        cout<<"0";
        return 0;
    }
    if (a==0){
        if(b==0){
            if(c==0){
                cout<<-1;
            }
            else{
                cout<<0;
            }
        }
        else{
            cout<<1<<"\n";
            cout<<fixed<<setprecision(9)<<(-c)/b;
        }
    }
    else{

        double ans1 = (-b+sqrt(det))/(2*a);
        double ans2 = (-b-sqrt(det))/(2*a);
        if(ans1==ans2){
            cout<<1<<"\n";
            cout<<fixed<<setprecision(9)<<ans1<<"\n";
            return 0;
        }
        cout<<2<<"\n";
        cout<<fixed<<setprecision(9)<<min(ans1,ans2)<<"\n";
        cout<<fixed<<setprecision(9)<<max(ans1,ans2)<<"\n";
    }
}
