#include <stdio.h>
int main(void)
{
    int i,j;
    float f,g;
    scanf("%d %d %lf %lf",&i,&j,&f,&g);
    printf("%d %d\n%.lf %.lf", i+j,i-j,f+g,f-g);
    return 0;
}