#ifdef _WIN32
#  define LL "%I64d"
#else
#  define LL "%Ld"
#endif

#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <ctime>
#include <vector>
#include <deque>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <bitset>
#include <string>
#include <algorithm>
#include <complex>
#include <utility>
#include <cassert>
using namespace std;
#define null NULL
#define mp make_pair
#define pb(a) push_back(a)
#define sz(a) ((int)(a).size())
#define all(a) a.begin() , a.end()
#define fi first
#define se second
#define relaxMin(a , b) (a) = min((a),(b))
#define relaxMax(a , b) (a) = max((a),(b))
#define SQR(a) ((a)*(a))
typedef vector<int> vi;
typedef pair<int,int> pii;
typedef long long ll;
const int oo = 1E9;
#define MAXS 100010
int M , K;
int A[MAXS] , b[MAXS] , r[MAXS];
int emp , bad , bads[MAXS] , bade;
bool badu[MAXS];
void doit(){
  scanf("%d%d" , &M , &K);
  for(int i=0;i<K;++i) scanf("%d" , &A[i]);
  bad = M , emp = 0;
  for(int i=0;i<M-1;++i){
    scanf("%d%d" , &b[i] , &r[i]);
    if(r[i] == 1 && bad == M){
     bad = i;
     bade = emp;
     memcpy(bads , A , K * sizeof(int));
                             }
    if(b[i] == 0) ++emp;
    else --A[b[i] - 1];
                        }
  memset(badu , 0 , K * sizeof(bool));
  for(int i=bad;i<M-1;++i)
   if(b[i]) badu[b[i] - 1] = true;
  if(bad == M){
   for(int s=0;s<K;++s)
    if(A[s] == 0 || emp >= A[s]) printf("Y");
    else printf("N");
              }
  else{
   int mtake = oo;
   for(int i=0;i<K;++i)
    if(!badu[i] && bads[i] < mtake)
     mtake = bads[i];
   for(int s=0;s<K;++s){
    if(A[s] == 0){
     printf("Y");
     continue;
                 }
    // Finish on top
    if(!badu[s] && bade >= bads[s]){
     printf("Y");
     continue;
                                   }
    // Finish on bottom
    int ost = A[s];
    int _emp = emp;
    if(!b[bad]) --ost , --_emp;
    if(ost == 0 || _emp - mtake >= ost){
     printf("Y");
     continue;
                                       }
    printf("N");
                       }
      }
  puts("");
}
int main(){
  int Q;
  scanf("%d" , &Q);
  while(Q-- > 0) doit();
  return 0;
}
