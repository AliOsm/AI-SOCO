#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <vector>

struct Parcel {
    int in,out,w,s,v;
    Parcel(int in=0,int out=0,int w=0,int s=0,int v=0)
        :in(in),out(out),w(w),s(s),v(v) {}
    void read() {
        scanf("%d%d%d%d%d",&in,&out,&w,&s,&v);
    }
    bool operator < (const Parcel &t) const {
        if (in == t.in) return out > t.out;
        return in < t.in;
    }
    void show() {
        printf("%d %d %d %d %d\n",in,out,w,s,v);
    }
};

const int N = 500 + 5;
const int M = 1000 + 5;
int n,S,dp[N][M],d[M];
Parcel parcel[N];

inline void toMax(int &a,int b) {
    if (a < b) a = b;
}

int main() {
    scanf("%d%d",&n,&S);
    for (int i = 0; i < n; ++ i) {
        parcel[i].read();
    }
    parcel[n] = Parcel(0,n++<<1,0,S,0);
    std::sort(parcel,parcel+n);
    for (int i = n-1; i >= 0; -- i) {
        for (int j = 0; j <= parcel[i].s; ++ j) {
			memset(d,0,sizeof(d));
            d[0] = parcel[i].v;
            for (int k = i+1,r = 1; k < n; ++ k) {
                if (parcel[k].in >= parcel[i].out) break;
                if (parcel[k].out > parcel[i].out) continue;
                if (parcel[k].w > j) continue;
                while (r<=parcel[k].in)
                    toMax(d[r],d[r-1]),r++;
               toMax(d[parcel[k].out],d[parcel[k].in]+dp[k][std::min(parcel[k].s,j-parcel[k].w)]);
            }
            for (int k = 0; k <= parcel[i].out; ++ k)
                toMax(dp[i][j],d[k]);
        }
    }
    printf("%d\n",dp[0][S]);
    return 0;
}
