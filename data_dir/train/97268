#pragma GCC optimize("no-stack-protector")
#include<bits/stdc++.h>
using namespace std;
#define ll long long

#ifdef WEAK
#include"../template/debug.cpp"
#else
#define endl '\n'
#define PDE(...) ;
#endif


ll a[300005];

struct node{
    node *l,*r;
    int ans,ldec,rdec,lans,rans,len;
    ll rest,lest,tag;
    void addtag(ll v){rest+=v, lest+=v, tag+=v;}
    node():l(0),r(0){
        ans=rest=lest=ldec=rdec=lans=rans=tag=0;
    }
} *root;

#define mid ((l+r)>>1)

void pull(node *now){
    now->lest=now->l->lest;
    now->rest=now->r->rest;
    now->ans=max(now->l->ans,now->r->ans);
    if(now->l->ldec==now->l->len && now->r->lest<now->l->rest)now->ldec=now->l->ldec+now->r->ldec;
    else now->ldec=now->l->ldec;
    if(now->r->rdec==now->r->len && now->l->rest<now->r->lest)now->rdec=now->r->rdec+now->l->rdec;
    else now->rdec=now->r->rdec;
    if(now->l->lans==now->l->len && now->r->lest<now->l->rest)now->lans=now->l->lans+now->r->ldec;
    else now->lans=now->l->lans;
    if(now->l->rdec==now->l->len && now->l->rest<now->r->lest)now->lans=max(now->lans,now->l->rdec+now->r->lans);
    if(now->r->rans==now->r->len && now->l->rest<now->r->lest)now->rans=now->r->rans+now->l->rdec;
    else now->rans=now->r->rans;
    if(now->r->ldec==now->r->len && now->r->lest<now->l->rest)now->rans=max(now->rans,now->r->ldec+now->l->rans);
    if(now->l->rest<now->r->lest)now->ans=max(now->ans,now->l->rdec+now->r->lans);
    if(now->r->lest<now->l->rest)now->ans=max(now->ans,now->r->ldec+now->l->rans);
}

void push(node *now){
    if(!now->tag)return;
    now->l->addtag(now->tag);
    now->r->addtag(now->tag);
    now->tag=0;
}

void build(node *now,int l,int r){
    if(l==r){
        now->ans=now->ldec=now->rdec=now->lans=now->rans=1;
        now->rest=now->lest=a[l];
        now->len=1;
        return;
    }
    build(now->l=new node(),l,mid);
    build(now->r=new node(),mid+1,r);
    now->len=r-l+1;
    pull(now);
}
void modify(node *now,int l,int r,int ml,int mr,ll v){
    if(r<ml || mr<l)return;
    if(ml<=l && r<=mr){
        now->addtag(v);
        return;
    }
    push(now);
    modify(now->l,l,mid,ml,mr,v);
    modify(now->r,mid+1,r,ml,mr,v);
    pull(now);
}

int main(){
    ios_base::sync_with_stdio(0); cin.tie(0);
    int n; cin>>n;
    for(int i=1;i<=n;++i)cin>>a[i];
    build(root=new node(),1,n);
    int m; cin>>m; while(m--){
        int l,r,d; cin>>l>>r>>d;
        modify(root,1,n,l,r,d);
        PDE(root->l->rest,root->r->lest,root->r->ldec,root->l->rans);
        cout<<root->ans<<endl;
    }
}
