#include<bits/stdc++.h>
using namespace std;
int mx = 0;
void cnt (int count, int p)
{
    int  total = 0;
    if(count >= 3)
    {
        total = p*3;
    }
    else if(count > 1)
    {
        total = p*count;
    }

    mx = max(mx, total);
}

int main()
{
    int ar[10],sum = 0;
    for(int i = 0; i < 5; i++)
    {
        cin >> ar[i];
        sum += ar[i];
    }

    sort(ar, ar+5);
    for(int i = 0; i < 5; i++)
    {
        int count = 0;
        for(int j = 0; j < 5; j++)
        {
            if(ar[i] == ar[j])count++;
           // cout<<count<<endl;
        }
        cnt(count, ar[i]);
    }
        //cout<<sum<<" "<<mx<<endl;
        cout<<sum - mx<<endl;
}
