#include<bits/stdc++.h>
using namespace std;

int main(){
    int q,w,e,r; cin>>q>>w>>e>>r;
    int r2=r*2;
    int e2=e*2;
    int c=max(e,r);
    if(w*2<c)cout<<-1<<endl;
    else if(e2<r || r2<e)cout<<-1<<endl;
    else{
    int b=max(c+1,w); b=max(b,r2+1);
    int a=max(b+1,q);
    if(b>w*2)cout<<-1<<endl;
    else if(a>q*2)cout<<-1<<endl;
    else cout<<a<<endl<<b<<endl<<c<<endl;
}}
