#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

int n;
const int n_ = 701;
bool g[n_][n_];
vector<int> bigger[n_];
vector<int> smaller[n_];
int a[n_];
int mem[2][n_][n_];
int LEFT = 0, RIGHT = 1;
int dp(int lst, int s, int e)
{
    if(s == e) return g[s][lst == LEFT ? s - 1: s + 1];
    int &ret = mem[lst][s][e];
    if(ret != -1) return ret;
    ret = 0;
    if(lst == LEFT)
    {
        for(int j : bigger[s - 1])
        {
            if(j > e) break;
            if(j == s)
            {
                ret = max(ret, 1 + dp(LEFT, s + 1, e));
                if(ret == e - s + 1) break;
            } else if(j == e)
            {
                ret = max(ret, 1 + dp(RIGHT, s, e - 1));
                if(ret == e - s + 1) break;
            } else {
                ret = max(ret, 1 + dp(RIGHT, s, j - 1) + dp(LEFT, j + 1, e));
                if(ret == e - s + 1) break;
            }
        }
    } else {
        for(int i = (int)smaller[e + 1].size() - 1; i >= 0; i--)
        {
            int j = smaller[e + 1][i];
            if(j < s) break;
            if(j == s)
            {
                ret = max(ret, 1 + dp(LEFT, s + 1, e));
                if(ret == e - s + 1) break;
            } else if(j == e)
            {
                ret = max(ret, 1 + dp(RIGHT, s, e - 1));
                if(ret == e - s + 1) break;
            } else {
                ret = max(ret, 1 + dp(RIGHT, s, j - 1) + dp(LEFT, j + 1, e));
                if(ret == e - s + 1) break;
            }
        }
    }
    return ret;
}
int main()
{
	scanf("%d", &n);
	for(int i = 0; i < n; i++)
	    scanf("%d", a + i);

	for(int i = 0; i < n; i++)
	    for(int j = i + 1; j < n; j++) {
            g[i][j] = g[j][i] = __gcd(a[i], a[j]) > 1;
            if(g[i][j]) {
                bigger[i].push_back(j);
            }
        }
    for(int i = 0; i < n; i++) {
	    for(int j = 0; j < i; j++) {
	        if(g[i][j]) {
	            smaller[i].push_back(j);
	        }
	    }
	}

	memset(mem, -1, sizeof mem);
	for(int i = 0; i < n; i++) {
	    int res = 0;
	    if(!i)
        {
            res = dp(LEFT, i + 1, n - 1);
        } else if(i == n - 1)
        {
            res = dp(RIGHT, 0, n - 2);
        } else
        {
            res = dp(RIGHT, 0, i - 1) + dp(LEFT, i + 1, n - 1);
        }
        if(res + 1 == n) {
	        cout << "Yes\n";
	        return 0;
	    }
	}
	cout << "No\n";
}