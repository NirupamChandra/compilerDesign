%{
#include<stdio.h>
#include<stdlib.h>
int yylex();
int yyerror(const char *s);
%}

%token NUMBER ID
%left '+' '-'
%left '*' '/'
%left '(' ')'

%%

E : T   {printf("value is : %d\n", $$); exit(0);}

T:  |T '+' T	{ $$ =  $1+$3; }
	| T '-' T	{ $$ =  $1-$3; }
	| T'*'T	    { $$ =  $1*$3; } 
	| T '/' T	{ $$ =  $1/$3; }  
	| '-' NUMBER { $$ = -$2; }
	| '-' ID { $$ = -$2; }
	| '-' '(' T ')'  { $$ = $2; }
	| NUMBER { $$ = $1; }
	| ID { $$ = $1; }
	;
%%

int main()
{
	printf("Enter the expression\n");
	yyparse();
	printf("Expression is valid\n");
	return 0;

}

int yyerror(const char *s)
{
	printf("\n expression is invalid\n");
    exit(0);
}