#include <bits/stdc++.h>
using namespace std;
const int limB = 1<<20;
const int limN = 20;

bool usdA[limB][limN], usdB[limB][limN];
int ansA[limB][limN], ansB[limB][limN];

int ja(int n, int k);
int jb(int n, int k);

int ja(int n, int k) {
    if(k==2)
        return n;
    if(usdA[n][k])
        return ansA[n][k];
    usdA[n][k] = true;
    int &ans = ansA[n][k];
    ans = jb(n>>1, k-1);
    for(int i=1; i<k; i++) {
        ans = min(ans, jb( ((n>>(i+1))<<i) + n%(1<<i), k-1) );
    }
    return ans;
}

int jb(int n, int k) {
    if(k==2)
        return n;
    if(usdB[n][k])
        return ansB[n][k];
    usdB[n][k] = true;
    int &ans = ansB[n][k];
    ans = ja(n>>1, k-1);
    for(int i=1; i<k; i++) {
        ans = max(ans, ja( ((n>>(i+1))<<i) + n%(1<<i), k-1) );
    }
    return ans;
}

void pint(int n, int k) {
    int w = 0;
    for(int i=k-1; i>=0; i--) {
        printf("%d", (1<<i) & n? 1 : 0);
        if((1<<i) & n)
            w ++;
    }
    printf(" => %d\n", w);
}

char str[limB];

int main() {
    // int n = 0, k = 0;
    // char str[100];

    // // scanf("%s", str);
    // // for(char *c=str; *c; c++) {
    // //     n = n*2 + *c-'0';
    // //     k++;
    // // }

    // int k;
    // scanf("%d", &k);
    // vector<int> ans[4];
    // for(int i=(1<<k)-1; i>=0; i--) 
    //     // printf("%d => %d\n", i, ja(i, k));
    //     ans[ja(i,k)].push_back(i);
    // for(int i=0; i<4; i++) {
    //     printf("==== %d\n", i);
    //     for(const int c : ans[i])
    //         pint(c, k);
    // }
    // return 0;
    scanf("%s", str);
    int mino=0, maxo=0, n=0;
    char ut = '?';
    for(char *c = str; *c; c++) {
        mino += *c=='1'? 1 : 0;
        maxo += *c!='0'? 1 : 0;
        ut = *c;
        n++;
    }

    n = (n+1)/2;
    // printf("%d %d %d\n", mino, maxo, n);
    if(mino <= n-1)
        printf("00\n");
    if(mino <= n && n <= maxo) {
        if(ut=='1' || (ut=='?' && mino+1 <= n) )
            printf("01\n");
        if(ut=='0' || (ut=='?' && n <= maxo-1))
            printf("10\n");
    }
    if(n+1 <= maxo)
        printf("11\n");
}
