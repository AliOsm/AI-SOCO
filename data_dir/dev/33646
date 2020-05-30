
#include "bits/stdc++.h"
using namespace std;
char Str[1000005];
int KMP[1000005];

void KMP_Algorithm(int length){
	int i , j;

	for( i = 1 ; i < length ; ++i ){
		j = i - 1;

		while( KMP[j] ){
			if( Str[KMP[j]] == Str[i] ){
				KMP[i] = KMP[j] + 1;
				break;
			} 
			
			j = KMP[j] - 1;
		}

		if( KMP[j] == 0 && Str[0] == Str[i] ) KMP[i] = 1;
	}
}

int Query( int length ){
	int i , j;
	j = length - 1;

	while( KMP[j] ){
		for( i = 1 ; i < length - 1 ; ++i ){
			if( KMP[i] == KMP[j] ) return KMP[i];
		}

		j = KMP[j] - 1;
	}

	return 0;
}

int main(){
	int N , length;
	scanf( "%s" , Str );
	N = strlen(Str);
	KMP_Algorithm(N);
	length = Query(N);

	if( length ){
		Str[length] = '\0';
		printf( "%s\n" , Str );
	}
	else puts( "Just a legend" );
	return 0;
}