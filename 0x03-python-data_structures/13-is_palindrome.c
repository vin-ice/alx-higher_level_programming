#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
/**
 * is_palindrome - checks if singly linked list pointed to
 * is a palindrome
 * @head: pointer to list
 * Return: return 1 if true otherwwise 0
*/
int is_palindrome(listint_t **head)
{
    int stack [500], pos;
    listint_t *ptr = NULL;

    if (head == NULL || *head == NULL)
        return (0);
    ptr = *head;
    for (pos = 0; ptr->next; ptr = ptr->next, pos++)
    {
        if (pos == 0)/**first point, avoid seg fault*/
            stack[pos] = ptr->n;
        else if (ptr->n != stack[pos - 1]) /**compare with top*/    
            stack[pos] = ptr->n;
        else if (ptr->n == stack[pos - 1])/**on match*/
            pos -= 2;
    }
    if (pos == 1 && ptr->n == stack[0])
        return (1);
    return (0);
}