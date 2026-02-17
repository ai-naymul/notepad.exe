#include<iostream>
using namespace std;

int main(){
    int x,n;
    cin>>x>>n;
    long long sum=1;
    if(n==0){
        cout<<1<<endl;
    }
    for(int i=1; i<=n; i++){
        sum = sum*x;
    }
    cout<<sum<<endl;
}
