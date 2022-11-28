#include "lists.h"
/**
 * check_cycle - checks is a singly linked list has a cycle
 * @list: pointer to linked list
 * Return: 0 if no cycle else 1
 */
int check_cycle(listint_t *list)
{
  listint_t *current, *first;

  if (list == NULL)
    return (0);
  current = first = list;
  for (;(current = current->next) != NULL;)
    if (current == first)
      return (1);
  return (0);
}
