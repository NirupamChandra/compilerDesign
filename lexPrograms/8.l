%{
    #include <stdio.h>
    #include <stdlib.h>
    int lc = 0;
    int wc = 0;
%}


%%

[\n]*                 {lc += 1;}

[a-zA-Z0-9_][a-zA-Z0-9_]+         { wc+=1; }

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

    printf("WC : %d\n", wc);
    printf("LC : %d\n", lc);
}

int yywrap(){
    return 1;
}