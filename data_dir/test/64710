#include<bits/stdc++.h>
using namespace std;

int main()
{
    int n,a,b,c,c1=0,c2=0,c3=0,p,q,r,count=0,_count=0,l;

    cin>>n>>a>>b>>c;

    int ar[10];
    memset(ar, 0, sizeof(ar));

    int br[5 ];
    br[0] = a;
    br[1] = b;
    br[2] = c;
    sort(br, br+3);

    int x = a+b+c;
    if(n%x==0)ar[0] = 3;
    if(n%a==0)ar[1] = n/a;
    if(n%b==0)ar[2] = n/b;
    if(n%c==0)ar[3] = n/c;
    p = n;
    if(a>=b)
    {
        while(p>0)
        {
            p -= a;
            c1++;

            if(p<0)break;

            if(p%b==0)
            {
                ar[4] = p/b + c1;
                //cout<<endl;

                break;
            }
        }
    }
    else
    {
        while(p>0)
        {
            p -= b;
            c1++;
            if(p<0)break;
            if(p%a==0)
            {
                ar[4] = p/a + c1;

                break;
            }
        }
    }
    q = n;
    if(b>=c)
    {
        while(q >0)
        {
            q -= b;
            c2++;
            if(q<0)break;
            if(q%c==0)
            {
                ar[5] = q/c + c2;
                //  cout<<ar[5]<<" __"<<endl;
                break;
            }
        }
    }
    else
    {
        int q = n;
        while(q>0)
        {
            q -= c;
            c2++;
            if(q<0)break;
            if(q%b==0)
            {
                ar[5] = q/b + c2;
                break;
            }
        }
    }
    r = n;
    if(a>=c)
    {
        while(r>0)
        {
            r -= a;
            c3++;
            if(r<0)break;
            if(r%c==0)
            {
                ar[6] = r/c + c3;
                break;
            }
        }
    }
    else
    {
        while(r>0)
        {
            r -= c;
            c3++;
            if(r<0)break;
            if(r%a==0)
            {
                ar[6] = r/a + c3;
                //cout<<ar[6]<<"__"<<endl;

                break;
            }
        }
    }

    l = n;
    while(l>0)
    {
        if(l%br[0]==0)
        {
            ar[8] = l/br[0]+_count;
            //cout<<_count<<endl;;
            break;
        }
        l -= br[2];
        _count++;
        l -= br[1];
        _count++;
    }
    while(n>0)
    {
        if(n%br[2]==0)
        {
            ar[7] = n/br[2]+count;
         //   cout<<ar[7]<<endl;;
            break;
        }

        n -= br[1];
        count++;
        n -= br[0];
        count++;
    }



    sort(ar, ar+9);
    //for(int i=0; i<7; i++)
    cout<<ar[8]<<endl;
}
