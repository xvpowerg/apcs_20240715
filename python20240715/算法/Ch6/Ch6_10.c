/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <stdio.h>

int main()
{  
   printf("1 Play\n");
   printf("2 Stop\n");
   printf("3 Exit\n");
   int action = 0;
   scanf("%d",&action);
   switch(action){
       case 1:
        printf("Play");
       break;
       case 2:
        printf("Stop");
       break;
       case 3:
        printf("Exit");
       break;
       default:
       printf("Error");
       
   }
   return 0;
}
