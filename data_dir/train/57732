#include<bits/stdc++.h>
using namespace std;

inline void NO(){exit(((cout<<"-1"<<endl),0));}

int n,m;
string s[2555];

void solve(string t){
    // cout<<"t: "<<t<<endl;
    bool allsame=[&t](){
        int cnt[26]={0};
        for(char c:t){
            ++cnt[c-'a'];
            if(cnt[c-'a']>1)return 0;
        }
        return 1;
    }();
    for(int i=0;i<n;++i){
        vector<int> diffpos;
        for(int j=0;j<m;++j)if(t[j]!=s[i][j])diffpos.push_back(j);
        if(!(diffpos.size()==2 || (diffpos.empty() && !allsame)))return;
    }
    cout<<t<<endl;
    exit(0);
}

void solve(string &s1,string &s2){
    vector<int> diffpos;
    for(int i=0;i<m;++i)if(s1[i]!=s2[i])diffpos.push_back(i);
    if(diffpos.size()>4)NO();
    for(int i=0;i<m;++i){
        for(int j=0;j<diffpos.size();++j){
            if(i==diffpos[j])continue;
            string t=s1;
            swap(t[i],t[diffpos[j]]);
            solve(t);
            t=s2;
            swap(t[i],t[diffpos[j]]);
            solve(t);
        }
    }
    NO();
}

int cnt1[26],cnt2[26];
int main(){
    cin>>n>>m;
    for(int i=0;i<n;++i)cin>>s[i];
    for(char c:s[0])++cnt1[c-'a'];
    for(int i=0;i<n;++i){
        memset(cnt2,0,sizeof(cnt2));
        for(char c:s[i])++cnt2[c-'a'];
        for(int i=0;i<26;++i)if(cnt1[i]!=cnt2[i])NO();
    }
    sort(s,s+n);
    for(int i=1;i<n;++i)if(s[i]!=s[i-1]){
        solve(s[i],s[i-1]);
        return 0;
    }
    swap(s[0][0],s[0][1]);
    cout<<s[0]<<endl;
}

