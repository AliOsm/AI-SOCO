#include<bits/stdc++.h>
using namespace std;
#define ld long double

int main(){
    int ts; cin>>ts; while(ts--){
        ld a,b; cin>>a>>b;
        if(b==0)cout<<1<<endl;
        else if(a==0)cout<<0.5<<endl;
        else{
        ld area=a*b;
        // x-4y>=0
        if(a/4<=b)area=(a*a/8)/area;
        else area=(area-b*b*2)/area;
        cout<<fixed<<setprecision(231)<<0.5+area/2<<endl;
    }}
}
