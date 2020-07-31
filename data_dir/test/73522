#include<bits/stdc++.h>
using namespace std;

set<int> lisend[100005];
int n,a[100005],lisat[100005],status[100005],pos[100005];

int main(){
    int n; cin>>n;
    for(int i=0;i<n;++i)cin>>a[i];
    vector<int> lis;
    for(int i=0;i<n;++i){
        if(lis.empty() || a[i]>lis.back())lis.push_back(a[i]);
        else *lower_bound(lis.begin(),lis.end(),a[i])=a[i];
    }
    int lissize=lis.size();
    lis.clear();
    for(int i=0;i<n;++i){
        if(lis.empty() || a[i]>lis.back()){
            lis.push_back(a[i]);
            pos[i]=lis.size();
            if(lis.size()==lissize){
            }
            else{
                
            }
        }
        else{
            auto it=lower_bound(lis.begin(),lis.end(),a[i]);
            *it=a[i];
            pos[i]=it-lis.begin()+1;
            if(lis.size()==lissize && it==--lis.end()){
            }
        }
    }
    for(int i=0;i<n;++i)status[i]=1;
    for(int i=n-1;i>=0;--i){
        if(pos[i]==lissize)lisend[pos[i]].insert(a[i]),status[i]=4;
        else if(lisend[pos[i]+1].upper_bound(a[i])!=lisend[pos[i]+1].end())lisend[pos[i]].insert(a[i]),status[i]=4;
    }
    vector<int> allpos;
    for(int i=0;i<n;++i)if(status[i]==4)allpos.push_back(pos[i]);
    sort(allpos.begin(),allpos.end());
    for(int i=0;i<n;++i)if(status[i]==4){
        auto lo=lower_bound(allpos.begin(),allpos.end(),pos[i]);
        auto up=upper_bound(allpos.begin(),allpos.end(),pos[i]);
        if(up-lo==1)status[i]=3;
        else status[i]=2;
    }
    for(int i=0;i<n;++i){
        cout<<status[i];
    }
    cout<<endl;
}
