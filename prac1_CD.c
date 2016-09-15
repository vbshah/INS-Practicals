#include <stdio.h>
#include <string.h>
int main(){
	int n,i;
	printf("Type the number of line : ");
	scanf("%d",&n);
	for(i=0;i<n;i++){
		char s[255];
		scanf("%s",s);
		int j=0,len=strlen(s);
		while(j<len && s[j]==' '){				
			j++;
		}
//		printf("two %c %c",s[j],s[j+1]);
		if((s[j]=='/' && s[j+1]=='/') || (s[j]=='/' && s[j+1]=='*')){
			printf("Given line is comment\n");		
		}
		else{
			printf("Given line is not a comment\n");		
		}
	}
	return 0;
}
