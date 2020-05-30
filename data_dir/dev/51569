
 #include "bits/stdc++.h"
 using namespace std;

 int First[26] , Last[26];

 int main(){
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);
  
  string Str , Temp;
  int i , N;
  cin >> Str >> N;
  char c2 , c1 = Str[0];
  c2 = Str[1];
  
     for( i = 1 ; i <= N ; ++i ){
      cin >> Temp; 
      First[Temp[0] - 'a'] = 1;
      Last[Temp[1] - 'a'] = 1;

         if( Temp == Str ){
          cout << "YES" << endl;
          return 0;
        }
    }
  
     if( First[c2 - 'a'] == 1 && Last[c1 - 'a'] == 1 )
      cout << "YES" << endl;
     else
      cout << "NO" << endl;   	
  
  return 0;
} 
