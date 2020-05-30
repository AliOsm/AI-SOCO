#include<bits/stdc++.h>
using namespace std;
#define ll long long

struct z{
    ll a,i;
} a[100005];
ll pre[100005];

int main(){
    ll n,A,cf,cm,m;
    cin>>n>>A>>cf>>cm>>m;
    for(int i=1;i<=n;++i){
        ll t; cin>>t;
        a[i]={t,i};
    }
    sort(a+1,a+1+n,[](const z &a,const z &b){return a.a>b.a;});
    for(int i=1;i<=n+3;++i)pre[i]=pre[i-1]+a[i].a;
    ll mxf=0,mxc=-1,mnv=-1,mnit=1;
    for(int i=0;i<=n;++i){
        ll mlef=m-(A*i-pre[i]);
        if(mlef<0)break;
        ll tf=cf*i;
        while(mnit<=i)++mnit;
        ll need=(n-mnit+1)*a[mnit].a-(pre[n]-pre[mnit-1]);
        while(need>mlef){
            ++mnit;
            need=(n-mnit+1)*a[mnit].a-(pre[n]-pre[mnit-1]);
        }
        mlef-=need;
        ll to=-1;
        if(mnit<=n){
            tf+=cm*a[mnit].a;
            ll lowadd=mlef/(n-mnit+1);
            to=a[mnit].a+lowadd;
            to=min(to,A);
            tf+=cm*(to-a[mnit].a);        
        }
        else tf+=cm*A;
        if(tf>mxf){
            mxf=tf;
            mxc=i;
            mnv=to;
        }
    }
    cout<<mxf<<endl;
    for(int i=1;i<=mxc;++i)a[i].a=A;
    for(int i=mxc+1;i<=n;++i)a[i].a=max(a[i].a,mnv);
    sort(a+1,a+1+n,[](const z &a,const z &b){return a.i<b.i;});
    for(int i=1;i<=n;++i)cout<<a[i].a<<" ";
    cout<<endl;
}
