
 #include "bits/stdc++.h"
 using namespace std;
 int Array[100005] , T[100005];
 long long Ans[100005] , Parital[100005] , Extra[100005];

 int binary_search_( int low , int high , int start , long long key ){
 	if( low >= high ) return low;
 	else{
 		int middle = ( low + high ) >> 1;

 		if( Parital[middle] - Parital[start - 1] == key ) return middle;
 		else if( Parital[middle] - Parital[start - 1] > key ) return binary_search_( low , middle - 1 , start , key );
 		else if( Parital[middle] - Parital[start - 1] < key ) return binary_search_( middle + 1 , high , start , key );
 	}

 	return low;
 }

 int main(){
 	int N , i;
 	scanf( "%d" , &N );

 	for( i = 1 ; i <= N ; ++i )
 		scanf( "%d" , Array + i );
 	for( i = 1 ; i <= N ; ++i ){
 		scanf( "%d" , T + i );
 		Parital[i] = T[i] + Parital[i - 1];
 	}

 	int d;

 	for( i = 1 ; i <= N ; ++i ){
 		d = binary_search_( i , N , i , 1LL * Array[i] );

 		if( Parital[d] - Parital[i - 1] < 1LL * Array[i] ){
 			if( d < N ){
 				++Ans[i];
 				--Ans[d + 1];
 				Extra[d + 1] = Extra[d + 1] + ( Array[i] - ( Parital[d] - Parital[i - 1] ) ); 
 			}
 			else ++Ans[i];
 		}	
 		else{
 			if( d == i ) Extra[i] = Extra[i] + Array[i];
 			else{
 				++Ans[i];
 				--Ans[d];
 				Extra[d] = Extra[d] + ( Array[i] - ( Parital[d - 1] - Parital[i - 1] ) );  
 			}
 		}
 	}

 	for( i = 1 ; i <= N ; ++i )
 		Ans[i] = Ans[i] + Ans[i - 1];

 	for( i = 1 ; i <= N ; ++i )
 		Ans[i] = Ans[i] * T[i];

 	for( i = 1 ; i <= N ; ++i )
 		printf( "%lld " , Ans[i] + Extra[i] );

 	puts( "" );
 	return 0;
 }