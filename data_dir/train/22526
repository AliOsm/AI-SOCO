#include <bits/stdc++.h>
using namespace std;

int n,m,i,j;
string s,ss;
vector<pair<string,int> > A;
int urutan[100005];

bool comp(pair<string,int> a,pair<string,int> b){
	return a.first < b.first;
}

int main(){
	ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
	cin >> n;
	for (i = 0 ; i < n ; i++) {
		cin >> s >> ss;
		A.push_back(make_pair(s,i));
		A.push_back(make_pair(ss,i));
	}
	for (i = 0 ; i < n ; i++){
		int temp;
		cin >> temp;
		urutan[i] = temp-1;
	}
	sort(A.begin(),A.end(),comp);
	//for (i = 0 ; i < A.size(); i++) {
		//cout << A[i].first << " " << A[i].second << '\n';
	//}
	j = 0;
	for (i = 0 ; i < A.size(); i++){
		if (A[i].second == urutan[j])
			j++;
		if (j==n) break;
	}
	cout << (j==n ? "YES" : "NO") << '\n';
	return 0;
}