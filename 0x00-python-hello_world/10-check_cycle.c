#include <stdio.h>
#include "lists.h"
/**
 * check_cycle - Checks if a linked list has a cycle.
 *
 * @list: A pointer to the head of the linked list.
 *
 * Return: 1 if there is a cycle, 0 otherwise.
 */
int check_cycle(listint_t *list)
{
	while (list != NULL)
	{
		if (list->flag == 1)
		{
			return (1);
		}
		list->flag = 1;
		list = list->next;
	}
	return (0);
}
