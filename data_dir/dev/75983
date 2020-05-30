#include<bits/stdc++.h>

using namespace std;

typedef long long LL;
typedef unsigned long long uLL;
typedef long double ldb;
typedef pair<int,int> pii;

int main()
{
    ios_base::sync_with_stdio(0);cin.tie(0);
    int n;
    cin>>n;
    map<int, int> ma;
    for(int i = 0 ; i < n; ++i)
    {
        int inp;
        cin>>inp;
        ++ma[inp];
    }
    if(ma.size() == 2 && ma.begin()->second == ma.rbegin()->second)
        cout<<"YES"<<endl<<ma.begin()->first<<" "<<ma.rbegin()->first<<endl;
    else
        cout<<"NO"<<endl;
    return 0;
}
