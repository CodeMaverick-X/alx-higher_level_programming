#include "lists.h"
/**
 * check_cycle - function in C that checks if a
 * singly linked list has a cycle in it.
 *
 * @list: pointer to head of the list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list->next;

	if (!list)
		return (0);

	while ((fast != NULL) && slow)
	{
		if (slow == fast)
		{
			return (1);
		}

		fast = fast->next;
	}

	return (0);
}
