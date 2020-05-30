#include<bits/stdc++.h>
using namespace std;

int dx[]={0,1,0,-1};
int dy[]={1,0,-1,0};

int n,m; 

string mp[555];

bool in(int x,int y){return x>=0&&x<n && y>=0&&y<m;}

int main(){
    cin>>n>>m;
    for(int i=0;i<n;++i)cin>>mp[i];
    for(int i=0;i<n;++i){
        for(int j=0;j<m;++j){
            if(mp[i][j]=='S'){
                for(int d=0;d<4;++d){
                    int nx=i+dx[d],ny=j+dy[d];
                    if(in(nx,ny) && mp[nx][ny]=='W'){
                        cout<<"No"<<endl;
                        exit(0);
                    }
                }
            }
        }
    }
    cout<<"YES"<<endl;
    for(int i=0;i<n;++i){
        for(int j=0;j<m;++j){
            if(mp[i][j]=='.')cout<<"D";
            else cout<<mp[i][j];
        }
        cout<<endl;
    }
}
