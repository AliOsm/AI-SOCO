#include<bits/stdc++.h>
using namespace std;

int get(string s){
    stringstream ss(s);
    int t; ss>>t; return t;
}

int main(){
    string s; cin>>s;
    int now=get(s);
    now=max(now,get(s.substr(0,s.size()-1)));
    s.erase(--(--s.end()));
    now=max(now,get(s));
    cout<<now<<endl;
}
