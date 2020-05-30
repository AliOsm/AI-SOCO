#include<bits/stdc++.h>
using namespace std;

int main(){
    int n,a,b; cin>>n>>a>>b;
    int req[]={a,a,a,a,b,b};
    sort(req,req+6);
    int mn=6;
    do{
        int now=1,lf=n;
        for(int i=0;i<6;++i){
            if(lf<req[i])lf=n,++now;
            lf-=req[i];
        }
        mn=min(mn,now);
    }while(next_permutation(req,req+6));
    cout<<mn<<endl;
}
