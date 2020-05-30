#include <cstdio>
#include <algorithm>
#include <iostream>
using namespace std ;

int main() {
    freopen( "input.txt", "r", stdin ) ;
    freopen( "output.txt", "w", stdout ) ;

    int N ;
    char arr[1005] ;

    scanf("%d", &N ) ;
    scanf("%s", arr ) ;

    for( int i=0; i<N/2; i++ )
        if( arr[i]=='R' && arr[i+N/2]=='L' )
            printf("%d %d\n", i+N/2+1, i+1 ) ;
        else
            printf("%d %d\n", i+1, i+N/2+1 ) ;

    return 0 ;
}
