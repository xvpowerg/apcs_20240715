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
    int replay = 0;
    do{
        printf("請輸入整數:");
        scanf("%d",&input);
        int ans = input % 2;
        printf("是否為奇數:%c\n",ans?'Y':'N');
        printf("繼續1結束0?");
        scanf("%d",&replay);
    }while(replay);
    
    
   return 0;
}
