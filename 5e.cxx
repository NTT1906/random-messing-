#include <iostream>
#include <cmath>
using namespace std;
int x, s, n, i;
int main(){
	cout << "Nhap x, n: ";
	cin >> x >> n;
	s = 0;
	for(i = 1; i <= n; i++) s+=pow(x, i)*pow(-1,i+1);
	cout << s;
	return 0;
}