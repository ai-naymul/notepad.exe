#include<iostream>
using namespace std;


vector<int> findFactors(int n){
    vector<int> factors;
    for(int i=1;i<=n;i++){
        if(n%i==0){
            factors.push_back(i);
        }   
    }
    return factors;
}

int hcf(int a, int b){
    vector<int> aFactors = findFactors(a);
    vector<int> bFactors = findFactors(b);
}


int main(){
    int a,b;
    cin>> a >>b;
}