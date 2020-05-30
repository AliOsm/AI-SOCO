#include <iostream>
#include <fstream>

#include <bits/stdc++.h>

using namespace std;

const int N = 2e5 + 9,M = 1e9, OO = 1e9;

int arr[N];

class BEmotes {
public:
	void solve(std::istream& cin, std::ostream& cout) {
		cout << fixed << setprecision(2);
		ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
		int n, k, m;
		cin >> n >> k >> m;
		for (int i = 0; i < n; ++i) {
			cin >> arr[i];
		}
		sort(arr, arr+n, greater<int>());
		int mxNum = arr[0], mxSc = arr[1];
//		cout << n << " " << k << " " << m;
		unsigned long long scc = k/(m+1), sff;
		sff = k - scc;
//		cout << sff << " " << scc;
		scc *= mxSc;
		sff *= mxNum;
		sff += scc;
		cout << sff;
	}
};


int main() {
	BEmotes solver;
	std::istream& in(std::cin);
	std::ostream& out(std::cout);
	solver.solve(in, out);
	return 0;
}