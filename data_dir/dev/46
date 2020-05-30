#include <cmath>
#include <cstdio>
#include <algorithm>
#include <iostream>
#include <vector>
#include <string>
#include <iomanip>
#include <climits>
#define F first
#define S second.first
#define T second.second
#define P3 pair<int,pair<int,int> >
#define MP make_pair
#define REP(n) for(int i = 0; i < n; i++)
#define PI 3.1415926535897932384626433832795028841971
#define EPS 1e-9

using namespace std;
typedef long double LD;
typedef long long LL;

int main()
{
	int n, t;
	string ret;
	cin >> n >> t;
	ret = "-1";
	if(n == 1)
	{
		REP(10)
		{ 
			if(i%t == 0 && i != 0)
				ret = to_string(i);
		}
	}
	else
	{
		ret = to_string(t);
		while(ret.size() < n) ret = ret+"0";
	}
	cout << ret;
	return 0;
}
