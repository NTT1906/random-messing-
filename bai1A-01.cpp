#include <iostream>
using namespace std;
int n, i, j, ucln, d, tem;
int main(){
	cout << "Nhập n: ";
	cin >> n;
	int a[n+1], out[n+1];
	int o = 1;
	for(i = 1; i <= n; i++) cin >> a[i];
	out[o] = a[1];
	for(i = 1; i <= n; i++){
	    for(j = i+1; j <= n; j++){
	        ucln = a[i];
	        d = a[j];
	        while(c != 0){
	            tem = ucln % d;
	            ucln = d;
	            d = tem;
	        }
	        ucln = b;
	        if(ucln == 1){
	            o++;
	            out[o]=a[j];
	            i = j;
	        }
	    }
	}
	cout << o << endl;
	for(i = 1; i<=o; i++) cout << out[i] << "  ";
}