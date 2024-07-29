/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <stdio.h>

int main()
{ 
    //請使用者輸入五筆成績 並加總 與 算出平均值
    //成績必須在 0 ~ 100 
    
   int i = 1,sum =0;
   for (;i <= 5;){
       int score = 0;
       printf("請輸入分數:");
       scanf("%d",&score);
       if(score < 0 || score > 100){
           printf("輸入錯誤的成績\n");
           continue;
       }
       i++;
       sum += score;
   }
   printf("總成績:%d",sum);
   printf("平均成績:%.2f",(double)sum/5);
   return 0;
}
