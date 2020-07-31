#include <iostream>
#include <algorithm>
using namespace std;

int k;

int sum(long long x)
{
	int s = 0;
	while(x > 0)
	{
		s += x % 10;
		x /= 10;
	}
	return s;
}

int main()
{
	cin >> k;

	long long counter = 0, i = 1;
	while(counter < k)
	{
		if(sum(i) <= 10)
			counter++;
		i++;
	}

	i--;
	cout << (i * 10) + (10 - sum(i)) << "\n";
	return 0;
}