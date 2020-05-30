// In the name of Allah the Most Merciful.

#include<bits/stdc++.h>
using namespace std;

typedef long long ll;

int main(void)
{
    int n;
    cin >> n;

    ll male[367] , female[367];

    memset(male , 0 , sizeof(male));
    memset(female , 0 , sizeof(female));

    for(int i=0;i<n;i++){

        char x;

        int l1 , l2;

        cin >> x >> l1 >> l2;

        for(;l1<=l2;l1++){

            if(x=='M')male[l1]++;
            else female[l1]++;
        }
    }

    ll mx = 0;

    for(int i=1;i<367;i++){

        mx = max(mx , min(male[i],female[i]));
    }

    cout << mx*2 << endl;

    return 0;
}
