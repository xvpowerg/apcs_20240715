/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <stdio.h>

int main()
{  
    int input = 0;
    int remain = 0;
    printf("請輸入數字:");
    scanf("%d",&input);
    remain = input % 2;
    printf("是否為奇數?%c",remain?'Y':'N');
   return 0;
}
