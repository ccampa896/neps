#include <iostream>

using namespace std;

bool eh_primo(int x){
    int primo = 0;
	for(int i = 1; i <= x; i++){
        if(x % i == 0){
            primo += 1;
        }
    }
    if(primo == 2){
        return true;
    }
    else{
        return false;
    }
}

int main(){
	int x;

	cin>>x;

	if(eh_primo(x)){
		cout << "S" << "\n";
	}else{
		cout << "N" << "\n";
	}
}
