#include <stdio.h>
#include <ctype.h>
#include <string.h>

int main() {
    char input[100];
    int i = 0;

    printf("Enter an expression: ");
    fgets(input, sizeof(input), stdin);

    while (input[i] != '\0') {

        // Skip spaces
        if (input[i] == ' ' || input[i] == '\t') {
            i++;
            continue;
        }

        // Check Identifier (starts with alphabet, can have digits later)
        if (isalpha(input[i])) {
            printf("Identifier: ");
            while (isalnum(input[i])) {
                printf("%c", input[i]);
                i++;
            }
            printf("\n");
        }

        // Check Number
        else if (isdigit(input[i])) {
            printf("Number: ");
            while (isdigit(input[i])) {
                printf("%c", input[i]);
                i++;
            }
            printf("\n");
        }

        // Check Operators
        else if (input[i] == '+' || input[i] == '-' || input[i] == '*' || input[i] == '/' ||
                 input[i] == '=' || input[i] == '<' || input[i] == '>') {
            printf("Operator: %c\n", input[i]);
            i++;
        }

        // Any other character
        else {
            printf("Unknown Symbol: %c\n", input[i]);
            i++;
        }
    }

    return 0;
}
