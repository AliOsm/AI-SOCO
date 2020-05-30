#include<bits/stdc++.h>

using namespace std;

typedef long long LL;
typedef unsigned long long uLL;
typedef long double ldb;
typedef pair<int,int> pii;

int n, m, s;

vector<int> A[100000];
vector<int> B[100000];

int ans[100001];

bool f(int sz)
{
    int cA = m-1, stI = n-1;
    LL passes = 0;
    priority_queue<pii, vector<pii>, greater<pii>> pq;
    while(cA >= 0)
    {
        while(stI >= 0 && B[stI][0]>=A[cA][0])
        {
            pq.emplace(B[stI][1], B[stI][2]);
            stI--;
        }
        if(pq.empty())
            return false;
        pii top = pq.top();
        pq.pop();
        passes += top.first;
        int t = sz;
        while(cA>=0 && t--)
        {
            ans[A[cA][1]] = top.second;
            --cA;
        }
    }
    return passes <= s;
}


int main()
{
    ios_base::sync_with_stdio(0);cin.tie(0);
    cin>>n>>m>>s;
    int inp;
    for(int i = 0; i < m; ++i)
        A[i].push_back((cin>>inp, inp));
    for(int i = 0; i < m; ++i)
        A[i].push_back(i+1);
    for(int i = 0; i < n; ++i)
        B[i].push_back((cin>>inp, inp));
    for(int i = 0; i < n; ++i)
        B[i].push_back((cin>>inp, inp));
    for(int i = 0; i < n; ++i)
        B[i].push_back(i+1);
    sort(A, A+m);
    sort(B, B+n);
    int l = 0, r = m+1;
    while(l + 1 < r)
    {
        int m = (l+r)/2;
        if(f(m))
            r = m;
        else
            l = m;
    }
    if(r==m+1)
        return cout<<"NO"<<endl, 0;
    f(r);
    cout<<"YES\n";
    for(int i = 1; i <= m; ++i)
        cout<<ans[i]<<' ';
    cout<<endl;
    return 0;
}
