#include <bits/stdc++.h>
#include <bitset>

#define REP(i,n) for(int i=0;i<(int)n;i++)
#define REP1(i,j,n) for(int i=j;i<(int)n;i++)
#define all(x) x.begin(),x.end()
#define double long double
#define mp(x,y) make_pair(x,y)

typedef long long ll;

using namespace std;


int dx[]={0,1,0,1};
int dy[]={-1,-1,1,1};
int n;
bool valid(int r,int c){
    return c>=0&&c<n;
}
string s[2];
int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    cin>>s[0]>>s[1];
    n=s[0].length();
    int cnt=0;
    REP(i,n){
        if(s[0][i]=='0'&&s[1][i]=='0'){
            REP(k,4){
                int nr=dx[k],nc=i+dy[k];
                if(valid(nr,nc)&&s[nr][nc]=='0'){
                    cnt++;
                    s[nr][nc]='.';
                    s[0][i]='.';
                    s[1][i]='.';
                    break;
                }
            }
        }
    }
    cout<<cnt<<"\n";
}