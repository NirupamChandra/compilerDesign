#include<iostream>
using namespace std;

typedef struct symbol{
    char name[50];
    char type[20];
    char scope[20];
    char value[50];
    struct symbol* next;
} symbol;

symbol* head = nullptr;

void takeIn(int p[], int x){

    for(int i=0; i<x; i++){
        printf("%d\t", p[i]);
        p[i] = i+1;
    }

}

int main(){
    int arr[10] = {1, 2, 3,4, 5};

    takeIn(arr, 10);
    for(int i=0; i<10; i++){
        printf("%d\t", arr[i]);
        arr[i] = i+1;
    }
}