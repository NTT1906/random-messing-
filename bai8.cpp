#include <iostream>
using namespace std;
int m, n, k;
int main(){
	cout << "Nhập m, n, k: ";
	cin >> m >> n >> k; //Nhập m, n, k
	if( (m < n) && (n < k) && ((n - m) == (k - n)) ){
		m = 2*m; //Nhân đôi
	    n = 2*n;
	    k = 2*k;
	}
	else
	{
	    m--; //Lấy m trừ mất 1
	    n--; //Lấy n trừ mất 1
	    k--; //Lấy k trừ mất 1
	}
	cout << "Output: m, n, k: " << m << " " << n << " " << k << endl;
}