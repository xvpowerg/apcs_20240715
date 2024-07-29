/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <stdio.h>

int main()
{ 
   int number[5] = {6,7,8,9,10};
   
   int i = 0;
   int len = sizeof(number) / sizeof(number[0]);
   for (;i < len; i++){
       
       printf("%d ",number[i]);
   }
   return 0;
}
