#include "lists.h"
#include <stddef.h>
/**
 * is_palindrome - function in C that checks if a
 *  singly linked list is a palindrome.
 *  @head: pointer to start of linked list
 *  Return: 0 if it is not a palindrome, 1 if it is a palindrome
 *  Description: if head pointer is equal to null return 1
 *  set flag to 1 and assigned two pointers right and left
 *  to point to the start and end of the list and compare
 *  intigers at those nodes if the intigers are equal the left
 *  pointer is moved forward and the right is moved backward kind of
 *  with the use of a marker mk.. just read the code...
 */
int is_palindrome(listint_t **head)
{
	listint_t *lt = *head;
	listint_t *rt = *head;
	listint_t *mkr = NULL;
	int flag = 1;

	if (*head == NULL)
		return (1);

	while (flag == 1)
	{
		rt = *head;
		while (rt->next != mkr)
			rt = rt->next;
		mkr = rt;

		if (lt->n != rt->n)
		{
			flag = 0;
			break;
		}
		if (lt->next == rt || lt == rt)
			break;

		lt = lt->next;
	}
	return (flag);
}
