#include<bits/stdc++.h>
using namespace std;
#define ll long long

int nodes;
void *__ptr[222];

struct node{
    node *ch[26],*fail;
    int dta,id;
    node():fail(0),dta(0),id(nodes++){memset(ch,0,sizeof(ch)); __ptr[id]=this;}
} *root;

node *ptr[222];

void add(node *&now,string &s,int ptr,int dt){
    if(!now)now=new node();
    // cout<<"add "<<s<<"["<<ptr<<"] = "<<s[ptr]<<" and id: "<<now->id<<endl;
    if(ptr>=s.size()){
        now->dta+=dt;
        return;
    }
    add(now->ch[s[ptr]-'a'],s,ptr+1,dt);
}

void go(){
    queue<node*> q;
    root->fail=root;
    for(int i=0;i<26;++i){
        if(!root->ch[i])root->ch[i]=root;
        else root->ch[i]->fail=root,q.push(root->ch[i]);
    }
    while(q.size()){
        for(int i=0;i<26;++i){
            if(q.front()->ch[i]){
                node *now=q.front()->fail;
                while(now && !now->ch[i])now=now->fail;
                q.front()->ch[i]->fail=now->ch[i];
                q.front()->ch[i]->dta+=now->ch[i]->dta;
                q.push(q.front()->ch[i]);
            }
            else q.front()->ch[i]=q.front()->fail->ch[i];
        }
        q.pop();
    }
}
struct mat{
    ll a[222][222];
    mat(){memset(a,0,sizeof(a));}
} tr;

mat operator*(const mat &a,const mat &b){
    mat rt;
    for(int i=0;i<nodes;++i){
        for(int j=0;j<nodes;++j){
            rt.a[i][j]=-(1<<30);
            for(int k=0;k<nodes;++k){
                rt.a[i][j]=max(rt.a[i][j],a.a[i][k]+b.a[k][j]);
            }
        }
    }
    return rt;
}

mat pw(mat b,long long n){
    if(n==1)return b;
    if(n&1)return pw(b*b,n>>1)*b;
    return pw(b*b,n>>1);
}

int a[222];

void pp(mat m){
    for(int i=0;i<nodes;++i){
        for(int j=0;j<nodes;++j){
            cout<<m.a[i][j]<<" ";
        }
        cout<<endl;
    }
    cout<<" > -------------- <\n";
}

int main(){
    int n; long long l; cin>>n>>l;
    for(int i=1;i<=n;++i)cin>>a[i];
    for(int i=1;i<=n;++i){
        string s; cin>>s;
        add(root,s,0,a[i]);
    }
    go();
    for(int i=0;i<nodes;++i)ptr[i]=(node*)__ptr[i];
    for(int i=0;i<nodes;++i)for(int j=0;j<nodes;++j)tr.a[i][j]=-(1<<30);
    for(int i=0;i<nodes;++i){
        node *now=ptr[i];
        for(int j=0;j<26;++j){
            tr.a[i][now->ch[j]->id]=now->ch[j]->dta;
            // if(now->ch[j]->id)cout<<"node "<<i<<" to "<<now->ch[j]->id<<" delta: "<<now->ch[j]->dta<<endl;
        }
    }
    // pp(tr);
    tr=pw(tr,l);
    // pp(tr);
    long long ans=0;
    for(int i=0;i<nodes;++i)ans=max(ans,tr.a[0][i]);
    cout<<ans<<endl;
}
