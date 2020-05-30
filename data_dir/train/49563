#include<bits/stdc++.h>
using namespace std;
int main()
{
    long long n,b,d,sum = 0,cnt = 0;

    cin >>n >> b >>d;

    for(int i = 0; i < n ; i++)
    {
        int a;
        cin >> a;
        if(b >= a)
            sum += a;
        if( sum > d)
        {
            cnt++;
            sum = 0;
        }
    }
    cout<<cnt<<endl;

    return 0;
}
