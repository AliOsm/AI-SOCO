#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <bitset>
#include <functional>
#include <vector>
#include <numeric>      // std::accumulate
#define MODD 1000000007

#define ll long long
using namespace std;


int main() {
    ll n,p,w,d;
    cin>>n>>p>>w>>d;
    
    
    for(ll x=0;x<=11000000;x++) {
        if (p >= x*w && (p-x*w)%d==0 &&  x+(p-x*w)/d<=n) {
            printf("%lld %lld %lld\n",x,(p-x*w)/d,n-x-(p-x*w)/d);
            return 0;
        }
    }
    
    for(ll y=0;y<=11000000;y++) {
        if (p >= y*d && (p-y*d)%w==0 && y+(p-y*d)/w<=n) {
            printf("%lld %lld %lld\n",(p-y*d)/w,y,n-y-(p-y*d)/w);
            return 0;
        }
    }
    
    cout << -1 << endl;
    return 0;
    
}
