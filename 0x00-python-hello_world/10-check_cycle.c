#include "lists.h"
/**
 * check_cycle - checks is a singly linked list has a cycle
 * @list: pointer to linked list
 * Return: 0 if no cycle else 1
 */
int check_cycle(listint_t *list)
{
	listint_t *ptr1, *ptr2;

	if (!list)
		return (0);

	ptr1 = list;
	ptr2 = list->next;

	while (ptr1 != ptr2)
	{
		ptr1 = ptr1->next;
		if (!ptr1)
			return (0);
		
        ptr2 = ptr2->next;
		if (!ptr2)
			return (0);
		
        ptr2 = ptr2->next;
		if (!ptr2)
			return (0);
	}
	return (1);
}