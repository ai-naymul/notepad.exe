#include<iostream>
using namespace std;

int main(){
    int num;
    cin>>num;
    int sum =0;
    if(num==0){
        cout<<1<<endl;
        return 0;
    }
    while(num>0){
        int digit = num % 10;
        num /= 10;
        if(digit==0){
            sum+=1;
        }
    }
    cout<<sum<<endl;
}
