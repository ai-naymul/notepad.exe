#include<iostream>
using namespace std;

int main(){
    int n;
    cin>>n;
    int pos=0,neg=0,ev=0,od=0;
    for(int i=0;i<n;i++){
        int num;
        cin>>num;
        if(num<0){
            neg += 1;
        }

        if(num>0){
            pos +=1;
        }
        if(num%2==0){
            ev +=1;
        }
        if(num%2!=0){
            od +=1; 
        }

    }

    cout<<pos<<endl;
    cout<<neg<<endl;
    cout<<ev<<endl;
    cout<<od<<endl;
}
