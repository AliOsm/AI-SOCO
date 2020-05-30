#pragma GCC optimize("no-stack-protector")
#include<bits/stdc++.h>
using namespace std;

int a[500005];

struct node{
    node *l,*r;
    int val;
    node():l(0),r(0),val(0){}
} *root;

void pull(node *now){
    now->val=__gcd(now->l->val,now->r->val);
}

#define mid ((l+r)>>1)
void build(node *now,int l,int r){
    if(l==r){
        now->val=a[l];
        return;
    }
    build(now->l=new node(),l,mid);
    build(now->r=new node(),mid+1,r);
    pull(now);
}
void modify(node *now,int l,int r,int x){
    if(l==r){
        now->val=a[l];
        return;
    }
    if(x<=mid)modify(now->l,l,mid,x);
    else modify(now->r,mid+1,r,x);
    pull(now);
}
int query(node *now,int l,int r,int ql,int qr,int x){
    if(r<ql || qr<l)return 0;
    if(ql<=l&&r<=qr){
        if(now->val%x==0)return 0;
        if(l==r)return 1;
        int qqq=query(now->l,l,mid,ql,qr,x);
        if(qqq>1)return qqq;
        return qqq+query(now->r,mid+1,r,ql,qr,x);
    }
    int qqq=query(now->l,l,mid,ql,qr,x);
    if(qqq>1)return qqq;
    return qqq+query(now->r,mid+1,r,ql,qr,x);
}

int main(){
    ios_base::sync_with_stdio(0); cin.tie(0);
    int n; cin>>n;
    for(int i=1;i<=n;++i)cin>>a[i];
    build(root=new node(),1,n);
    int q; cin>>q; while(q--){
        int c; cin>>c;
        if(c==1){
            int l,r,x; cin>>l>>r>>x;
            cout<<(query(root,1,n,l,r,x)<=1?"YES":"NO")<<'\n';
        }
        else{
            int x,v; cin>>x>>v;
            a[x]=v;
            modify(root,1,n,x);
        }
    }
}
