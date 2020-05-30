#include<bits/stdc++.h>
using namespace std;

struct spell{
    int a,b,c,d,i;
} a[100004];
bool operator<(const spell &a,const spell &b){return a.b==b.b?a.i<b.i:a.b<b.b;}

bitset<100004> v;

struct node{
    node *l,*r;
    set<spell> st;
    node():l(0),r(0){}
} *root;

#define mid ((l+r)>>1)
void build(node *now,int l,int r){
    if(l==r)return;
    build(now->l=new node(),l,mid);
    build(now->r=new node(),mid+1,r);
}

void add(node *now,int l,int r,int id){
    now->st.insert(a[id]);
    if(l==r)return;
    if(a[id].a<=mid)add(now->l,l,mid,id);
    else add(now->r,mid+1,r,id);
}

queue<int> q;
int d[100004],cf[100004];

void query(node *now,int l,int r,int ql,int qr,int id){
    // cout<<now<<" "<<l<<" "<<r<<endl;
    if(r<ql || qr<l)return;
    if(ql<=l&&r<=qr){
        while(now->st.size() && now->st.begin()->b<=a[id].d){
            int nid=now->st.begin()->i;
            now->st.erase(now->st.begin());
            
            if(d[nid]>0)continue;
            d[nid]=d[id]+1;
            cf[nid]=id;
            q.push(nid);
        }
        return;
    }
    query(now->l,l,mid,ql,qr,id);
    query(now->r,mid+1,r,ql,qr,id);
}

int main(){
    ios_base::sync_with_stdio(0); cin.tie(0);
    int n; cin>>n;
    vector<int> acs;
    for(int i=1;i<=n;++i)cin>>a[i].a>>a[i].b>>a[i].c>>a[i].d,a[i].i=i;
    for(int i=1;i<=n;++i)acs.push_back(a[i].a),acs.push_back(a[i].c);
    sort(acs.begin(),acs.end());
    for(int i=1;i<=n;++i)a[i].a=lower_bound(acs.begin(),acs.end(),a[i].a)-acs.begin()+1,a[i].c=lower_bound(acs.begin(),acs.end(),a[i].c)-acs.begin()+1;
    build(root=new node(),1,acs.size());
    for(int i=1;i<=n;++i)add(root,1,acs.size(),i);
    q.push(0);
    d[n]=-1;
    a[0].c=1;
    while(q.size()){
        int now=q.front(); q.pop();
        // cout<<"now: "<<now<<endl;
        spell &sp=a[now];
        query(root,1,acs.size(),1,sp.c,now);
        if(d[n]>0)break;
    }
    cout<<d[n]<<endl;
    if(d[n]<0)return 0;
    stack<int> pa;
    while(n){
        pa.push(n);
        n=cf[n];
    }
    while(pa.size()){
        cout<<pa.top()<<" ";
        pa.pop();
    }
}
