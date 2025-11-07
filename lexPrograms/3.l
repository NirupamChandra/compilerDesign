%{
    #include <stdio.h>
    #include <stdlib.h>
%}


%%

[A-Z][A-Z]+          { printf("Capital word : %s\n", yytext); }

.                           { /* skip every other*/}

%%

int main(){

    FILE *fp;

    fp = fopen("./test.c", "r" );

    if(!fp){
        printf("Error opening file.c\n");
        return 0;
    }

    yyin = fp;

    yylex();
}

int yywrap(){
    return 1;
}