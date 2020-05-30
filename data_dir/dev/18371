#include<bits/stdc++.h>
using namespace std;

ostringstream ostm(ios_base::ate);

void go(){
    string s;
    if(!(cin>>s)){
        cout<<"Error occurred"<<endl;
        exit(0);
    }
    if(s=="pair"){
        ostm<<"pair<";
        go();
        ostm<<",";
        go();
        ostm<<">";
    }
    else{
        ostm<<s;
    }
}

int main(){
    int n; cin>>n;
    go();
    string s; if(cin>>s){
        cout<<"Error occurred"<<endl;
        exit(0);
    }
    cout<<ostm.str()<<endl;
}
