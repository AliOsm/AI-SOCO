#include <iostream>
#include <cmath>
using namespace std;

const int MAXN = 1000 * 100 + 10;
int mark[MAXN];

int main()
{
	int n, m;
	cin>> n >> m;

	int mn = n - 1;
	int mx = 0;
	for(int i = 0; i < m; i ++)
	{
		int a, b;
		cin>> a >> b;

		a --;
		b --;
		if(mark[max(a, b)] == 1)
		{
			cout<< 0 << endl;
			return 0;
		}
		if(mark[min(a, b)] == 2)
		{
			cout<< 0 << endl;
			return 0;
		}
		mark[max(a, b)] = 2;
		mark[min(a, b)] = 1;

		mx = max(min(a, b), mx);
		mn = min(max(a, b), mn);
	}

	if(mx > mn)
	{
		cout<< "0\n";
		return 0;
	}

	cout<< mn - mx << endl;

}