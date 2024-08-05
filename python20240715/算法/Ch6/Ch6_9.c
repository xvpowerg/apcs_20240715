/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <stdio.h>

int main()
{  
   int score = 75;
   
   if (score >= 90){
       printf("A");
   }else if(score >= 80 && score < 90){
       printf("B");
   }else if(score >= 70 && score < 80){
       printf("C");
   }else if(score >= 60 && score < 70){
        printf("D");
   }else{
         printf("F");
   }
   return 0;
}
