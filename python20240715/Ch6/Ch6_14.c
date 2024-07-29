/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <stdio.h>

int main()
{  int score = 0;
   int sum = 0;
   int count = -1;
   while(score != -1){
       count++;
       sum += score; 
       printf("請輸入分數-1結束:");
       scanf("%d",&score);
   }
     printf("sum:%d",sum);
   return 0;
}
