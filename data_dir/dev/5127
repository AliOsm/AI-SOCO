#include<bits/stdc++.h>
using namespace std;

int is0[10],is1[10];

int main(){
    for(int i=0;i<10;++i)is1[i]=1;
    int cmds; cin>>cmds; while(cmds--){
        string op; int x; cin>>op>>x;
        if(op=="&"){
            for(int i=0;i<10;++i){
                is0[i]&=!!(x&(1<<i));
                is1[i]&=!!(x&(1<<i));
            }
        }
        if(op=="|"){
            for(int i=0;i<10;++i){
                is0[i]|=!!(x&(1<<i));
                is1[i]|=!!(x&(1<<i));
            }
        }
        if(op=="^"){
            for(int i=0;i<10;++i){
                is0[i]^=!!(x&(1<<i));
                is1[i]^=!!(x&(1<<i));
            }
        }
    }
    int And=0,Or=0,Xor=0;
    for(int i=0;i<10;++i){
        if(is0[i]==0&&is1[i]==0){
            Or|=(1<<i);
            Xor|=(1<<i);
        }
        else if(is0[i]==0&&is1[i]==1){
            And|=(1<<i);
        }
        else if(is0[i]==1&&is1[i]==0){
            And|=(1<<i);
            Xor|=(1<<i);
        }
        else{
            Or|=(1<<i);
        }
    }
    cout<<"3\n& "<<And<<"\n| "<<Or<<"\n^ "<<Xor<<endl;
}
