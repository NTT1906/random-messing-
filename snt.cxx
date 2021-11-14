#include <iostream>
using namespace std;
int main(){
	int n, i;
	cin >> n;
	bool check[n+1];
	memset(check, true, n+1);
	for(int i  = 2; i <= n; i++){
		if(check[i]){
			for(int j = 2*i; j <= n; j += i) check[j] = false;
		}
	}
	for(i= 2; i <= n; i++) if(check[i]) cout << i << " ";
	return 0;
}