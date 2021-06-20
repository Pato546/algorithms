#include <iostream>

using namespace std;

int binary_search(int arrays[], int item, int size) {
	int min_ = 0;
	int max_ = size - 1; 
	
	while (min_ <= max_) {
		int mid = (min_ + max_) / 2;
		if (arrays[mid] == item) {
			return mid;
		}
		if (arrays[mid] > item) {
			max_ = mid -1;
		}else {
			min_ = mid + 1;
		}
	}
	return -1;
}

int binary_search(string arrays[], string item, int size) {
	int min_ = 0;
	int max_ = size - 1; 
	
	while (min_ <= max_) {
		int mid = (min_ + max_) / 2;
		if (arrays[mid] == item) {
			return mid;
		}
		if (arrays[mid] > item) {
			max_ = mid -1;
		}else {
			min_ = mid + 1;
		}
	}
	return -1;
}


int main() {
	int arrays[] = {1, 2, 3, 4, 5, 6, 7, 8};
	string names[] = {"Ababio", "Patrick"};
	int n = sizeof(names) / sizeof(names[0]);
	int size = sizeof(arrays) / sizeof(arrays[0]);
	cout <<  binary_search(arrays, 6, size) << endl;
	cout <<  binary_search(names, "Ababio", n) << endl;
	return 0;
}
