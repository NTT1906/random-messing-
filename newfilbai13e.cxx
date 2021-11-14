#include <iostream>
#include <cmath>
using namespace std;
int main(){
	int n, i, j, dem;
	cin >> n;
	for(i=2; i<n; i++){
		dem = 0;
		while(j <= sqrt(i)){
			if(i % j == 0) dem++;
			j++;
		}
		//for(j = 2; j<=sqrt(i); j++){
//			if(i % j == 0) dem++;
//		}
		if(dem == 0) cout << i << endl;
	}
	return 0;
}