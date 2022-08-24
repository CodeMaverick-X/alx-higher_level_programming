#include "lists.h"
#include <stdlib.h>
#include <unistd.h>

/**
 * insert_node - inserts a number in an ordered linked list
 * @head: double pointer to the linked list
 * @number: number to insert in the new node
 *
 * Return: address of the new node, or NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *bck;
	listint_t *frd;

	new = malloc(sizeof(listint_t));
	new->n = number;
	new->next = NULL;

	if (!(*head))
	{
		new->next = *head;
		*head = new;
		return (new);
	}

	if (!((*head)->next) || ((*head)->n > new->n))
	{
		if ((*head)->n < new->n)
		{
			(*head)->next = new;
			return (new);
		}
		else if (((*head)->n > new->n))
		{
			new->next = *head;
			*head = new;
			return (new);
		}
	}

	frd = (*head)->next;
	bck = *head;

	while (frd)
	{
		if ((new->n > bck->n) && (new->n > frd->n))
		{
			bck = frd;
			frd = frd->next;
		}
		if ((new->n >= bck->n) && (!(frd) || (new->n <= frd->n)))
		{
			new->next = frd;
			bck->next = new;
			return (new);
		}
	}
	return (NULL);
}
