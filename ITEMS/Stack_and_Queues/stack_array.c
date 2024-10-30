#include <stdio.h>
#include <stdlib.h>
#define LIMIT 100 //Maximum limit of the stack
// Global declaration of variables

int stack[LIMIT]; // Array implementation
int top; // To insert and delete the data elements in the stack
int i;
int choice; // To choose either of the stack operations

void push(); // Inserts element into the stack
void pop(); // Deletes element from stack
void display(); // Displays all the elements in the stack

int main()
{
	printf("Welcome to Ryan's Tutorials!\n\n");

	printf("ARRAY IMPLEMENTATION USING STACKS\n\n");

	top = -1; // Initializing top to -1 idicates that it is empty
do
{
	printf("1. Insert\n2. Delete\n3. Display\n4. Exit\n\n");
	printf("Enter your choice: \n");
	scanf("%d", &choice);

	switch(choice)
	{
		case 1:
		push();
		break;
		case 2:
		pop();
		break;
		case 3:
		display();
		break;
		case 4:
		exit(0);
		break;
		default:
		printf("Sorry! invalid choice\n");
		break;
	}
} while(choice != 4);

return 0;
}

void push()
{
	int element;

	if(top == LIMIT - 1)
	{
		printf("Stack underflow\n");
	}
	else
	{
		printf("Enter the element to be inserted: ");
		scanf("%d", &element);
		top++;
		stack[top] = element;
	}
}

void pop()
{
	int element;
	if(top == -1)
	{
		printf("Stack UnderFlow\n");
	}
	else
	{
		element = stack[top];
		printf("The deleted item is %d\n", stack[top]);
		top--; // Element below the top most element is deleted
	}
}
void display()
{
	if (top == -1)
	{
		printf("Stack underflow\n");//empty stack
	}
	else if(top > 0)
	{
		printf("The elements of the stack are:\n");
		for(i = top; i >= 0; i--) // top to bottom traversal
	{
		printf("%d\n", stack[i]);
	}
	}
}
