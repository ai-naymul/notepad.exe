#include<iostream>
using namespace std;


bool checkPrime(int n){
    int cnt=0;
    for(int i=1;i<=n;i++){
        if(n%i==0){
            cnt++;
        }
    }
    if(cnt==2){
        return true;
    }
    else{
        return false;
    }
}

void printPrimes(int n){
    if(checkPrime(n)){
        cout<< n <<" ";
    }
}


int main(){
    int n;
    cin>>n;
    for(int i=2;i<=n;i++){
        printPrimes(i);
    }
}