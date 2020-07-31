#include<bits/stdc++.h>
using namespace std;
const int maxn = (int)2e5+5;
int q, fst[maxn],lst[maxn];
int main(){
    int n,k;
    cin>>n>>k;
    for(int i=1;i<=k;i++){
        cin>>q;
        lst[q]=i;
        if(fst[q]==0) fst[q]=i;
    }
    for(int i=1;i<=n;i++) 
        if(fst[i]==0) fst[i]=n+2;
    int ans=0;
    for(int i=1;i<=n;i++){
        if(lst[i]==0){
            ans++;
            if(i>1) ans++;
            if(i<n) ans++;
        }
        else{
            if(i>1 && lst[i-1]<fst[i]) ans++;
            if(i<n && lst[i+1]<fst[i]) ans++;
        }
    }
    cout << ans;
    return 0;
}
