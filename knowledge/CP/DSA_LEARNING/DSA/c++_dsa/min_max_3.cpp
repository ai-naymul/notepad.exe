#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int main(){
    int a,b,c;
    cin>>a>>b>>c;
    vector<int> arr = {a,b,c};
    int max_value = arr[0];
    int min_value = arr[0];

    for(int i=0;i<arr.size();i++){
        max_value = max(max_value, arr[i]);
        min_value = min(min_value, arr[i]);
    }

    cout << "Min = "<<min_value<<endl;
    cout<<"Max = "<<max_value<<endl;
}
