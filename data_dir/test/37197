// In the name of Allah the Most Merciful.

#include<bits/stdc++.h>
using namespace std;

int main(void)
{
    int n;
    cin >> n;

    int ar[n] , br[n];

    for(int i=0;i<n;i++){

        cin >> ar[i];
        br[i] = ar[i];
    }

    sort(br , br+n);

    int c = 0 , j , lim;

    for(int i=0;i<n;i++){

        if(ar[i]!=br[i]){

            c++;

            int d = i;

            while(true){

                if(d+1==n)break;
                if(ar[d]<ar[d+1])break;
                d++;
            }

            j = i;
            lim = d;
            i = lim;
        }
    }

    if(c==1){

        cout << "yes" << endl << j+1 << " " << lim+1 << endl;
    }

    else if(c==0){

        cout << "yes" << endl << 1 << " " << 1 << endl;
    }

    else cout << "no" << endl;
}
