/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
int main()
{ 
 
    srand(time(0));
    int gus;
    int ans = (rand() % 5) + 1 ;
    printf("ans:%d\n",ans);
    
    while(1){
        printf("1-5猜一個數字:");
        scanf("%d",&gus);
        if (ans == gus){
            printf("答對了!\n");
            break;
        }
          printf("答錯了!\n");
    }
   
    
    
   return 0;
}
