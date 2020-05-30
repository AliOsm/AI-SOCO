#include <bits/stdc++.h>
#include <bitset>

#define REP(i,n) for(int i=0;i<(int)n;i++)
#define REP1(i,j,n) for(int i=j;i<(int)n;i++)
#define all(x) x.begin(),x.end()
#define double long double
#define BUG cerr<<"BUG\n";

typedef long long ll;

using namespace std;

int n=4,m,k;
int a[4][50];
pair<int,int>nxt[4][50],prv[4][50];
int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    cin>>m>>k;
    REP1(j,1,m)nxt[1][j-1]=make_pair(1,j),prv[1][j]=make_pair(1,j-1);
    REP1(j,1,m)prv[2][j-1]=make_pair(2,j),nxt[2][j]=make_pair(2,j-1);
    nxt[1][m-1]=make_pair(2,m-1);
    prv[2][m-1]=make_pair(1,m-1);
    nxt[2][0]=make_pair(1,0);
    prv[1][0]=make_pair(2,0);
    REP(i,n)REP(j,m)cin>>a[i][j];
    int cars=0;
    vector<pair<int,pair<int,int> > >ret;
    while(1){
        REP1(i,1,3)REP(j,m)
                if(a[i][j]&&a[i-1][j]==a[i][j]){
                    ret.push_back(make_pair(a[i][j],make_pair(i-1,j)));
                    a[i][j]=0;
                    cars++;
                }else if(a[i][j]&&a[i+1][j]==a[i][j]){
                    ret.push_back(make_pair(a[i][j],make_pair(i+1,j)));
                    a[i][j]=0;
                    cars++;
                }
        int erow=-1,ecol=-1;
        REP1(i,1,3)REP(j,m)
                       if(!a[i][j])
                           erow=i,ecol=j;
        if(cars==k||erow==-1)break;
        int row=nxt[erow][ecol].first,col=nxt[erow][ecol].second;
        while(row!=erow||col!=ecol){
            if(a[row][col]){
                ret.push_back(make_pair(a[row][col],make_pair(prv[row][col].first,prv[row][col].second)));
                a[prv[row][col].first][prv[row][col].second]=a[row][col];
                a[row][col]=0;
            }
            int nrow=nxt[row][col].first;
            col=nxt[row][col].second;
            row=nrow;
        }
//        REP(i,n){
//            REP(j,m){
//                cerr<<" "<<a[i][j];
//            }
//            cerr<<"\n";
//        }
//        cerr<<"\n";
    }

    if(cars!=k)cout<<"-1\n";
    else{
        cout<<ret.size()<<"\n";
        for(auto p:ret)
            cout<<p.first<<" "<<p.second.first+1<<" "<<p.second.second+1<<"\n";
    }
}