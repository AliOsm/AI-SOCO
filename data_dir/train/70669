#include<bits/stdc++.h>
using namespace std;

int a[400005],nxt[400005],prv[400005],pos[400005];

int main(){
    int n,k; cin>>n>>k;
    for(int i=1;i<=n;++i){
        cin>>a[i];
    }
    for(int i=1;i<=n;++i)pos[i]=n+1;
    for(int i=n;i>=1;--i){
        nxt[i]=pos[a[i]];
        pos[a[i]]=i;
    }
    for(int i=1;i<=n;++i)pos[i]=0;
    for(int i=1;i<=n;++i){
        prv[i]=pos[a[i]];
        pos[a[i]]=i;
    }
    int ans=0;
    set<pair<int,int>> st;
    for(int i=1;i<=n;++i){
        if(prv[i]==0){
            ++ans;
            if(st.size()==k){
                st.erase(--st.end());
            }
            st.insert({nxt[i],i});
        }
        else{
            auto it=st.find({i,prv[i]});
            if(it!=st.end()){
                st.erase(it);
                st.insert({nxt[i],i});
            }
            else{
                if(st.size()==k){
                    st.erase(--st.end());
                }
                st.insert({nxt[i],i});
                ++ans;
            }
        }
    }
    cout<<ans<<endl;
}
