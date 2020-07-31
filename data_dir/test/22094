#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;
const int N = 501000;
int n,head[N],etot,p[N],dft,st[N],ed[N]; // [st,ed]
bool tree[N<<2],lazy[N<<2];
struct edge{int v,next;}g[N<<1];
void add_edge(int u,int v) {
        g[etot] = (edge){v,head[u]}; head[u] = etot ++;
}
void down(int rt) {
        if (lazy[rt]) {
                tree[rt<<1] = tree[rt<<1|1] = tree[rt];
                lazy[rt<<1] = lazy[rt<<1|1] = 1;
                lazy[rt] = 0;
        }
}
void up(int rt) {
        tree[rt] = tree[rt<<1] | tree[rt<<1|1];
}
void modify(int L,int R,int val,int l,int r,int rt) {
        if (L<=l && r<= R) {
                tree[rt] = val; 
                lazy[rt] = 1;
                return ;
        }
        int mid = l+r>>1;
        down(rt);
        if (L<=mid) modify(L,R,val,l,mid,rt<<1);
        if (R> mid) modify(L,R,val,mid+1,r,rt<<1|1);
        up(rt);
}
bool query(int L,int R,int l,int r,int rt) {
        if (L<=l && r<=R) return tree[rt];
        int mid = l+r>>1;
        down(rt);
        bool ret = 0;
        if (L<=mid) ret |= query(L,R,l,mid,rt<<1);
        if (R> mid) ret |= query(L,R,mid+1,r,rt<<1|1);
        return ret;
}
inline int getInt() {
        int ret = 0; char c;
        while ((c=getchar())==' ' || c=='\n');
        ret = c-'0';
        while ((c=getchar())!=' ' && c!='\n') ret = ret*10+c-'0';
        return ret;
}
void dfs(int u,int fa) {
        st[u] = ++dft;
        p[u] = fa;
        for (int i = head[u]; i != -1; i = g[i].next) {
                edge &e = g[i];
                if (e.v==fa) continue;
                dfs(e.v,u);
        }
        ed[u] = dft;
}
int main() {
        n = getInt();
        memset(head,-1,sizeof(head)); etot = 0;
        for (int i = 0; i < n-1; i ++) {
                int a,b;
                a = getInt(); b = getInt();
                add_edge(a,b); add_edge(b,a);
        }
        dfs(1,-1);
        int nq;
        nq = getInt();
        modify(1,dft,1,1,dft,1);
        while (nq--) {
                int c,v;
                c = getInt(); v = getInt();
                if (c==1) {
                        bool tmp;
                        tmp = query(st[v],ed[v],1,dft,1);
                        if (tmp && p[v]!=-1) modify(st[p[v]],st[p[v]],1,1,dft,1);
                        modify(st[v],ed[v],0,1,dft,1);
                }
                else if (c==2) {
                        modify(st[v],st[v],1,1,dft,1);
                }
                else printf("%d\n",query(st[v],ed[v],1,dft,1)!=1);
        }
        return 0;
}
