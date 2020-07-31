// In the name of Allah the Lord of the Worlds.

#include<bits/stdc++.h>
using namespace std;

typedef long long ll;
ll ans = 0 , n;

void f(ll value)
{
    if(value>n)return ;

    ans++;

    f(value*10);
    f(value*10+1);
}

int main(void)
{
    cin >> n;

    f(1);
    cout << ans << endl;

    return 0;
}
