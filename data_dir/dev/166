#include <bits/stdc++.h>

using namespace std;

const int N = 503;

int n, m, A[N][N], B[N][N], mat[N][N];

int main(){

    scanf("%d %d", &n, &m);
    
    for(int i = 0; i < n; i++) for(int j = 0; j < m; j++)
        scanf("%d", &A[i][j]);

    for(int i = 0; i < n; i++) for(int j = 0; j < m; j++)
        scanf("%d", &B[i][j]);

    for(int i = 0; i < n; i++) for(int j = 0; j < m; j++)
        mat[i][j] = A[i][j] ^ B[i][j];

    for(int i = 0; i < n; i++){
        int ans = 0;
        for(int j = 0; j < m; j++) ans += mat[i][j];
        if(ans % 2) return printf("No\n"), 0;
    }

    for(int j = 0; j < m; j++){
        int ans = 0;
        for(int i = 0; i < n; i++) ans += mat[i][j];
        if(ans % 2) return printf("No\n"), 0;
    }

    printf("Yes\n");
}
