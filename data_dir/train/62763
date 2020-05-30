#include<bits/stdc++.h>
using namespace std;
char a[505][505];
int n,m,k,cnt=0,x,y,z=0;
int dx[]={-1,1,0,0};
int dy[]={0,0,1,-1};
int valid(int x,int y){
   return (x>=0 && x<n) &&(y>=0 &&y<m);
}
void dfs(int x,int y){
   if(z == cnt) return;
   for(int i=0;i<4;i++){
      int u=x+dx[i];
      int v=y+dy[i];
      if(valid(u,v) && a[u][v]=='.' && z < cnt){
          a[u][v]='A';
          z++;
         dfs(u,v);
      }
   }
}
int main(){
  cin>>n>>m>>k;
  getchar();
  for(int i=0;i<n;i++){
     gets(a[i]);
     for(int j=0;j<m;j++)
     {
        if(a[i][j]=='.') {
          x=i,y=j;cnt++;}
     }
  }
  cnt=cnt-k;
  z++;
  a[x][y]='A';
  dfs(x,y);
  for(int i=0;i<n;i++){
     for(int j=0;j<m;j++)
     {
        if(a[i][j]=='A') cout<<'.';
        else if(a[i][j]=='.') cout<<'X';
        else cout<<'#';
     }
     cout<<"\n";
  }
 return 0;
}
