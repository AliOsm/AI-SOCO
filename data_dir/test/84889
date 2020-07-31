#include<bits/stdc++.h>

using namespace std;

typedef long long LL;
typedef unsigned long long uLL;
typedef long double ldb;
typedef pair<int,int> pii;

vector<int> A[12];

int main()
{
    ios_base::sync_with_stdio(0);cin.tie(0);
    for(int i = 0; i < 4; ++i)
        A[i] = vector<int>(4);
    for(int i = 0; i < 4; ++i)
        for(int j = 0 ; j < 4; ++j)
            cin>>A[i][j];
    for(int i = 4; i < 12; ++i)
        A[i] = A[i-4];
    for(int i = 4; i < 8; ++i)
    {
        if(A[i][3] && (A[i-1][2] || A[i+1][0] || A[i+2][1] || A[i][0] || A[i][1] || A[i][2]))
            return cout<<"YES"<<endl, 0;
    }
    cout<<"NO"<<endl;
    return 0;
}
