%{
    #include <stdio.h>
    #include <stdlib.h>
%}


%%
"//"[^\n]*              { printf("Single-line comment: %s\n", yytext); }

"/*"([^*]|\*+[^*/])*\*+"/"   { printf("Multi-line comment: %s\n", yytext); }

[a-zA-Z_][a-zA-Z0-9_]*       { printf("Identifier: %s\n", yytext); }

[0-9]+                       { printf("Constant: %s\n", yytext); }

[+\-*/%<>=]+               { printf("Operator: %s\n", yytext); }

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