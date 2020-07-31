#pragma comment(linker, "/stack:252457298")
#pragma GCC optimize("Ofast")

#include <bits/stdc++.h>
using namespace std;

#define endl '\n'
mt19937 rng32(chrono::steady_clock::now().time_since_epoch().count());
mt19937_64 rng64(chrono::steady_clock::now().time_since_epoch().count());

vector<int> x(667), y(667);
vector<int> rowrook(1001, 0), colrook(1001, 0);
vector<vector<bool>> occ(1001, vector<bool>(1001, false));

bool meetMiddle = false;

void Input() {
	for (int i=0; i<667; i++) {
		cin >> x[i] >> y[i];
		if (i == 0) continue;
		rowrook[x[i]]++; colrook[y[i]]++;
		occ[x[i]][y[i]] = true;
	}
}

void Solve() {
	int NW = 0, NE = 0, SW = 0, SE = 0;
	bool goNW = false, goNE = false, goSW = false, goSE = false;
	
	while (true) {
		for (int i=-1; i<=1; i++) {
			for (int j=-1; j<=1; j++) {
				if (i == 0 && j == 0) continue;
				if (x[0]+i < 1 || x[0]+i > 999) continue;
				if (y[0]+j < 1 || y[0]+j > 999) continue;
				if (occ[x[0]+i][y[0]+j]) continue;
				if (rowrook[x[0]+i] || colrook[y[0]+j]) {
					cout << x[0]+i << " " << y[0]+j << endl;
					fflush(stdout);
					int K, X, Y; cin >> K >> X >> Y;
					if (K == 0) {cerr << "Error found.\n"; return;}
					if (K == -1 && X == -1 && Y == -1) return;
					occ[x[K]][y[K]] = false; rowrook[x[K]]--; colrook[y[K]]--;
					x[K] = X; y[K] = Y; occ[X][Y] = true; rowrook[X]++; colrook[Y]++;
				}
			}
		}
		
		if (!meetMiddle && (x[0] != 500 || y[0] != 500)) {
			if (x[0] < 500 && y[0] < 500) {
				x[0] += 1; y[0] += 1; cout << x[0] << " " << y[0] << endl; fflush(stdout);
			}
			
			else if (x[0] < 500 && y[0] == 500) {
				x[0] += 1; y[0] += 0; cout << x[0] << " " << y[0] << endl; fflush(stdout);
			}
			
			else if (x[0] < 500 && y[0] > 500) {
				x[0] += 1; y[0] -= 1; cout << x[0] << " " << y[0] << endl; fflush(stdout);
			}
			
			else if (x[0] == 500 && y[0] < 500) {
				x[0] += 0; y[0] += 1; cout << x[0] << " " << y[0] << endl; fflush(stdout);
			}
			
			else if (x[0] == 500 && y[0] > 500) {
				x[0] += 0; y[0] -= 1; cout << x[0] << " " << y[0] << endl; fflush(stdout);
			}
			
			else if (x[0] > 500 && y[0] < 500) {
				x[0] -= 1; y[0] += 1; cout << x[0] << " " << y[0] << endl; fflush(stdout);
			}
			
			else if (x[0] > 500 && y[0] == 500) {
				x[0] -= 1; y[0] += 0; cout << x[0] << " " << y[0] << endl; fflush(stdout);
			}
			
			else if (x[0] > 500 && y[0] > 500) {
				x[0] -= 1; y[0] -= 1; cout << x[0] << " " << y[0] << endl; fflush(stdout);
			}
			
			int K, X, Y; cin >> K >> X >> Y;
			if (K == 0) {cerr << "Error found.\n"; return;}
			if (K == -1 && X == -1 && Y == -1) return;
			occ[x[K]][y[K]] = false; rowrook[x[K]]--; colrook[y[K]]--;
			x[K] = X; y[K] = Y; occ[X][Y] = true; rowrook[X]++; colrook[Y]++;
			continue;
		}
		
		if (!meetMiddle && x[0] == 500 && y[0] == 500) {
			meetMiddle = true;
			
			for (int i=1; i<1000; i++) {
				for (int j=1; j<1000; j++) {
					if (!occ[i][j]) continue;
					NW++; NE++; SW++; SE++;
					if (i < 500 && j < 500) SE--;
					if (i < 500 && j > 500) SW--;
					if (i > 500 && j < 500) NE--;
					if (i > 500 && j > 500) NW--;
				}
			}
			
			if (NW == max({NW, NE, SW, SE})) goNW = true;
			else if (NE == max({NW, NE, SW, SE})) goNE = true;
			else if (SW == max({NW, NE, SW, SE})) goSW = true;
			else if (SE == max({NW, NE, SW, SE})) goSE = true;
		}
		
		if (meetMiddle && goNW) {
			x[0]--; y[0]--; cout << x[0] << " " << y[0] << endl; fflush(stdout);
		}
		
		else if (meetMiddle && goNE) {
			x[0]--; y[0]++; cout << x[0] << " " << y[0] << endl; fflush(stdout);
		}
		
		else if (meetMiddle && goSW) {
			x[0]++; y[0]--; cout << x[0] << " " << y[0] << endl; fflush(stdout);
		}
		
		else if (meetMiddle && goSE) {
			x[0]++; y[0]++; cout << x[0] << " " << y[0] << endl; fflush(stdout);
		}
		
		else {cout << NW << "-" << NE << "-" << SW << "-" << SE << "|" << goNW << goNE << goSW << goSE << endl; fflush(stdout); return;}
			
			int K, X, Y; cin >> K >> X >> Y;
			if (K == 0) {cerr << "Error found.\n"; return;}
			if (K == -1 && X == -1 && Y == -1) return;
			occ[x[K]][y[K]] = false; rowrook[x[K]]--; colrook[y[K]]--;
			x[K] = X; y[K] = Y; occ[X][Y] = true; rowrook[X]++; colrook[Y]++;
			continue;
	}
}

int main(int argc, char* argv[]) {
	ios_base::sync_with_stdio(0);
	Input(); Solve(); return 0;
}

/**********************************************\
*  Ngoc-Mai Ngo, #Team4T's Deputy Leader     *
*  #Team4T Secondary Flagship - Destruction  *
\**********************************************/
