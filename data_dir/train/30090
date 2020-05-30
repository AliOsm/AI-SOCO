#include<bits/stdc++.h>

using namespace std;

typedef long long LL;
typedef unsigned long long uLL;
typedef long double ldb;
typedef pair<int,int> pii;

const int mod = 1e9 + 7;
bool orth[int(5e6+1)];
int ans[int(5e6+1)];
int first[int(5e6+1)];
vector<int> primes;

int main()
{
    ios_base::sync_with_stdio(0);cin.tie(0);
    LL t, l, r;
    cin>>t>>l>>r;
    for(int i = 2; i <= r; ++i)
        if(!orth[i])
        {
            first[i] = i;
            primes.push_back(i);
            for(LL j = LL(i) * i; j <= r; j += i)
            {
                orth[j] = true;
                if(!first[j])
                    first[j] = i;
            }
        }
    for(int i = 2; i <= r; ++i)
        ans[i] = (ans[i/first[i]] + i/first[i] * (LL(first[i]) * (first[i] - 1)/2%mod)%mod)%mod;
    LL d = 1;
    LL sum = 0;
    for(int i = l; i <= r; ++i)
    {
        sum = (sum + ans[i]*d%mod) % mod;
        d = d * t % mod;
    }
    cout<<sum<<endl;
    return 0;
}
