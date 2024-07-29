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
   if (action == 1){
       printf("Play");
   }else if(action == 2){
       printf("Stop");
   }else if(action == 3){
       printf("Exit");
   }else{
       printf("Error");
   }
   return 0;
}
