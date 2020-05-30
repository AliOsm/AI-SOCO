#include <iostream>
#include <vector>
#include <string>
#include <vector>
#include <queue>
#include <deque>
#include <set>
#include <map>
#include <cmath>
#include <algorithm>
#include <cassert>
#include <tuple>
#include <functional>
#include <unordered_set>
#include <unordered_map>
#include <sstream>
#include <stdio.h>



#define forn(i,n) for(int i=0;i<(int)(n); i++)
#define forsn(i,s,n) for(int i=(s);i<(int)(n); i++)
#define esta(x,v) (find((v).begin(),(v).end(),(x)) !=  (v).end())
#define index(x,v) (find((v).begin(),(v).end(),(x)) - (v).begin())
#define debug(x) cout << #x << " = "  << x << endl

typedef long long tint;
typedef unsigned long long utint;

using namespace std;



void imprimirVector (vector<int> v)
{
	if (!v.empty())
	{ 
		int p = v.size();
		cout << "[";
		forn(i,p-1)
			cout << v[i] << ",";
		cout << v[p-1] << "]" << endl;
	}
	else
		cout << "[]" << endl;
}

int toNumber (string s)
{
	int Number;
	if ( ! (istringstream(s) >> Number) ) Number = 0; // el string vacio lo manda al cero
	return Number;
}

string toString (int number)
{    
    ostringstream ostr;
    ostr << number;
    return  ostr.str();
}




int main()
{
	ios_base::sync_with_stdio(0);
	tint n;
	cin >> n;
	vector<string> word (n);
	forn(i,n)
		cin >> word[i];
	vector<char> l = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};
	tint maxTotal = 0;
	forn(i,26)
	{
		forn(j,26)
		{
			tint total = 0;
			for (auto w : word)
			{
				tint largo = w.size();
				bool tutti = true;
				forn(k,largo)
					tutti &= ((w[k] == l[i]) or (w[k] == l[j]));
				if (tutti)
					total += largo;				
			}
			maxTotal = max(maxTotal,total);
		}
	}
	cout << maxTotal << endl;
	return 0;
}



