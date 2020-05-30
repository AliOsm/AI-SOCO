#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair <ll, ll> pll;

ll N, D, A, B, ANS, ACU;
pll L[100005];

int main() {
    scanf("%lld %lld", &N, &D);

    for(int i=0;i<N;i++)
        scanf("%lld %lld", &L[i].first, &L[i].second);

    sort(L, L + N);

    ANS = ACU = L[0].second;

    while(B < N - 1) {
        if(L[B+1].first - L[A].first < D) 
            ACU += L[++B].second;
        else
            ACU -= L[A++].second;
        ANS = max(ANS, ACU);
    }

    printf("%lld\n", ANS);

    return 0;
}