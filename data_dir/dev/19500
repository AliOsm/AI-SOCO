#include <algorithm>
#include <cstdio>
#include <iostream>
#include <set>
using namespace std ;

int main() {
    int N ;
    long long sum = 0LL ;
    set< long long > S ;

    scanf("%d", &N ) ;

    for( int i=1; sum<=N; i++ ) {
        sum += i ;
        S.insert( sum ) ;
        if( S.find( N-sum ) != S.end() ) {
            printf("YES\n" ) ;
            return 0 ;
        }
    }

    printf("NO\n" ) ;

    return 0 ;
}
