%{
#include<stdio.h>
#include"temp10.tab.h"
%}

%%
[0-9]+          {yylval=atoi(yytext);   return NUMBER;}
[a-zA-Z]+       {return ID;}
[\-\+\*\/]		return yytext[0];
[ \t]+ 	         {/*skip others...*/}

%%

int yywrap()
{
    return 1;
}
