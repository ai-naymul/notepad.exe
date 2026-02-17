#include<iostream>
using namespace std;

int main(){
    int l, b;
    int area;
    int perimeter;
    cin >> l >> b;

    area = l * b;
    perimeter = 2 * (l+b);

    cout << "Area = " << area << endl;
    cout << "Perimeter = " << perimeter << endl;
}
