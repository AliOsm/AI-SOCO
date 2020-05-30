#include <bits/stdc++.h>

using namespace std;

int main()
{
    int n , m , i , j , k;
    scanf("%d %d",&n,&m);
    int arr[n+5][m+5];
    int cnt[n+5][m+5];

    for(i = 1 ; i <= n ; i++)
    {
        for(j = 1 ; j <= m ; j++)
        {
            scanf("%d",&arr[i][j]);
        }
    }
    for(j = 1 ; j <= m ; j++)
    {
        cnt[1][j] = 1;
        cnt[0][j] = 0;
    }

    for(i = 2 ; i <= n ; i++)
    {
        for(j = 1 ; j <= m ; j++)
        {
            if(arr[i][j] >= arr[i-1][j])
            {
                cnt[i][j] = cnt[i-1][j] + 1;
            }
            else
            {
                cnt[i][j] = 1;
            }
        }
    }

    int last[n+5];
    memset(last,0,sizeof(last));

    for(i = 1 ; i <= n ; i++)
    {
        for(j = 1 ; j <= m ; j++)
        {
            last[i] = max(last[i],cnt[i][j]);
        }
    }

    scanf("%d",&k);
    bool ok ;
    int l , r;
    while(k--)
    {
        scanf("%d %d",&l,&r);
        ok = false;

        if(last[r] >= (r-l+1))
        {
            ok = true;
        }

        if(ok)printf("Yes\n");
        else printf("No\n");
    }
    return 0;
}
