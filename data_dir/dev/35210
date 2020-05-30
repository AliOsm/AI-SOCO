#include <cstdio>
#include <algorithm>
#include <iostream>
using namespace std ;

int main() {
    int N, M ;
    string S, S2, tmp ;
    int res = 0 ;

    cin >> S  ;
    cin >> S2 ;

    N = S.size() ;
    M = S2.size() ;

    for( int i=min(N,M), j; i; i-- ) {
        if( N%i || M%i )
            continue ;
        tmp = S.substr(0,i) ;
        for( j=0; j<N && S.substr(j,i)==tmp; j+=i ) ;
        if( j!=N )
            continue ;
        for( j=0; j<M && S2.substr(j,i)==tmp; j+=i ) ;
        if( j!=M )
            continue ;
        res ++ ;
    }

    printf("%d\n", res ) ;

    return 0 ;
}
