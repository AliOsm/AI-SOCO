#include<bits/stdc++.h>
using namespace std;

int main()
{
    map<string, int>mp;
    int n,mx = 0;
    cin>> n;

    string str;
    char c[2];

    cin >> str;
   // int bahir = 0, vitor = 0;

    for(int i = 0; i < n - 1; i++)
    {
        //bahir++;
       // vitor = 0;
        int cnt = 0;
        for(int j = 0; j < n-1; j++)
        {
           // vitor++;
            if(str[i] == str[j] && str[i+1] == str[j+1])
            {
                cnt++;
            if(cnt > mx)
            {
                mx = cnt;
                c[0] = str[i];
                c[1] = str[i+1];
            }

            }
        }
    }
   // cout<<bahir<<" "<<vitor<<endl;
        cout<<c[0]<<c[1]<<endl;

}
