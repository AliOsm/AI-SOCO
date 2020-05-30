#include<bits/stdc++.h>
using namespace std;

void meow(int n,int b){
    stack<int> st;
    while(n){
        st.push(n%b);
        n/=b;
    }
    while(st.size()){
        cout<<st.top();
        st.pop();
    }
}
int main(){
    int n; cin>>n;
    for(int i=1;i<n;++i){
        for(int j=1;j<n;++j){
            meow(i*j,n);
            cout<<" ";
        } cout<<endl;
    }
}
