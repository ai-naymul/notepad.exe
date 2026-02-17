#include<iostream>
#include<vector>

using namespace std;

int main(){
    int n;
    int sum=0;
    cin>>n;
    for(int i=1;i<=n;i++){
        int num;
        cin>>num;
        if(num==0){
            sum +=1;
        } else if(18%num==0 || num%45==0){
            sum += 1;
        }
    }
    cout<<sum<<endl;
}
