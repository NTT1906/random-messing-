#include <iostream>
using namespace std;
int a(int n){
	int s = 0;
	for(int i = 1; i<=2*n+1; i+=2) s+=i;
	return s;
}

int main(){
	cout << a(3) <<endl;
	cout << int a = (for(int i = 1; i<=10; i++) a++);
	return 0;
}