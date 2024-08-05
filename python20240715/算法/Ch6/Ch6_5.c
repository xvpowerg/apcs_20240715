/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <stdio.h>

int main()
{ int b1 = 0,b2 = 1;

   int ans1 = b1 && b2;
   int ans2 = b1 || b2;
   int ans3 = !b2;
   
   printf("%d\n",ans1);
   printf("%d\n",ans2);
   printf("%d\n",ans3);
   return 0;
}
