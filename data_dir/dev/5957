#include<bits/stdc++.h>
using namespace std;

int ar[10001];


int main()
{
    memset(ar, 100, sizeof(ar) );
    int n,k,total = 0,p,q;
    cin >> n >> k;

    for(int i = 1; i <= n; i++)
    {
        cin >> ar[i];
        if(ar[k] == 1) total = 1;
    }
    p = k;
    q = k;
    int ck = 0;
    while(1)
    {
        p--;
        q++;
        //cout<<p<<" "<<q<<endl;
        //cout<<" P "<<ar[p]<<"  Q "<<ar[q]<<" "<<total<<endl;
        if(p <= 0 || q > n)ck = 1;
         if( p <= 0 && q > n)break;
         if(ar[p] == 1 && ar[q] == 1 && ck == 0)total = total + 2;
        else
        {
            if(q > n)
            if(ar[p] == 1)total++;
             if(p <= 0)
             if(ar[q] == 1)total++;
        }

    }
    cout<<total<<endl;
}
