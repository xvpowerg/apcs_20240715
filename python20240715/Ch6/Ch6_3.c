/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <stdio.h>

int main()
{
    int input1;
    float input2;
    char input3[10];
    
    printf("輸入整數:");
    scanf("%d",&input1);
    printf("您輸入的整數是:%d\n",input1);
    
    printf("輸入浮點數:");
    scanf("%f",&input2);
    printf("您輸入的浮點數:%f\n",input2);
    
    printf("請輸入文字:");
    scanf("%10s",&input3);
    printf("文字:%s\n",input3);
    
    
    return 0;
}
