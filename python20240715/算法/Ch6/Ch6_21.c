/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <stdio.h>
#define ROWS 2
#define LEN 3
int main()
{ 
    
    int myArray[ROWS][LEN] = {
        {1,2,3},
        {4,5,6}
    };
   
   printf("%d \n",myArray[0][1]);
   printf("%d \n",myArray[1][2]);
   
   int i,k;
   for (i = 0; i < ROWS; i++){
       
       for (k =0 ; k < LEN; k++){
           printf("%d ",myArray[i][k]);
           
       }
       printf("\n");
   }
   return 0;
}
