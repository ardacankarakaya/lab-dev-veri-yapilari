#include <stdio.h>
#include <stdlib.h>

// ---- Bağlı Liste ----

struct Node {
    int data;
    struct Node* next;
};

struct Node* head = NULL;

void addEnd(int x) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = x;
    newNode->next = NULL;

    if (head == NULL) {
        head = newNode;
        return;
    }

    struct Node* temp = head;
    while (temp->next != NULL)
        temp = temp->next;

    temp->next = newNode;
}

void addMiddle(int pos, int x) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = x;

    struct Node* temp = head;
    int i = 0;
    while (temp != NULL && i < pos - 1) {
        temp = temp->next;
        i++;
    }

    if (temp == NULL) return;

    newNode->next = temp->next;
    temp->next = newNode;
}

void showList() {
    struct Node* temp = head;
    while (temp != NULL) {
        printf("%d -> ", temp->data);
        temp = temp->next;
    }
    printf("NULL\n");
}

// ---- Stack ----

int stack[100];
int top = -1;

void push(int x) {
    if (top < 99) {
        stack[++top] = x;
    }
}

int pop() {
    if (top >= 0) {
        return stack[top--];
    }
    return -1;
}

int peek() {
    if (top >= 0) {
        return stack[top];
    }
    return -1;
}

void showStack() {
    for (int i = 0; i <= top; i++) {
        printf("%d ", stack[i]);
    }
    printf("\n");
}

// ---- Main ----

int main() {

    // Bağlı liste deneme
    addEnd(10);
    addEnd(20);
    addEnd(40);
    addMiddle(1, 30);
    printf("Bagli Liste: ");
    showList();

    // Stack 15 işlem
    push(10);
    push(20);
    push(30);
    push(40);
    push(50);
    push(60);
    push(70);
    push(80);
    push(90);
    push(100);
    pop();
    pop();
    push(110);
    push(120);
    push(130);

    printf("Stack: ");
    showStack();

    return 0;
}