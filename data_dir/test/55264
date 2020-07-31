#include <bits/stdc++.h>
using namespace std;

int main() {
	#ifdef tajir
		freopen("input.txt","r",stdin);
	#else
		//online submission
	#endif

	char a,b;
	int c,d;

	scanf("%c%d",&a,&c);
	scanf(" %c%d",&b,&d);

	printf("%d\n",max(abs(a-b) , abs(c-d)) );
//	return 0;
	while(1) {
		if(a < b) {
			printf("R");
			a++;
		}
		else if(a > b) {
			printf("L");
			a--;
		}
		if(c < d) {
			printf("U");
			c++;
		}
		else if(c > d) {
			printf("D");
			c--;
		}
		printf("\n");

		if(a == b && c == d)	break;
	}

	return 0;
}