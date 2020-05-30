#include<bits/stdc++.h>

using namespace std;

typedef long long LL;
typedef unsigned long long uLL;
typedef long double ldb;
typedef pair<int,int> pii;

int P[50];
int T[50];

int main()
{
    ios_base::sync_with_stdio(0);cin.tie(0);
    int n, c;
    cin>>n>>c;
    int tl = 0, tr = 0;
    for(int i = 0; i < n; ++i)
        cin>>P[i];
    for(int i = 0; i < n; ++i)
        cin>>T[i];
    int l = 0;
    for(int i = 0; i < n; ++i)
    {
        tl += T[i];
        l += max(0, P[i] - c*tl);
    }
    int r = 0;
    for(int i = n-1; i >= 0; --i)
    {
        tr += T[i];
        r += max(0, P[i] - c*tr);
    }
    if(l > r)
        cout<<"Limak";
    else if(r > l)
        cout<<"Radewoosh";
    else
        cout<<"Tie";
    cout<<endl;
    return 0;
}
