#include <iostream>
#include <cmath>
using namespace std;
int j, s, n, i, e, f;
int main(){
	cout << "Nhap n: ";
	cin >> n;
	for(i = 1; i <= n; i++){
		for(int j = n; j > i; j--) cout << " ";
		e = 0;
		f = 1;
		for(j = 1; j<=i; j++){
			s = e + f;
			e = f;
			f = s;
			cout << s << " ";
		}
		cout << endl;
	}
	return 0;
}