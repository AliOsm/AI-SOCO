#include <bits/stdc++.h>
#define ull unsigned long long int
#define ll long long int
#define P pair
#define PLL pair<long long, long long>
#define PII pair<int, int>
#define PUU pair<unsigned long long int, unsigned long long int>
#define L list
#define V vector
#define S set
#define MS multiset
#define M map
#define mp make_pair
#define pb push_back
#define MM multimap
#define IT iterator
#define RIT reverse_iterator
#define FAST ios_base::sync_with_stdio(false);cin.tie();cout.tie();

using namespace std;

int main(){
    int n;
    cin >> n;
    V<double> arr(n);
    priority_queue<double,V<double>, greater<double> > p;
    double ans = 0;
    for(int i = 0; i < n;++i)cin >> arr[i];
    for(int i = 0; i < n;++i)ans+=arr[i];
    for(int i = 0; i < n;++i)p.push(arr[i]);
    ans = ans/n;
    int c = 0;
    // printf("(%f,%d)\n",ans,c);
    while(ans < 4.4999999999999){
        double a = p.top();
        p.pop();
        ans+=((5-a)/n);
        // cout << ans << "\n";
        c++;
        // printf("(%f,%d)\n",ans,c);
    }
    cout << c;
    return 0;
}