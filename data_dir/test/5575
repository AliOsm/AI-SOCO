#include<bits/stdc++.h>
using namespace std;
#define ll long long

const ll mod=1000000009;
const ll _p=613;

string s;
ll p[1000006],invp;

ll pw(ll b,int n,int m,ll a=1){
    while(n){
        if(n&1)a=a*b%mod;
        b=b*b%mod; n>>=1;
    } return a;
}

#define norm(x) (((x%mod)+mod)%mod)

void print(int len){
    cout<<s.substr(0,len)<<endl;
    exit(0);
}

int main(){
    cin>>s;
    p[0]=1; for(int i=1;i<=1000000;++i)p[i]=p[i-1]*_p%mod;
    invp=pw(_p,mod-2,mod);
    ll prefix=0,suffix=0;
    for(int i=0;i<s.size();++i)prefix=(prefix+s[i]*p[i])%mod;
    suffix=prefix;
    int preptr=s.size()-1,sufptr=0,len=s.size();
    prefix=norm(prefix-s[preptr]*p[preptr]%mod); --preptr;
    suffix=norm(suffix-s[sufptr])*invp%mod; ++sufptr; --len;
    prefix=norm(prefix-s[preptr]*p[preptr]%mod); --preptr;
    suffix=norm(suffix-s[sufptr])*invp%mod; ++sufptr; --len;
    while(prefix || suffix){
        if(prefix==suffix){
            ll now=0; int i=1,j=1;
            for(int wwq=0;wwq<len;++wwq,++j){
                now=(now+s[j]*p[wwq]%mod)%mod;
            }
            if(prefix==now)print(len);
            for(;j<s.size()-1;++i,++j){
                now=(now+s[j]*p[len]%mod)%mod;
                now=norm(now-s[i])*invp%mod;
                if(prefix==now)print(len);
            }
        }
        prefix=norm(prefix-s[preptr]*p[preptr]%mod); --preptr;
        suffix=norm(suffix-s[sufptr])*invp%mod; ++sufptr; --len;
    }
    cout<<"Just a legend"<<endl;
}
