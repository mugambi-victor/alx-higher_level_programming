#include "lists.h"
#include <stddef.h>
#include <stdlib.h>
#include <stdio.h>
/**
 * insert_node - Inserts a new node with
 * a given number into a sorted linked list.
 * @head: Pointer to the head of the linked list.
 * @number: Integer value to be inserted.
 *
 * Return: Address of the new node or NULL if memory allocation fails.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current;
	listint_t *prev;
	listint_t *new_node = (listint_t *)malloc(sizeof(listint_t));

	if (new_node == NULL)
	{
		printf("Memory allocation failed.\n");
		return (NULL);
	}
	new_node->n = number;
	new_node->next = NULL;

	current = *head;
	prev = NULL;

	while (current != NULL && current->n < number)
	{
		prev = current;
		current = current->next;
	}
	if (prev == NULL)
	{
		new_node->next = *head;
		*head = new_node;
	}
	else
	{
		prev->next = new_node;
		new_node->next = current;
	}
	return (new_node);
}
