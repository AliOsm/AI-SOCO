#include <cstring>
#include <cassert>
#include <cstdio>
#include <string>
#include <cmath>
#include <vector>
#include <iostream>
#include <map>
#include <set>
#include <algorithm>
#include <queue>
#include <sstream>
using namespace std;
#define REP(i,n) for(int i=0;i<(int)(n);i++)

typedef long long ll;
typedef long long HASH;


bool isPrime(int v)
{
	for(int i=2;i*i<=v;i++)
		if(v%i==0)
			return false;
	return true;
}

const int MAXN=300000;
const int MODCNT=5;
char s[MAXN];
char t[MAXN];
const int MUL=37;
HASH mod[MODCNT];
HASH hashS[MODCNT][MAXN];
HASH hashT[MODCNT][26];
HASH PW[MODCNT][MAXN];
vector<int> posS[26], posT[26];

bool okay;
int to[26];

void update(int i, int v)
{
	if(to[i]!=v && to[i]!=-1)
		okay=false;
	to[i]=v;
}

int main()
{
	{
		int mtop=0;
		for(int i=1000000007;mtop<MODCNT;i++)
			if(isPrime(i))
				mod[mtop++]=i;
		REP(i,MODCNT)
		{
			PW[i][0]=1;
			for(int j=1;j<MAXN;j++)
				PW[i][j]=PW[i][j-1]*MUL%mod[i];
		}
	}

	int sl,tl;
	scanf("%d%d",&sl,&tl);
//	REP(i,sl)
//		s[i]='a'+rand()%26;
//	REP(j,tl)
//		t[j]='a'+rand()%26;
	scanf("%s%s",s,t);
	REP(i,sl)
		posS[s[i]-'a'].push_back(i);
	REP(i,tl)
		posT[t[i]-'a'].push_back(i);
	REP(i,MODCNT)
	{
		hashS[i][0]=0;
		REP(j,sl)
			hashS[i][j+1]=(hashS[i][j]*MUL+s[j]-'a')%mod[i];
		REP(j,26)
		{
			hashT[i][j]=0;
			REP(k,tl)
				hashT[i][j]=(hashT[i][j]*MUL+(t[k]=='a'+j))%mod[i];
		}
	}

	vector<int> res;
	for(int i=0;i+tl<=sl;i++)
	{
		okay=true;
		memset(to,-1,sizeof(to));
		REP(j,26)
		{
			if(posT[j].empty()) continue;
			int p=posT[j][0];
			update(s[i+p]-'a',t[p]-'a');
			update(t[p]-'a',s[i+p]-'a');
		}
		REP(j,26)
		{
			int p=lower_bound(posS[j].begin(), posS[j].end(), i)-posS[j].begin();
			if(p==posS[j].size()) continue;
			p=posS[j][p];
			if(i<=p && p<i+tl)
			{
				update(s[p]-'a',t[p-i]-'a');
				update(t[p-i]-'a',s[p]-'a');
			}
		}
		if(okay)
		{
			REP(j,MODCNT)
			{
				HASH hS=((hashS[j][i+tl]-hashS[j][i]*PW[j][tl])%mod[j]+mod[j])%mod[j];
				HASH hT=0;
				REP(k,26)
				{
					hT=(hT+to[k]*hashT[j][k])%mod[j];
				}
				okay&=hS==hT;
			}
		}
		if(okay) res.push_back(i+1);
	}
	printf("%u\n",res.size());
	REP(i,res.size())
	{
		printf("%d ",res[i]);
	}

	return 0;
}
