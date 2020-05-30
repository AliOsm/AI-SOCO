#include<iostream>

#define int long long

using namespace std;

const int MAXN = 55, mod = 1e9 + 7;
int mp[300];

struct matrix 
{
	int a[MAXN][MAXN], sz;
	matrix (int sz) :sz(sz) 
	{
		for(int i = 0; i < sz; i++)
			for(int j = 0; j < sz; j++)
				a[i][j] = (i == j);
	}
	matrix operator * (matrix b)
	{
		matrix ans(sz);
		for(int i = 0; i < sz; i++)
			for(int j = 0; j < sz; j++)
			{
				ans.a[i][j] = 0;
				for(int k = 0; k < sz; k++)
					ans.a[i][j] = (ans.a[i][j] + a[i][k] * b.a[k][j]) % mod;
			}
		return ans;
	}

	matrix operator ^ (int p)
	{
		if(p == 0)
		{
			matrix tmp(sz);
			return tmp;
		}
		matrix ans = *this ^ (p / 2);
		ans = ans * ans;
		if(p % 2 == 1)
			ans = ans * *this;
		return ans;
	}
};

main()
{
	int n, m, k;
	cin >> n >> m >> k;
	for(int i = 'a'; i <= 'z'; i++)
		mp[i] = i - 'a';
	for(int i = 'A'; i <= 'Z'; i++)
		mp[i] = 26 + i - 'A';
	matrix a(m);
	for(int i = 0; i < m; i++)
		for(int j = 0; j < m; j++)
			a.a[i][j] = 1;
	for(int i = 0; i < k; i++)
	{
		char c1, c2;
		cin >> c1 >> c2;
		a.a[mp[c1]][mp[c2]] = 0;
	}
	matrix p = a ^ (n - 1);
	matrix ans(m);
	for(int i = 0; i < m; i++)
		ans.a[i][0] = 1;
	matrix res = p * ans;
	int sum = 0;
	for(int i = 0; i < m; i++)
		sum += res.a[i][0];
	cout << sum % mod << endl;
	return 0;
}
