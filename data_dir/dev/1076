#pragma GCC optimize("no-stack-protector,Ofast")
#include<bits/stdc++.h>
using namespace std;
#define Hash unsigned long long
#define Hset unordered_set<int>
#ifndef WEAK
#define endl '\n'
#define PDE(a) ;
#else
#define PDE(a) cout<<#a<<" = "<<a<<endl;
#endif


vector<int> G[100005];
Hash a[100005];

string s;
inline Hash getHash(){
    cin>>s;
    Hash rt=0;
    for(char &c:s){
        rt=(rt*47017)+c;
    }
    return rt;
}

int dep[100005],in[100005],out[100005],dt=-1,inby[100005];
vector<int> depts[100005];
void dfs(int now,int ndep){
    dep[now]=ndep;
    in[now]=++dt;
    inby[dt]=now;
    depts[ndep].push_back(dt);
    for(int i:G[now]){
        dfs(i,ndep+1);
    }
    out[now]=dt;
}

vector<Hash> dephs[100005];
int ans[100005],*bit[100005],*prv[100005],*pos[100005];

void add(int bid,int x,int v){
    for(;x<depts[bid].size()+5;x+=x&-x)bit[bid][x]+=v;
}
int query(int bid,int x,int v=0){
    for(;x;x-=x&-x)v+=bit[bid][x];
    return v;
}

struct Q{
    int i,d,l,r,t;
} qs[100005];

int main(){
    ios_base::sync_with_stdio(0); cin.tie(0);
    int n; cin>>n;
    for(int i=1,pa;i<=n;++i){
        a[i]=getHash();
        cin>>pa;
        G[pa].push_back(i);
    }
    // cout<<"meow"<<endl;
    dfs(0,0);
    for(int i=1;i<=n;++i){
        dephs[dep[i]].push_back(a[i]);
    }
    // cout<<"meow"<<endl;
    for(int i=1;i<=n;++i){
        if(depts[i].empty())break;
        bit[i]=new int[depts[i].size()+5];
        prv[i]=new int[depts[i].size()+5];
        pos[i]=new int[depts[i].size()+5];
        memset(bit[i],0,sizeof(int)*(depts[i].size()+5));
        memset(prv[i],0xff,sizeof(int)*(depts[i].size()+5));
        memset(pos[i],0xff,sizeof(int)*(depts[i].size()+5));
        sort(depts[i].begin(),depts[i].end());
        sort(dephs[i].begin(),dephs[i].end());
    }
    // cout<<"meow"<<endl;
    for(int i=1;i<=n;++i){
        a[i]=lower_bound(dephs[dep[i]].begin(),dephs[dep[i]].end(),a[i])-dephs[dep[i]].begin()+1;
    }
    // cout<<"meow"<<endl;
    for(int i=1;i<=dt;++i){
        
        int t=lower_bound(depts[dep[inby[i]]].begin(),depts[dep[inby[i]]].end(),i)-depts[dep[inby[i]]].begin()+1;
        // PDE(i);
        // PDE(t);
        // PDE(inby[i]);
        prv[dep[inby[i]]][t]=pos[dep[inby[i]]][a[inby[i]]];
        // pos[dep[inby[i]]][a[inby[i]]]=lower_bound(depts[i].begin(),depts[i].end(),i)-depts[i].begin()+1;
        pos[dep[inby[i]]][a[inby[i]]]=t;
    }
    // cout<<"meow"<<endl;
    int q; cin>>q;
    for(int i=0,x,k;i<q;++i){
        cin>>x>>k;
        if(dep[x]+k>n)continue;
        int d=dep[x]+k;
        int l=lower_bound(depts[d].begin(),depts[d].end(),in[x])-depts[d].begin()+1;
        int r=upper_bound(depts[d].begin(),depts[d].end(),out[x])-depts[d].begin();
        // cout<<"query of dep "<<d<<" q: "<<l<<" to "<<r<<" with out time "<<out[x]<<endl;
        if(l>r)continue;
        qs[i]={i,d,l,r,out[x]};
    }
    sort(qs,qs+q,[](const Q &a,const Q &b){return a.t<b.t;});
    int nt=0;
    for(int i=0;i<q;++i){
        if(qs[i].d==0)continue;
        while(nt<qs[i].t){
            ++nt;
            // cout<<"processing time "<<nt<<endl;
            int x=lower_bound(depts[dep[inby[nt]]].begin(),depts[dep[inby[nt]]].end(),nt)-depts[dep[inby[nt]]].begin()+1;
            // cout<<"add dep "<<dep[inby[nt]]<<" pos "<<x<<endl;
            add(dep[inby[nt]],x,1);
            int p=prv[dep[inby[nt]]][x];
            if(p!=-1){
                // cout<<"sub "<<p<<endl;
                add(dep[inby[nt]],p,-1);
            }
        }
        ans[qs[i].i]=query(qs[i].d,qs[i].r)-query(qs[i].d,qs[i].l-1);
    }
    for(int i=0;i<q;++i)cout<<ans[i]<<'\n';
}
