#include<stdio.h>
#include<string.h>

int main()
{
    char string[50];
    char newstr[50];
    scanf("%s", string);
    //printf("%s\n", string);
    int n=strlen(string);
    int i;
    for(i=0; i<n; i++){
        //printf("%d\n",string[i]);
        //int cn;
        //cn=(int)string[i];
        if(string[i]>=97 && string[i]<=123){
            int up=string[i]-97;
            newstr[i]=65+up;
        }
    }
    printf("%s",newstr);
}