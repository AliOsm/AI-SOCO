#include<bits/stdc++.h>
using namespace std;


int main(){
    vector<int> v;
    int ans=0;
    int n; cin>>n; n<<=1;
    for(int i=0;i<n;++i){
        int t; cin>>t;
        v.push_back(t);
    }
    while(v.size()){
        for(int i=1;i<v.size();++i){
            if(v[i]==v[0]){
                ans+=i-1;
                v.erase(v.begin()+i);
                v.erase(v.begin());
                break;
            }
        }
    }
    cout<<ans<<endl;
}
