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
#define ll long long
using namespace std;


int main() {
    int T;
    cin>>T;
    for(int t=1;t<=T;t++) {
        int a,b,c,d,k;
        cin>>a>>b>>c>>d>>k;
        bool found=false;
        for(int x=0;x<=k;x++) {
            int y = k-x;
            
            if (x*c >= a && y*d >= b) {
                printf("%d %d\n",x,y);
                found=true;
                break;
            }
        }
        if (!found) {
            cout << -1 << endl;
        }
    }
}
