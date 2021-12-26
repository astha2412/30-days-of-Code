#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {   
    float mealValue;
    int tip;
    int tax;
    unsigned int total; 
    scanf("%f",(float *)&mealValue);
    scanf("%d",&tip);
    scanf("%d",&tax);
    
    total = round(mealValue + (mealValue*((float)tip/100)) + (mealValue*((float)tax/100)));
    printf("%d", (int)total);
    return 0;
}