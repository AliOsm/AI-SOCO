#include<bits/stdc++.h>

using namespace std;

typedef long long LL;
typedef unsigned long long uLL;
typedef long double ldb;
typedef pair<int,int> pii;

char A[2][3];

int main()
{
    ios_base::sync_with_stdio(0);cin.tie(0);
    string s,t,d;
    cin>>A[0];
    cin>>A[1];
    s = "";
    if(A[0][0]!='X')
        s += A[0][0];
    if(A[0][1]!='X')
        s += A[0][1];
    if(A[1][1]!='X')
        s += A[1][1];
    if(A[1][0]!='X')
        s += A[1][0];
    cin>>A[0];
    cin>>A[1];
    t = "";
    if(A[0][0]!='X')
        t += A[0][0];
    if(A[0][1]!='X')
        t += A[0][1];
    if(A[1][1]!='X')
        t += A[1][1];
    if(A[1][0]!='X')
        t += A[1][0];
    s += s;
    cout<<(s.find(t) == string::npos ? "NO" : "YES")<<endl;
    return 0;
}
