/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <stdio.h>

int main()
{  
    int i,k;
   for (i =2; i <= 9; i++){
       for (k = 1;k <= 9;k++ ){
           printf("%d*%d=%2d ",i,k,i*k);
       }
       printf("\n");
   }
   return 0;
}
