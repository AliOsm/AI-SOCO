#include <cstdio>
#include <vector>
#include <cstring>
#include <map>
#include <algorithm>
using namespace std;

#include <cstring>
using namespace std;

class BITree {
public:
    static const int SIZE = 300010, BIAS = 5;
    int u[SIZE],cnt;
    void clear(){
        memset(u,cnt=0,sizeof(u));
    }
    void modify(int x, int v){
        cnt+=v;
        for(x+=BIAS;x<SIZE;x+=x&-x) u[x]+=v;
    }
    int getrhs(int x){
        int s=cnt;
        for(x+=BIAS-1;x;x-=x&-x) s-=u[x];
        return s;
    }
}seg;

int x[300005],y[300005],cnt[300005];

int main(){
    int n,m;
    map<pair<int,int>,int> u;
    long long ans=0;
    scanf("%d%d",&n,&m);
    for(int i=1;i<=n;i++){
        scanf("%d%d",&x[i],&y[i]);
        if(x[i]>=y[i]) swap(x[i],y[i]);
        u[{x[i],y[i]}]++;
        ++cnt[x[i]];
        ++cnt[y[i]];
    }
    for(int i=1;i<=n;i++){
        ans+=seg.getrhs(max(m-cnt[i],0));
        seg.modify(cnt[i],1);
    }
    for(auto& r:u){
        int x,y;
        tie(x,y)=r.first;
        if(cnt[x]+cnt[y]>=m && cnt[x]+cnt[y]-r.second<m) ans--;
    }
    printf("%I64d\n",ans);
}
