#include<iostream>
#include<vector>
using namespace std;

int main(){
    char ch;
    vector<char> arr = {'a','e','i','o','u'};
    cin>>ch;
    for(int i=0;i<arr.size();i++){
        if(ch==arr[i]){
            cout<<"YES"<<endl;
            return 0;
        }
    }
    cout<<"NO"<<endl;
}
