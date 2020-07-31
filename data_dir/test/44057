#include<bits/stdc++.h>
using namespace std;

string mp[3][3][3];
int cnt[3][3];
int main(){
    for(int i=0;i<3;++i){
        for(int j=0;j<3;++j){
            cin>>mp[i][0][j]>>mp[i][1][j]>>mp[i][2][j];
        }
        for(int j=0;j<3;++j){
            for(int k=0;k<3;++k){
                for(int l=0;l<3;++l){
                    if(mp[i][j][k][l]=='.')++cnt[i][j];
                }
            }
        }
    }
    int x,y; cin>>x>>y; --x, --y; x%=3, y%=3;
    bool all=0;
    if(!cnt[x][y])all=1;
    for(int i=0;i<3;++i){
        for(int j=0;j<3;++j){
            for(int k=0;k<3;++k){
                for(int l=0;l<3;++l){
                    if(all && mp[i][k][j][l]=='.')cout<<'!';
                    else if(all)cout<<mp[i][k][j][l];
                    else if(i==x && k==y && mp[i][k][j][l]=='.')cout<<'!';
                    else cout<<mp[i][k][j][l];
                }
                cout<<" ";
            }
            cout<<endl;
        }
        cout<<endl;
    }
}
