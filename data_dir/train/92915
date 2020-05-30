// In the name of Allah the Most Merciful.

#include<bits/stdc++.h>
using namespace std;

typedef long long ll;

int main(void)
{
    //ios::sync_with_stdio(0);
    //cin.tie(0);

    ll n;
    cin >> n;
    n*=2;

    vector<ll>v , temp;

    for(int i=0;i<n;i++){

        ll in;
        cin >> in;
        v.push_back(in);
    }

    sort(v.begin() , v.end());
    int ans = 123456789;
    for(int i=0;i<n;i++){

        for(int j=i+1;j<n;j++){

            temp.clear();
            int counter = 0;

            for(int k=0;k<n;k++){

                if(k==i||k==j)continue;

                temp.push_back(v[k]);
            }

            for(int k=0;k<n-2;k+=2){

                counter+=(temp[k+1]-temp[k]);
            }

            ans = min(counter , ans);

        }
    }

    cout << ans << endl;

    return 0;
}
