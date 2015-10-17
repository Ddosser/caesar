
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
char kaiser[] =
  "U8Y]:8KdJHTXRI>XU#?!K_ecJH]kJG*bRH7YJH7YSH]*=93dVZ3^S8*$:8\"&:9U]RH;g=8Y!U92‘=j*$KH]ZSj&[S#!gU#*dK9\\.";
 /* 记得转义 */
int
main ()
{
  char ch[1000];
  int flag = 1;
  int i,j;
  for (i = 0; i < 127; i++)
    {
      memset (ch, 0, sizeof (ch));
      for (j = 0; j < strlen (kaiser); j++)
	{
	  ch[j] = (kaiser[j] + i) % 127;
	  if (ch[j] <= 32 || ch[j] > 127)
	    flag = 0;
	}

	   printf("%s",ch);
    }
  return 0;
}
