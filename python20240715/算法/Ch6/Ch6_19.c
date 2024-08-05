/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <stdio.h>

int main()
{ 
   float myNumber[5] = {1.2,3.4,5.7,8.3,6.5};
   printf("%.2f \n",myNumber[0]);   
   int i = 3;
   printf("%.2f \n",myNumber[i]);   
   printf("%.2f \n",myNumber[2]);
   myNumber[2] = 9.5;
   printf("%.2f",myNumber[2]);
   return 0;
}
