#include<bits/stdc++.h>
using namespace std;

int dp[1111][1111],cf[1111][1111];

#pragma GCC diagnostic ignored "-Wempty-body"
#define update(a,b,y,z) if(dp[a][b]>y)dp[a][b]=y,cf[a][b]=z;else;


int main(){
    string s,t; cin>>s>>t;
    memset(dp,0x3f,sizeof(dp));
    dp[0][0]=0;
    for(int i=0;i<=s.size();++i){
        for(int j=0;j<=t.size();++j){
            if(i<s.size() && j<t.size() && s[i]==t[j]){
                update(i+1,j+1,dp[i][j],-1);
            }
            if(i<s.size() && j<t.size())update(i+1,j+1,dp[i][j]+1,(1<<15)+t[j]-'A');
            if(j<t.size())update(i,j+1,dp[i][j]+1,(1<<16)+t[j]-'A');
            if(i<s.size())update(i+1,j,dp[i][j]+1,(1<<17));
            // cout<<i<<" "<<j<<" dp: "<<dp[i][j]<<" "<<cf[i][j]<<endl;
        }
    }
    cout<<dp[s.size()][t.size()]<<endl;
    int i=s.size(),j=t.size();
    stack<int> st;
    while(i>0||j>0){
        if(cf[i][j]==-1)--i,--j;
        else if(cf[i][j]&(1<<15)){
            st.push((1<<29)|(j<<18)|(((1<<10)-1)&cf[i][j]));
            // cout<<"REPLACE "<<j<<" "<<(char)((cf[i][j]&((1<<10)-1))+'A')<<endl;
            --i,--j;
        }
        else if(cf[i][j]&(1<<16)){
            st.push((2<<29)|(j<<18)|(((1<<10)-1)&cf[i][j]));
            // cout<<"INSERT "<<j<<" "<<(char)((cf[i][j]&((1<<10)-1))+'A')<<endl;
            --j;
        }
        else if(cf[i][j]&(1<<17)){
            st.push((3<<29)|(j<<18)|(((1<<10)-1)&cf[i][j]));
            // cout<<"DELETE "<<j<<endl;
            --i;
        }
    }
    while(st.size()){
        int x=st.top(); st.pop();
        // cout<<bitset<32>(x)<<endl;
        if((x>>29)==1){
            cout<<"REPLACE "<<((x<<3>>21))<<" "<<(char)((x<<18>>18)+'A')<<endl;
        }
        if((x>>29)==2){
            cout<<"INSERT "<<((x<<3>>21))<<" "<<(char)((x<<18>>18)+'A')<<endl;
        }
        if((x>>29)==3){
            cout<<"DELETE "<<((x<<3>>21)+1)<<" "<<endl;
        }
        
    }
}
