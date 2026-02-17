#include<iostream>
using namespace std;

int main(){
    int n;
    long long sum=0;
    cin>>n;
    for(int i=0;i<=n;i++){
        sum+=i;
    }
    cout<<sum<<endl;
}
