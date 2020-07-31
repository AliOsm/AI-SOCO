// In the name of Allah the Most Merciful.

#include<bits/stdc++.h>
using namespace std;

double ax , ay , bx , by , tx , ty;
vector<pair <double , double > > v;

double dp[100005][2][2];
int n;

double dis(double x1 , double y1 , double x2 , double y2)
{

    return sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2));
}

double f(int i , int j , int k)
{

    if(i==n){

        if(j==0&&k==0)return 1e19;
        return 0;

    }

    if(dp[i][j][k]!=-1)return dp[i][j][k];

    double value = 1e19;

    if(j==0){

        value = min(value , f(i+1 , 1 , k)+

            dis(ax , ay , v[i].first , v[i].second)

            + dis(v[i].first , v[i].second , tx , ty));
    }

    if(k==0){

        value = min(value , f(i+1 , j , 1)+

            dis(bx , by , v[i].first , v[i].second)

            + dis(v[i].first , v[i].second , tx , ty));
    }



    value = min(value , f(i+1 , j , k)+2*dis(tx , ty , v[i].first , v[i].second));


    return dp[i][j][k] = value;
}

int main(void)
{
    for(int i=0;i<100005;i++){

        for(int j=0;j<2;j++){

            for(int k=0;k<2;k++){

                dp[i][j][k] = -1;
            }
        }
    }

    scanf("%lf %lf %lf %lf %lf %lf %d",&ax , &ay , &bx , &by , &tx , &ty , &n);

    for(int i=0;i<n;i++){

        double in1 , in2;
        scanf("%lf %lf",&in1 , &in2);

        v.push_back(make_pair(in1 , in2));
    }

    printf("%.14f\n",f(0 , 0 , 0));

    return 0;
}
