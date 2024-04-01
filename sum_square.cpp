#define DLL_MACRO

#include "sum_square.h"

unsigned long sum_square(unsigned int n) {
	unsigned long res = 0;
	for (int i = 1; i <= n; i++) {
		res += i * i;
	}
	return res;
}